import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from tkinter import Tk, filedialog, messagebox, Button, Label
import time
import urllib.parse

def send_whatsapp_message(phone, message):
    url = f"https://web.whatsapp.com/send?phone={phone}&text={urllib.parse.quote(message)}"
    driver.get(url)
    try:
        # Wait for message box to load and send message
        time.sleep(10)
        send_box = driver.find_element(By.XPATH, "//div[@contenteditable='true'][@data-tab='10']")
        send_box.send_keys(Keys.ENTER)
        time.sleep(2)
    except Exception as e:
        print(f"Error sending message to {phone}: {e}")

def send_messages(excel_path):
    df = pd.read_excel(excel_path)

    for index, row in df.iterrows():
        name = str(row.get('Name', '')).strip()
        status = str(row.get('Status', '')).strip().lower()
        raw_phone = str(row.get('Parent Number', '')).strip().replace(' ', '')

        # Add +91 if number has only 10 digits
        if len(raw_phone) == 10 and raw_phone.isdigit():
            phone = '+91' + raw_phone
        elif raw_phone.startswith('+91') and len(raw_phone) == 13:
            phone = raw_phone
        else:
            print(f"Skipping invalid number: {raw_phone}")
            continue

        if status == 'absent':
            msg = f"Dear Parent, your child {name} was marked absent today. Please ensure regular attendance."
            send_whatsapp_message(phone, msg)

        elif status == 'left':
            msg = f"Dear Parent, your child {name} has left school early today. Please confirm the reason."
            send_whatsapp_message(phone, msg)

    messagebox.showinfo("Done", "All messages have been sent.")

def open_file():
    file_path = filedialog.askopenfilename(title="Select Excel File", filetypes=[("Excel Files", "*.xlsx")])
    if file_path:
        send_messages(file_path)

# Set up GUI
root = Tk()
root.title("Attendance Notifier - WhatsApp")
root.geometry("400x200")
Label(root, text="Free WhatsApp Attendance Notifier", font=("Arial", 14, "bold")).pack(pady=20)
Button(root, text="Select Attendance Excel File", command=open_file, font=("Arial", 12)).pack(pady=10)

# Start browser driver
driver = webdriver.Chrome()  # Make sure chromedriver is available
driver.get("https://web.whatsapp.com")
messagebox.showinfo("WhatsApp Login", "Scan the QR code in the opened browser, then click OK here once WhatsApp Web loads.")

root.mainloop()
driver.quit()
