import os
import shutil
import re
import requests

# 1) Move all .jpg files
def move_jpg_files():
    src = input("Enter source folder path: ")
    dst = input("Enter destination folder path: ")
    os.makedirs(dst, exist_ok=True)

    count = 0
    for file in os.listdir(src):
        if file.lower().endswith(".jpg"):
            shutil.move(os.path.join(src, file), os.path.join(dst, file))
            count += 1
    print(f"Moved {count} .jpg file(s) to {dst}")

# 2) Extract all email addresses from .txt
def extract_emails():
    txt_file = input("Enter path of .txt file: ")
    with open(txt_file, "r", encoding="utf-8") as f:
        text = f.read()
    emails = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", text)
    with open("emails.txt", "w", encoding="utf-8") as f:
        for email in set(emails):
            f.write(email + "\n")
    print(f"Extracted {len(set(emails))} email(s) to emails.txt")

# 3) Scrape title of a fixed webpage
def scrape_title():
    url = "https://www.python.org"  # fixed webpage
    html_text = requests.get(url).text
    match = re.search(r"<title>(.*?)</title>", html_text, re.IGNORECASE | re.DOTALL)
    if match:
        title = match.group(1).strip()
        with open("title.txt", "w", encoding="utf-8") as f:
            f.write(title)
        print(f"Scraped title: {title} (saved to title.txt)")
    else:
        print("Title not found.")

# Menu
while True:
    print("\nTask Automation Menu:")
    print("1. Move .jpg files")
    print("2. Extract emails from .txt")
    print("3. Scrape webpage title")
    print("0. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        move_jpg_files()
    elif choice == "2":
        extract_emails()
    elif choice == "3":
        scrape_title()
    elif choice == "0":
        break
    else:
        print("Invalid choice, try again.")
