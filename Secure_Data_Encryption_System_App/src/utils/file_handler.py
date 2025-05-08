# import json
# import os

# # Path to store the data
# DATA_FILE = "data.json"

# # Function to load data from the JSON file
# def load_data():
#     if os.path.exists(DATA_FILE):
#         with open(DATA_FILE, 'r') as file:
#             return json.load(file)
#     return {}

# # Function to save data to the JSON file
# import json

# def save_data(data, filename="data_store.json"):
#     def convert_keys_to_str(obj):
#         if isinstance(obj, dict):
#             return {k.decode() if isinstance(k, bytes) else k: convert_keys_to_str(v) for k, v in obj.items()}
#         elif isinstance(obj, list):
#             return [convert_keys_to_str(item) for item in obj]
#         return obj

#     data = convert_keys_to_str(data)  # Convert all keys to str
#     with open(filename, "w") as file:
#         json.dump(data, file, indent=4)
#         st.success("✅ Data saved successfully!")

# -------------------------------------------------------------------------------------------

# import json
# import os
# import hashlib

# DATA_FILE = 'src/data.json'
# USER_FILE = 'src/users.json'

# def load_data():
#     if not os.path.exists(DATA_FILE):
#         return {}
#     with open(DATA_FILE, 'r') as file:
#         try:
#             return json.load(file)
#         except json.JSONDecodeError:
#             return {}

# def save_data(data):
#     with open(DATA_FILE, 'w') as file:
#         json.dump(data, file, indent=4)

# def load_users():
#     if not os.path.exists(USER_FILE):
#         return {}
#     with open(USER_FILE, 'r') as file:
#         try:
#             return json.load(file)
#         except json.JSONDecodeError:
#             return {}

# def save_users(users):
#     with open(USER_FILE, 'w') as file:
#         json.dump(users, file, indent=4)

# def hash_password(password):
#     return hashlib.sha256(password.encode()).hexdigest()
import json
import os
import hashlib

DATA_FILE = 'data.json'

def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as file:
            try:
                data = json.load(file)
            except json.JSONDecodeError:
                data = {}
    else:
        data = {}
    # Ensure keys exist
    if 'users' not in data:
        data['users'] = {}
    if 'data' not in data:
        data['data'] = {}
    return data

def save_data(data):
    with open(DATA_FILE, 'w') as file:
        json.dump(data, file, indent=4)

def load_users():
    data = load_data()
    return data['users']

def save_users(users):
    data = load_data()
    data['users'] = users
    save_data(data)

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def add_user(username, password_hash):
    data = load_data()
    data['users'][username] = password_hash
    save_data(data)

def get_user_password_hash(username):
    data = load_data()
    return data['users'].get(username)

def add_encrypted_data(username, title, encrypted_data):
    data = load_data()
    if username not in data['data']:
        data['data'][username] = {}
    data['data'][username][title] = encrypted_data
    save_data(data)

def get_data_by_title(username, title):
    data = load_data()
    return data['data'].get(username, {}).get(title)
