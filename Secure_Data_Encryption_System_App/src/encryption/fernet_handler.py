# from cryptography.fernet import Fernet
# from encryption.key_generator import generate_key

# import base64
# import hashlib

# def generate_key_from_passkey(passkey: str) -> bytes:
#     # Create a SHA-256 hash of the passkey and take the first 32 bytes
#     key = hashlib.pbkdf2_hmac('sha256', passkey.encode(), b'salt_', 100000, dklen=32)
#     return base64.urlsafe_b64encode(key)

# def get_cipher(passkey: str) -> Fernet:
#     key = generate_key_from_passkey(passkey)
#     return Fernet(key)

# def encrypt_data(data: str, passkey: str) -> str:
#     key = generate_key(passkey)
#     fernet = Fernet(key)
#     encrypted = fernet.encrypt(data.encode())
#     return encrypted.decode()  # ✅ Convert bytes → string

# def decrypt_data(token: bytes, passkey: str) -> str:
#     cipher = get_cipher(passkey)
#     return cipher.decrypt(token).decode()

# ---------------------------------------------------------------------------------------------------------------------------
# from cryptography.fernet import Fernet
# import base64
# import hashlib

# def generate_key_from_passkey(passkey: str) -> bytes:
#     key = hashlib.pbkdf2_hmac('sha256', passkey.encode(), b'salt_', 100000, dklen=32)
#     return base64.urlsafe_b64encode(key)

# def get_cipher(passkey: str) -> Fernet:
#     key = generate_key_from_passkey(passkey)
#     return Fernet(key)

# def encrypt_data(data: str, passkey: str) -> str:
#     cipher = get_cipher(passkey)
#     encrypted = cipher.encrypt(data.encode())
#     return encrypted.decode()

# def decrypt_data(token: str, passkey: str) -> str:
#     cipher = get_cipher(passkey)
#     decrypted = cipher.decrypt(token.encode())
#     return decrypted.decode()
import base64
import hashlib
from cryptography.fernet import Fernet

def generate_key_from_passkey(passkey: str) -> bytes:
    key = hashlib.pbkdf2_hmac('sha256', passkey.encode(), b'salt_', 100000, dklen=32)
    return base64.urlsafe_b64encode(key)

def get_cipher(passkey: str) -> Fernet:
    key = generate_key_from_passkey(passkey)
    return Fernet(key)

def encrypt_data(data: str, passkey: str) -> str:
    cipher = get_cipher(passkey)
    encrypted = cipher.encrypt(data.encode())
    return encrypted.decode()  # Store as string

def decrypt_data(encrypted_data: str, passkey: str) -> str:
    cipher = get_cipher(passkey)
    decrypted = cipher.decrypt(encrypted_data.encode())
    return decrypted.decode()
