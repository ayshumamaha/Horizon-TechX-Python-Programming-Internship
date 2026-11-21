import re
import os

# Input and output filenames
input_file = "input_emails.txt"
output_file = "extracted_emails.txt"

print("=" * 45)
print("       EMAIL EXTRACTION AUTOMATION")
print("=" * 45)

# Create a sample input file if it does not exist
if not os.path.exists(input_file):

    sample_text = """
    Contact us at support@example.com.
    For enquiries, email info@company.com.
    You can also reach admin@gmail.com.
    Invalid address: example@.
    Another contact: contact@website.org.
    """

    with open(input_file, "w") as file:
        file.write(sample_text)

    print("\nSample input file created:", input_file)

# Read the input file
try:
    with open(input_file, "r") as file:
        text = file.read()

    # Regular expression to identify email addresses
    pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b'

    # Extract email addresses
    emails = re.findall(pattern, text)

    # Remove duplicate addresses
    emails = list(dict.fromkeys(emails))

    # Save extracted addresses
    with open(output_file, "w") as file:

        if emails:
            for email in emails:
                file.write(email + "\n")
        else:
            file.write("No email addresses found.")

    # Display results
    print("\nEmail Extraction Completed!")
    print("-" * 35)

    if emails:
        print("Extracted Email Addresses:")

        for email in emails:
            print(email)

        print("\nTotal emails found:", len(emails))

    else:
        print("No email addresses were found.")

    print("\nResults saved to:", output_file)

except OSError as error:
    print("File handling error:", error)

print("\nAutomation process completed.")
