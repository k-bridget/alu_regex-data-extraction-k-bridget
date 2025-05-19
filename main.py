#!/usr/bin/env python3
import re
def extract_emails(text):
    pattern = r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+'
    return re.findall(pattern, text)
def extract_phone_numbers(text):
    pattern = r'(\(?\d{3}\)?[\s.-]?\d{3}[\s.-]\d{4})'
    return re.findall(pattern, text)
def extract_credit_cards(text):
    pattern = r'\b(?:\d{4}[- ]?){3}\d{4}\b'
    return re.findall(pattern, text)
def extract_time(text):
    pattern = r'\b(?:[01]?[0-9]|2[0-3]):[0-5][0-9](?: ?[APap][Mm])?\b'
    return re.findall(pattern, text)

if __name__ == "__main__":
    info = """
    Contact me at user@example.com or firstname.lastname@company.co.uk
    Call me: (123) 456-7890 or 123-456-7890 or 123.456.7890
    My card: 1234 5678 9012 3456 or 1234-5678-9012-3456
    Meeting at 14:30 or 2:30 PM
    """

    print("Emails:", extract_emails(info))
    print("Phones:", extract_phone_numbers(info))
    print("Credit Cards:", extract_credit_cards(info))
    print("Time:", extract_time(info))
