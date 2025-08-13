 -->Contact Management System (Python + Tkinter)
A simple GUI-based Contact Management System built using Python's Tkinter library.
This application allows users to store, view, edit, and delete contact information.
All contacts are saved in a JSON file for persistent storage, so data remains even after closing the application.

✨ Features
➕ Add Contact – Store name, phone number, and email address

📋 View Contacts – Display all saved contacts in a list

✏️ Edit Contact – Update existing contact information

🗑️ Delete Contact – Remove contacts from the list

💾 Persistent Storage – Contacts are saved in contacts.json

🛠️ Technologies Used
Python 3

Tkinter – for building the GUI

JSON – for storing data

📂 File Structure
bash
Copy
Edit
📁 Contact-Management-System
│── main.py         # Main application code
│── contacts.json   # Data file for storing contacts
│── .gitignore      # Ignore unnecessary files in Git
│── README.md       # Project documentation
🚀 How to Run
Clone the repository

bash
Copy
Edit
git clone https://github.com/your-username/contact-management-system.git
cd contact-management-system
Run the app

bash
Copy
Edit
python main.py
📦 Packaging into .exe (Optional)
If you want to run it as a standalone application without Python:

bash
Copy
Edit
pip install pyinstaller
pyinstaller --onefile --noconsole main.py
The .exe file will be available in the dist/ folder.