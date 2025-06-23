# 📱 WhatsApp Attendance Notifier

A *Python-based automation tool* to notify parents via WhatsApp when a student is marked *Absent* or *Left Early* in the attendance sheet.
Messages are sent using *Selenium WebDriver* and *WhatsApp Web* — no paid APIs needed!

---

## ✨ Features

* ✅ Reads attendance from an Excel file (.xlsx)
* 📲 Automatically sends WhatsApp messages to parents
* 🖥 User-friendly GUI using *Tkinter*
* 💸 Completely free – no Twilio or external API required
* 🚨 Supports *"Absent"* and *"Left"* alerts

---

## 📁 Excel Format

Your Excel file should contain the following columns:

| Name       | Status  | Parent Number |
| ---------- | ------- | ------------- |
| John Doe   | Present | XXXXXXXXXX  |
| Jane Smith | Absent  | YYYYYYYYYY  |
| Max Lee    | Left    | ZZZZZZZZZZ  |

* Use *"Absent"* or *"Left"* (case-insensitive) to trigger message alerts.

---

## 💬 Message Templates

* *Absent*:
  "Dear Parent, your child **{Name}* was marked absent today. Please ensure regular attendance."*

* *Left*:
  "Dear Parent, your child **{Name}* has left school early today. Please confirm the reason."*

---

## 🚀 How to Use

### 1️⃣ Install Dependencies

bash
pip install selenium pandas openpyxl tk


### 2️⃣ Install ChromeDriver

* Download the version matching your Chrome from:
  [https://googlechromelabs.github.io/chrome-for-testing/](https://googlechromelabs.github.io/chrome-for-testing/)

* Place chromedriver(.exe) in your project folder or add it to your system PATH.

### 3️⃣ Run the Script

bash
python attendance_notifier.py


* WhatsApp Web will open in Chrome.
* Scan the QR code with your phone.
* Use the GUI to select your Excel attendance file.
* Messages will be sent automatically! ✅

---

## 🔐 Notes

* This tool uses *WhatsApp Web* — ensure:

  * Your phone is connected to the internet
  * You don’t close Chrome until all messages are sent
* 📢 Use responsibly to avoid being flagged as spam

---

## 🧑‍💻 Author

*Sushank Thatipally*
Feel free to *fork, enhance, and contribute!*

---

## 📜 License

*MIT License* – Use freely, but at your own risk.

---

## 📦 Extras (Optional Files)

Let me know if you'd like to add:

* 📄 .gitignore – Python-friendly
* 📊 sample_attendance.xlsx – Ready-to-use test file
* 🏷 Project badge or icon – Custom branding
