# 🔐 Secure Data Encryption System

A **Streamlit-based Secure Data Encryption App** that allows users to register, log in, and securely **encrypt/decrypt personal data** using passkey-protected encryption. Built as part of **GIAIC Assignment #5** under the mentorship of **Sir Hamzah Syed**, this project emphasizes **data confidentiality, authentication, and access control**.

**Secure data** means protecting **sensitive information** from unauthorized access by using encryption and strong authentication methods. It ensures that your data remains confidential, intact, and accessible only to those with the right permissions — giving you peace of **mind in a digital world full of threats**.

---

## 📌 Features

- ✅ **User Registration & Login** with password hashing (SHA-256)  
- 🔑 **Fernet-based encryption** with passkey  
- 🛡️ **Brute-force protection** with lockout after multiple failed attempts  
- 📁 **Data saved in JSON** format for persistent storage  
- 🔍 **Search and view** encrypted entries by title  
- 📂 **View all encrypted records** for the logged-in user  
- 🔐 **Session-based access control** using Streamlit session state  

---

## ⚙️ Technologies Used

- **Python 3**  
- **Streamlit** – for building the interactive UI  
- **Cryptography (Fernet)** – for secure encryption and decryption  
- **Hashlib** – for password hashing (SHA-256)  
- **PBKDF2** – for key derivation  
- **JSON** – for user and data persistence  

---

## 📁 Project Structure

secure-data-encryption/
│
├── src/
│ ├── encryption/
│ │ └── fernet_handler.py # Fernet encryption/decryption logic
│ ├── utils/
│ │ ├── file_handler.py # File I/O and password hashing
│ │ └── lockout_handler.py # Lockout mechanism for failed login attempts
│
├── data.json # Central data and user store
├── app.py # Main Streamlit application
└── README.md # Project documentation

---

## 🧪 **Sample Use Cases**

- Create a new account with a unique username and password  
- Log in to your account  
- Encrypt sensitive data using a custom passkey  
- Decrypt stored data by providing the correct passkey  
- Search for encrypted entries by title  
- View all saved entries and decrypt them securely  

---
