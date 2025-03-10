import os
import glob
import pywhatkit as kit
import pandas as pd
from models import Student
import time
from dotenv import load_dotenv
import messages

# Load environment variables from .env file
load_dotenv()

def send_whatsapp_message(phone, message):
    # Send a WhatsApp message using pywhatkit without the link box
    try:
        kit.sendwhatmsg_instantly(phone, message, 30, True, 10)
        print(f"Message sent to {phone}")
    except Exception as e:
        print(f"Failed to send message to {phone}: {e}")

def process_students(file_path, message_template):
    df = pd.read_excel(file_path)

    for index, row in df.iterrows():
        student = Student(
            name=row['Full name // Nome completo:'],
            email=row['E-mail adress // Endereço de e-mail'],
            phone=str(row['Cell phone with country code']),
            country=row['Country where you live'],
            languages=row['In what language do you prefer to be contacted?']
        )
        
        # Ensure the phone number starts with a '+' sign
        if not student.phone.startswith('+'):
            student.phone = '+' + student.phone

        # Use the corresponding message template for the message
        message = message_template.format(name=student.name, country=student.country, email=student.email)
        send_whatsapp_message(student.phone, message)

        # Wait for a few seconds before sending the next message
        time.sleep(5)  # Adjust the sleep time as needed

def main():
    # Define the directory containing the .xlsx files
    directory = 'languages'
    
    # Map file names to message templates
    message_map = {
        'english.xlsx': messages.messageEnglish,
        'italian.xlsx': messages.messageItalian,
        'portuguese.xlsx': messages.messagePortuguese,
        'french.xlsx': messages.messageFrench,
        'spanish.xlsx': messages.messageSpanish,
        'german.xlsx': messages.messageGerman,
    }

    # Get all .xlsx files in the specified directory
    xlsx_files = glob.glob(os.path.join(directory, '*.xlsx'))

    for file_path in xlsx_files:
        file_name = os.path.basename(file_path)  # Get the file name
        if file_name in message_map:
            print(f"Processing {file_name}...")
            process_students(file_path, message_map[file_name])
        else:
            print(f"No message template found for {file_name}. Skipping...")

if __name__ == "__main__":
    main()
