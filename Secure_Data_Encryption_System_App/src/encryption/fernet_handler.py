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
