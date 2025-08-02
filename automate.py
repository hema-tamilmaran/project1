import os
import shutil
import re
import requests

def move_jpg_files():
    source = input("Enter source folder path: ").strip()
    destination = input("Enter destination folder path: ").strip()

    os.makedirs(destination, exist_ok=True)

    moved = 0
    for filename in os.listdir(source):
        if filename.lower().endswith('.jpg'):
            src_path = os.path.join(source, filename)
            dest_path = os.path.join(destination, filename)
            shutil.move(src_path, dest_path)
            print(f"Moved: {filename}")
            moved += 1

    print(f"Total .jpg files moved: {moved}")

def extract_emails():
    input_file = input("Enter path to the input .txt file: ").strip()
    output_file = input("Enter path for output email file (e.g., emails.txt): ").strip()

    with open(input_file, 'r') as file:
        content = file.read()

    emails = re.findall(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', content)

    with open(output_file, 'w') as file:
        for email in emails:
            file.write(email + '\n')

    print(f"Extracted {len(emails)} email(s) and saved to '{output_file}'.")

def scrape_webpage_title():
    url = input("Enter webpage URL (e.g., https://example.com): ").strip()
    output_file = input("Enter path for output file (e.g., title.txt): ").strip()

    try:
        response = requests.get(url)
        html_content = response.text

        match = re.search(r'<title>(.*?)</title>', html_content, re.IGNORECASE)
        if match:
            title = match.group(1)
            with open(output_file, 'w') as file:
                file.write(f"Title of {url}:\n{title}")
            print(f"Title extracted and saved: {title}")
        else:
            print("Title tag not found.")
    except Exception as e:
        print(f"Error fetching URL: {e}")

def main():
    print("Choose a task to automate:")
    print("1. Move all .jpg files to another folder")
    print("2. Extract emails from a .txt file")
    print("3. Scrape the title of a webpage")
    choice = input("Enter your choice (1/2/3): ")

    if choice == '1':
        move_jpg_files()
    elif choice == '2':
        extract_emails()
    elif choice == '3':
        scrape_webpage_title()
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
