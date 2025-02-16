#!/usr/bin/python3

import copy
import os
import sys
import zipfile
from bs4 import BeautifulSoup


# Function to process an XHTML file
def process_xhtml(file_path):
    print(f"Processing XHTML file: {file_path}")

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()

        soup = BeautifulSoup(content, 'html.parser')

        # Find the div with class bodyTxt
        body_txt = soup.find('div', class_='bodyTxt')
        if not body_txt:
            print(f"No 'div' with class 'bodyTxt' found in {file_path}")
            return

        # Find all H3 elements
        h2_tags = body_txt.find_all('h3')
        if len(h2_tags) < 2:
            print(f"Less than two H3 tags found in {file_path}")
            return

        # Process elements following the second H3
        for element in h2_tags[2].find_all_next():
            if element.name == 'div' and element.get('id', '').startswith('tt') and not element.find('h2'):
                print(f"Wrapping div with id {element.get('id')} in a new tag in {file_path}")
                new_tag = soup.new_tag('div')
                element.wrap(new_tag)

        # Save changes back to the file
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(str(soup))
        print(f"File processed and saved: {file_path}")

    except Exception as e:
        print(f"Error processing {file_path}: {e}")


# Function to extract and process EPUB files
def process_epub(epub_path):
    print(f"Processing EPUB file: {epub_path}")

    try:
        with zipfile.ZipFile(epub_path, 'r') as zip_ref:
            extract_dir = "extracted_epub"
            zip_ref.extractall(extract_dir)
        print(f"EPUB extracted to {extract_dir}")

        oebps_path = os.path.join(extract_dir, "OEBPS")

        if not os.path.exists(oebps_path):
            print("OEBPS folder not found in the EPUB structure")
            return

        # Locate all XHTML files to process
        for root, dirs, files in os.walk(oebps_path):
            for file_name in files:
                if file_name.endswith(".xhtml") and "-extracted" not in file_name:
                    file_path = os.path.join(root, file_name)
                    print(f"Found XHTML file to process: {file_path}")
                    process_xhtml(file_path)

        # Optional: Re-compress the EPUB
        output_epub = "./OUTPUT/" + os.path.basename(epub_path)
        os.makedirs(os.path.dirname(output_epub), exist_ok=True)
        with zipfile.ZipFile(output_epub, 'w') as zip_ref:
            for root, dirs, files in os.walk(extract_dir):
                for file in files:
                    file_path = os.path.join(root, file)
                    arcname = os.path.relpath(file_path, extract_dir)
                    zip_ref.write(file_path, arcname)
        print(f"Processed EPUB saved as {output_epub}")

    except Exception as e:
        print(f"Error processing EPUB {epub_path}: {e}")


# Main function
def main():
    # Ensure a file path is passed as an argument
    if len(sys.argv) != 2:
        print("Usage: Drag and drop a file onto this script to process it.")
        return

    # Get the file path from the arguments
    file_path = sys.argv[1]
    print(f"Starting processing for file: {file_path}")
    process_epub(file_path)


if __name__ == "__main__":
    main()