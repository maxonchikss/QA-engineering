import os
from cryptography.fernet import Fernet, InvalidToken


class FileEncryptor:
    def __init__(self, key=None):
        self.key = key or Fernet.generate_key()
        self.cipher = Fernet(self.key)

    def encrypt_file(self, input_path, output_path, delete_original=False):
        if not os.path.exists(input_path):
            raise FileNotFoundError(f"Input file not found: {input_path}")
        with open(input_path, "rb") as file:
            data = file.read()
        encrypted_data = self.cipher.encrypt(data)
        with open(output_path, "wb") as file:
            file.write(encrypted_data)
        if delete_original:
            os.remove(input_path)

    def decrypt_file(self, input_path, output_path):
        if not os.path.exists(input_path):
            raise FileNotFoundError(f"Input file not found: {input_path}")
        with open(input_path, "rb") as file:
            encrypted_data = file.read()
        try:
            decrypted_data = self.cipher.decrypt(encrypted_data)
        except InvalidToken:
            raise ValueError("Decryption failed: invalid key or corrupted file")
        with open(output_path, "wb") as file:
            file.write(decrypted_data)

    def save_key(self, key_path):
        with open(key_path, "wb") as file:
            file.write(self.key)

    def load_key(self, key_path):
        with open(key_path, "rb") as file:
            self.key = file.read()
        self.cipher = Fernet(self.key)
