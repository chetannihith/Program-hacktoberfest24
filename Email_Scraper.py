import re
import requests
from bs4 import BeautifulSoup

def extract_emails_from_text(text):
    # Regular expression to find email addresses
    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    emails = re.findall(email_pattern, text)
    return emails

def extract_emails_from_url(url):
    try:
        # Send a request to the URL and get the content
        response = requests.get(url)
        response.raise_for_status()
        # Parse the content with BeautifulSoup
        soup = BeautifulSoup(response.text, "html.parser")
        text = soup.get_text()
        return extract_emails_from_text(text)
    except requests.exceptions.RequestException as e:
        print(f"Error fetching URL: {e}")
        return []

def extract_emails_from_file(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            text = file.read()
            return extract_emails_from_text(text)
    except FileNotFoundError:
        print("File not found. Please check the file path.")
        return []

# Main function to choose between URL or file input
def main():
    choice = input("Extract emails from:\n1. Website URL\n2. Text file\nEnter choice (1 or 2): ")

    if choice == "1":
        url = input("Enter the URL: ")
        emails = extract_emails_from_url(url)
        print("Emails found:", emails if emails else "No emails found.")
    
    elif choice == "2":
        file_path = input("Enter the file path: ")
        emails = extract_emails_from_file(file_path)
        print("Emails found:", emails if emails else "No emails found.")
    
    else:
        print("Invalid choice. Please enter 1 or 2.")

if __name__ == "__main__":
    main()
