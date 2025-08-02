import re

# Ask user for input file name
input_file = input("Enter the path of the .txt file: ")
output_file = "extracted_emails.txt"

try:
    # Read contents of the input file
    with open(input_file, 'r') as file:
        content = file.read()

    # Regular expression to find all email addresses
    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    emails = re.findall(email_pattern, content)

    if emails:
        # Write found emails to output file
        with open(output_file, 'w') as out_file:
            for email in emails:
                out_file.write(email + '\n')
        print(f"\n✅ {len(emails)} email(s) extracted and saved to '{output_file}'.")
    else:
        print("\n⚠️ No emails found in the file.")

except FileNotFoundError:
    print("❌ File not found. Please check the path and try again.")
except Exception as e:
    print(f"❌ An error occurred: {e}")
