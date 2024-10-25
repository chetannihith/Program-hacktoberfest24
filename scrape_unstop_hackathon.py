import requests
import time
import pandas as pd
from datetime import datetime

# Define headers for the request
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.6613.138 Safari/537.36",
    "Accept-Language": "en-GB,en;q=0.8",
    "Accept-Encoding": "gzip, deflate, br",
    "Connection": "keep-alive",
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "X-Requested-With": "XMLHttpRequest",
    # "Referer" will be dynamically set based on oppstatus
}

def days_in_month(date_str):
    """
    Helper function to get the number of days in the month of the given date.
    
    Args:
        date_str (str): Date in 'YYYY-MM-DDTHH:MM:SS+HH:MM' format
    
    Returns:
        int or str: Number of days in that month (28, 29, 30, 31) or 'N/A' if parsing fails
    """
    try:
        # Use fromisoformat to parse the date string
        date_obj = datetime.fromisoformat(date_str)
    except ValueError:
        print(f"Date format error: {date_str}")
        return "N/A"
    
    if date_obj.month == 2:
        # Check for leap year
        is_leap = date_obj.year % 4 == 0 and (date_obj.year % 100 != 0 or date_obj.year % 400 == 0)
        return 29 if is_leap else 28
    # Days in each month
    days_in_months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    return days_in_months[date_obj.month - 1]


def calculate_deadline(durations, text, start_date):
    """
    Calculate the actual number of days left for the application deadline.
    
    Args:
        durations (int or str): The duration value (either days or months).
        text (str): Text that indicates whether the duration is in days or months (e.g., '29 days left', '2 months left').
        start_date (str): The start date of the hackathon posting.
    
    Returns:
        int or str: Calculated number of days left or "N/A" if calculation fails
    """
    try:
        durations = int(durations)
    except (ValueError, TypeError):
        print(f"Invalid duration value: {durations}")
        return "N/A"

    if "day" in text.lower():
        return durations  # It's already in days
    elif "month" in text.lower():
        days_in_this_month = days_in_month(start_date)
        if isinstance(days_in_this_month, int):
            return durations * days_in_this_month  # Convert months to days based on month length
    return "N/A"  # If the text doesn't match known patterns


def extract_page(url, params):
    """
    Fetches data from the given URL with specified parameters.
    
    Args:
        url (str): The API endpoint URL.
        params (dict): Query parameters for the GET request.
    
    Returns:
        dict: JSON response if successful, else None.
    """
    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()  # Raise HTTPError for bad responses
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
        return None

def scrape_hackathons():
    """
    Scrapes hackathon listings from Unstop for different hackathon statuses and saves the data to a combined CSV file.
    """
    base_url = "https://unstop.com/api/public/opportunity/search-result"
    oppstatuses = ["open", "closed", "recent", "expired"]  # Define the statuses to scrape
    max_hackathons_per_status = 2180  # Maximum hackathons to scrape per status
    hackathons_per_page = 30  # Number of hackathons per API call (adjust based on API limits)

    all_hackathons = []

    for status in oppstatuses:
        print(f"\nScraping hackathons with oppstatus='{status}'")
        search_params = {
            "opportunity": "hackathons",
            "oppstatus": status,
            "page": 1,
            "size": hackathons_per_page
        }
        
        # Update the Referer header dynamically for each oppstatus
        headers["Referer"] = f"https://unstop.com/api/public/opportunity/search-result?opportunity=hackathons&oppstatus={status}"

        hackathons_scraped = 0  # Counter for hackathons scraped per status

        while hackathons_scraped < max_hackathons_per_status:
            print(f"Scraping page {search_params['page']} for status='{status}'...")
            data = extract_page(base_url, search_params)
            
            if data and "data" in data and "data" in data["data"]:
                hackathons = data["data"]["data"]
                if not hackathons:
                    print(f"No more hackathons found for status='{status}' on page {search_params['page']}.")
                    break  # Exit loop if no hackathons are found
                
                for hackathon in hackathons:
                    # Extract basic information safely
                    organisation = hackathon.get("organisation")
                    organisation_name = organisation.get("name", "N/A") if organisation else "N/A"

                    # Extract additional fields
                    applied = hackathon.get("registerCount", "N/A")
                    impressions = hackathon.get("viewsCount", "N/A")

                    # Extract eligibility from filters
                    filters = hackathon.get("filters", [])
                    eligibility_list = [filter_item.get("name", "N/A") for filter_item in filters]
                    eligibility = ", ".join(eligibility_list) if eligibility_list else "N/A"

                    # Extract category from filters
                    filters = hackathon.get("filters", [])
                    category_list = [filter_item.get("name", "N/A") for filter_item in filters]
                    category = ", ".join(category_list) if category_list else "N/A"

                    # Extract application deadline from regnRequirements -> remainingDaysArray -> durations and text
                    regn_requirements = hackathon.get("regnRequirements", {})
                    remaining_days_array = regn_requirements.get("remainingDaysArray", {})
                    duration = remaining_days_array.get("durations", 0)
                    text = remaining_days_array.get("text", "")
                    start_date = hackathon.get("start_date", "N/A")

                    if start_date != "N/A":
                        application_deadline = calculate_deadline(duration, text, start_date)
                    else:
                        application_deadline = "N/A"

                    hackathon_entry = {
                        "Title": hackathon.get("title", "N/A"),
                        "Organisations": organisation_name,
                        # "Location": location_str,
                        "Link": f"https://unstop.com/{hackathon.get('public_url', '')}",
                        "Uploaded On": start_date,
                        "Opportunity Type": hackathon.get("type", "N/A"),
                        "Status": status,  # Track the hackathon's oppstatus
                        "Applied": applied,
                        "Application Deadline": application_deadline,
                        "Impressions": impressions,
                        "Eligibility": eligibility,
                        "Category": category,
                        "Region": hackathon.get("region", "N/A")
                    }

                    all_hackathons.append(hackathon_entry)
                    hackathons_scraped += 1

                    if hackathons_scraped >= max_hackathons_per_status:
                        break  # Stop if we've reached the maximum number of hackathons
            
                print(f"Scraped {len(hackathons)} hackathons from page {search_params['page']} for status='{status}'. Total hackathons scraped for this status: {hackathons_scraped}")
                search_params["page"] += 1  # Move to the next page
                time.sleep(1)  # Polite delay to avoid overwhelming the server
            else:
                print("Invalid response structure or failed to retrieve data.")
                break

        print(f"Completed scraping {hackathons_scraped} hackathons for status='{status}'.")

    print(f"\nTotal hackathons scraped across all statuses: {len(all_hackathons)}")

    # Convert to DataFrame
    df = pd.DataFrame(all_hackathons)

    # Save to CSV
    csv_filename = 'scraped_hackathons.csv'
    df.to_csv(csv_filename, index=False, encoding='utf-8')
    print(f"Data saved to '{csv_filename}'")

    return df

if __name__ == "__main__":
    scrape_hackathons()
