# Password Automation Tool

## Overview
The **Password Automation Tool** is a Python script designed to automate the process of copying passwords from a CSV file and pasting them into input fields. It follows a sequence of actions: copying the password, pasting it, selecting all, deleting, and pasting again. This tool enhances efficiency and accuracy when dealing with bulk password management tasks.

## Features
- Automatically reads passwords from a CSV file.
- Simulates keyboard actions for pasting, selecting, and deleting passwords.
- Ensures secure and accurate password input.
- User-friendly and lightweight.

## Prerequisites
Before running the tool, ensure you have the following installed:

- **Python 3.x**
- Required dependencies (install using the command below):
  ```bash
  pip install -r requirements.txt
  ```

## Installation
1. Clone this repository to your local machine:
   ```bash
   git clone https://github.com/mad1fyJourn3y/PassAutomationTool.git
   ```
2. Navigate to the project directory:
   ```bash
   cd PassAutomationTool
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
1. Prepare your CSV file containing passwords with the following format:
   ```csv
   username,password
   user1,password123
   user2,password456
   ```
2. Run the script:
   ```bash
   python password_automation.py -i
   ```
   Now wait for 5 seconds after the CSV file finishes its file clean for it to start
3. Follow on-screen prompts to select the desired password entry.

## Configuration
You can modify the script to customize:
- **Input file path** – Change the default CSV file location.
- **Hotkeys** – Adjust keyboard shortcuts for pasting and selecting.

## Security Considerations
- Use this tool responsibly and avoid exposing sensitive credentials.
- Ensure your environment is secure when running automation scripts.

## Troubleshooting
- Ensure the correct CSV format is used.
- Verify dependencies are properly installed.
- Run the script with appropriate permissions if encountering access issues.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing
Contributions are welcome! Please fork the repository and submit a pull request with your improvements.

## Contact
For any issues or inquiries, feel free to reach out via email: [ninitekali@gmail.com](mailto:ninitekali@gmail.com)

---

**Author:** mad1fy
GitHub: [mad1fyjourn3y](https://github.com/mad1fyjourn3y)  
Instagram: [mad1fy_](https://instagram.com/mad1fy_)  
TikTok: [mad1fy_](https://tiktok.com/@mad1fy_)

