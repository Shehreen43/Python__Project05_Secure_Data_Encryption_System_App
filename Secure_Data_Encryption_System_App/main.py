# Secure Data Encryption System App
import streamlit as st
import time
from src.encryption.fernet_handler import encrypt_data, decrypt_data
from src.utils.file_handler import load_data, save_data, load_users, save_users, hash_password
from src.utils.lockout_handler import handle_lockout

# Load users and data
users = load_users()
stored_data = load_data()

# Session state
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False
if 'username' not in st.session_state:
    st.session_state.username = ""
if 'failed_attempts' not in st.session_state:
    st.session_state.failed_attempts = 0
if 'lockout_time' not in st.session_state:
    st.session_state.lockout_time = 0

# Handle lockout with live countdown
if st.session_state.lockout_time > time.time():
    remaining = int(st.session_state.lockout_time - time.time())
    timer_placeholder = st.empty()
    while remaining > 0:
        timer_placeholder.warning(f"⏳ Too many failed attempts. Please wait {remaining} seconds...")
        time.sleep(1)
        remaining = int(st.session_state.lockout_time - time.time())
    st.session_state.failed_attempts = 0
    st.session_state.lockout_time = 0
    timer_placeholder.success("✅ You can now try again!")
    st.stop()

st.title("🔒 Secure Data Encryption System")

menu = ["Register", "Login", "Encrypt/Decrypt"]
choice = st.sidebar.selectbox("Menu", menu)

if choice == "Register":
    st.subheader("Create an Account")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Register"):
        if username in users:
            st.warning("⚠️ Username already exists!")
        else:
            users[username] = hash_password(password)
            save_users(users)
            st.success("✅ Registration successful! 🎉 You can now log in.")

elif choice == "Login":
    st.subheader("Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if username in users and users[username] == hash_password(password):
            st.session_state.logged_in = True
            st.session_state.username = username
            st.session_state.failed_attempts = 0
            st.success(f"✅ Login successful! Welcome, {username}! 🎉")
        else:
            st.error("❌ Invalid username or password.")

elif choice == "Encrypt/Decrypt":
    if not st.session_state.logged_in:
        st.warning("⚠️ Please log in first to access encryption and decryption.")
    else:
        st.subheader(f"Encrypt/Decrypt - User: {st.session_state.username}")
        action = st.radio("Action", ["Encrypt Data", "Decrypt Data", "View All", "Search by Title"])

        username = st.session_state.username

        if username not in stored_data:
            stored_data[username] = {}

        if action == "Encrypt Data":
            title = st.text_input("Enter a Title for Data")
            user_data = st.text_area("Enter Data to Encrypt")
            passkey = st.text_input("Enter Passkey", type="password")

            if st.button("Encrypt"):
                if title and user_data and passkey:
                    encrypted_text = encrypt_data(user_data, passkey)
                    stored_data[username][title] = {
                        'encrypted': encrypted_text,
                        'passkey': passkey
                    }
                    save_data(stored_data)
                    st.success("✅ Data encrypted successfully! 🎉")
                    st.write(f"🔐 **Encrypted Data Saved with Title:** `{title}`")
                else:
                    st.warning("⚠️ Please provide title, data, and passkey.")

        elif action == "Decrypt Data":
            if stored_data[username]:
                title = st.selectbox("Select Title to Decrypt", list(stored_data[username].keys()))
                passkey_input = st.text_input("Enter Passkey", type="password")

                if st.button("Decrypt"):
                    entry = stored_data[username][title]
                    encrypted_input = entry['encrypted']
                    correct_passkey = entry['passkey']
                    if passkey_input == correct_passkey:
                        try:
                            decrypted_text = decrypt_data(encrypted_input, passkey_input)
                            st.success("✅ Data decrypted successfully! 🎉")
                            st.write(f"🔓 **Decrypted Data:** `{decrypted_text}`")
                            st.session_state.failed_attempts = 0
                        except Exception as e:
                            st.session_state.failed_attempts += 1
                            st.error(f"❌ Failed to decrypt: {str(e)}")
                    else:
                        st.session_state.failed_attempts += 1
                        st.error(f"❌ Incorrect passkey. Attempt {st.session_state.failed_attempts}/3")
                        if st.session_state.failed_attempts >= 3:
                            st.session_state.lockout_time = time.time() + 10

            else:
                st.warning("⚠️ No encrypted data available. Please encrypt something first!")

        elif action == "View All":
            st.info("🔑 Enter correct passkey to view each item.")
            for title, entry in stored_data[username].items():
                st.write(f"**Title:** {title}")
                passkey_input = st.text_input(f"Enter Passkey for `{title}`", type="password", key=title)
                if st.button(f"Decrypt `{title}`", key=f"btn_{title}"):
                    correct_passkey = entry['passkey']
                    if passkey_input == correct_passkey:
                        try:
                            decrypted_text = decrypt_data(entry['encrypted'], passkey_input)
                            st.success(f"✅ `{title}`: {decrypted_text}")
                            st.session_state.failed_attempts = 0
                        except Exception as e:
                            st.session_state.failed_attempts += 1
                            st.error(f"❌ Failed to decrypt `{title}`: {str(e)}")
                    else:
                        st.session_state.failed_attempts += 1
                        st.error(f"❌ Incorrect passkey for `{title}`. Attempt {st.session_state.failed_attempts}/3")
                        if st.session_state.failed_attempts >= 3:
                            st.session_state.lockout_time = time.time() + 10

        elif action == "Search by Title":
            search_title = st.text_input("Enter Title to Search")
            passkey_input = st.text_input("Enter Passkey", type="password")
            if st.button("Search"):
                if search_title in stored_data[username]:
                    entry = stored_data[username][search_title]
                    correct_passkey = entry['passkey']
                    if passkey_input == correct_passkey:
                        try:
                            decrypted_text = decrypt_data(entry['encrypted'], passkey_input)
                            st.success(f"✅ Found Data: {decrypted_text}")
                            st.session_state.failed_attempts = 0
                        except Exception as e:
                            st.session_state.failed_attempts += 1
                            st.error(f"❌ Failed to decrypt: {str(e)}")
                    else:
                        st.session_state.failed_attempts += 1
                        st.error(f"❌ Incorrect passkey. Attempt {st.session_state.failed_attempts}/3")
                        if st.session_state.failed_attempts >= 3:
                            st.session_state.lockout_time = time.time() + 10
                else:
                    st.warning(f"⚠️ No data found with the title `{search_title}`.")
