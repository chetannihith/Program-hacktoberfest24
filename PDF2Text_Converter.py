import PyPDF2
import pdfplumber

def extract_text_pypdf2(pdf_path, output_txt, pages=None):
    with open(pdf_path, "rb") as pdf_file:
        reader = PyPDF2.PdfReader(pdf_file)
        with open(output_txt, "w", encoding="utf-8") as txt_file:
            if pages is None:  # Extract all pages
                for page_num in range(len(reader.pages)):
                    page_text = reader.pages[page_num].extract_text()
                    txt_file.write(f"Page {page_num + 1}:\n")
                    txt_file.write(page_text if page_text else "No text found on this page.\n")
                    txt_file.write("\n" + "-"*50 + "\n")
            else:  # Extract specified pages
                for page_num in pages:
                    page_text = reader.pages[page_num].extract_text()
                    txt_file.write(f"Page {page_num + 1}:\n")
                    txt_file.write(page_text if page_text else "No text found on this page.\n")
                    txt_file.write("\n" + "-"*50 + "\n")
    print(f"Text extracted and saved to {output_txt} using PyPDF2.")


def extract_text_pdfplumber(pdf_path, output_txt, pages=None):
    with pdfplumber.open(pdf_path) as pdf:
        with open(output_txt, "w", encoding="utf-8") as txt_file:
            if pages is None:  # Extract all pages
                for page_num in range(len(pdf.pages)):
                    page = pdf.pages[page_num]
                    page_text = page.extract_text()
                    txt_file.write(f"Page {page_num + 1}:\n")
                    txt_file.write(page_text if page_text else "No text found on this page.\n")
                    txt_file.write("\n" + "-"*50 + "\n")
            else:  # Extract specified pages
                for page_num in pages:
                    page = pdf.pages[page_num]
                    page_text = page.extract_text()
                    txt_file.write(f"Page {page_num + 1}:\n")
                    txt_file.write(page_text if page_text else "No text found on this page.\n")
                    txt_file.write("\n" + "-"*50 + "\n")
    print(f"Text extracted and saved to {output_txt} using pdfplumber.")


def main():
    pdf_path = input("Enter the path to the PDF file: ")
    output_txt = input("Enter the output .txt file name: ")
    pages_input = input("Enter specific pages to extract (e.g., 1,2,3) or press Enter to extract all: ")
    
    if pages_input:
        pages = [int(p) - 1 for p in pages_input.split(",")]  # Convert to zero-based page index
    else:
        pages = None

    choice = input("Choose library for extraction:\n1. PyPDF2\n2. pdfplumber\nEnter choice (1 or 2): ")

    if choice == '1':
        extract_text_pypdf2(pdf_path, output_txt, pages)
    elif choice == '2':
        extract_text_pdfplumber(pdf_path, output_txt, pages)
    else:
        print("Invalid choice. Please select 1 or 2.")

if __name__ == "__main__":
    main()
