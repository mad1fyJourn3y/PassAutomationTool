import csv
import pyperclip
import pyautogui
import time

# Input CSV file name
csv_file = 'chrome_passwords.csv'  # Change this to your actual file name

# Extract unique passwords
unique_passwords = set()

try:
    with open(csv_file, 'r') as infile:
        reader = csv.DictReader(infile)
        for row in reader:
            password = row.get('password', '').strip()
            if password:
                unique_passwords.add(password)  # Add unique passwords

    print(f"Found {len(unique_passwords)} unique passwords. Starting auto process...")

    time.sleep(5)  # Give time to switch to the target application

    for password in unique_passwords:
        pyperclip.copy(password)  # Copy password to clipboard
        
        # Simulate Ctrl + A (Select all) and Backspace (Delete)
        pyautogui.hotkey('ctrl', 'a')
        pyautogui.press('backspace')
        
        # Simulate Ctrl + V (Paste)
        pyautogui.hotkey('ctrl', 'v')

        # Simulate Enter key to submit
        pyautogui.press('enter')
        
        print(f"Pasted: {password}")
        
        time.sleep(2)  # Adjust delay as needed for processing

    print("All passwords processed successfully!")

except FileNotFoundError:
    print(f"Error: The file '{csv_file}' was not found.")
except Exception as e:
    print(f"An error occurred: {e}")
