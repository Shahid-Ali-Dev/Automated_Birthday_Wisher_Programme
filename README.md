# 🎂 Automated Birthday Wishing Program

This Python script automatically sends personalized birthday wishes to people on their special day.  
It uses a CSV file to store birthday details, randomly selects from multiple pre-written letter templates, and sends the greeting via email using Gmail's SMTP server.

## ✨ Features
- Automatically checks today's date and matches it with birthdays in a CSV file.
- Sends **personalized emails** with the recipient's name and age.
- Selects a **random letter template** from the `letter_templates` folder.
- Uses `.env` for secure storage of email credentials.
- Supports multiple birthdays on the same day.

## 📄 CSV File Format
The `birthdays.csv` file should look like this:

| name     | email              | year | month | day |
|----------|--------------------|------|-------|-----|
| Alice    | alice@example.com  | 1995 | 8     | 9   |
| Bob      | bob@example.com    | 1988 | 12    | 15  |

## 📝 Letter Template Format
Each letter template should contain placeholders:


## 🔑 Environment Variables
Create a `.env` file in the root directory:


> ⚠️ **Note:** If using Gmail, you must enable "App Passwords" in your Google account security settings.

## 🚀 How to Run
1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/birthday-wisher.git
   cd birthday-wisher
