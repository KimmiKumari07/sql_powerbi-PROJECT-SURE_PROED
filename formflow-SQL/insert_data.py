import gspread
from oauth2client.service_account import ServiceAccountCredentials
import mysql.connector
from config import MYSQL_CONFIG
from datetime import datetime

# Step 1: Connect to Google Sheet
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)
client = gspread.authorize(creds)
sheet = client.open("Data Form").sheet1
data = sheet.get_all_records()

# Step 2: Connect to MySQL
conn = mysql.connector.connect(**MYSQL_CONFIG)
cursor = conn.cursor()

# Step 3: Insert data
for row in data:
    formatted_timestamp = datetime.strptime(row['Timestamp'], "%m/%d/%Y %H:%M:%S").strftime("%Y-%m-%d %H:%M:%S")

    try:
        cursor.execute("""
            INSERT INTO responses (full_name, email, phone, course, feedback, timestamp)
            VALUES (%s, %s, %s, %s, %s, %s)
        """, (
            row['Full Name'],
            row['Email'],
            row['Phone Number'],
            row['Course Selected'],
            row['Feedback'],
            formatted_timestamp
        ))
        print("✅ Inserted:", row['Full Name'])
    except mysql.connector.errors.IntegrityError:
        print("⏭️ Skipped duplicate:", row['Full Name'])

conn.commit()
cursor.close()
conn.close()