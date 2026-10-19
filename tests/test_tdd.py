import os
import pytest
from cryptography.fernet import Fernet
from src.file_encryptor import FileEncryptor


def test_encrypt_creates_output_file(tmp_path):
    encryptor = FileEncryptor()
    input_file = tmp_path / "input.txt"
    output_file = tmp_path / "output.enc"
    input_file.write_text("Hello, World!", encoding="utf-8")
    encryptor.encrypt_file(str(input_file), str(output_file))
    assert output_file.exists()


def test_decrypt_restores_original_content(tmp_path):
    encryptor = FileEncryptor()
    input_file = tmp_path / "input.txt"
    encrypted_file = tmp_path / "encrypted.enc"
    decrypted_file = tmp_path / "decrypted.txt"
    input_file.write_text("Secret message", encoding="utf-8")
    encryptor.encrypt_file(str(input_file), str(encrypted_file))
    encryptor.decrypt_file(str(encrypted_file), str(decrypted_file))
    assert decrypted_file.read_text(encoding="utf-8") == "Secret message"


def test_encrypt_with_delete_original(tmp_path):
    encryptor = FileEncryptor()
    input_file = tmp_path / "input.txt"
    output_file = tmp_path / "output.enc"
    input_file.write_text("Delete me", encoding="utf-8")
    encryptor.encrypt_file(str(input_file), str(output_file), delete_original=True)
    assert not input_file.exists()
    assert output_file.exists()


def test_encrypt_nonexistent_file_raises_error(tmp_path):
    encryptor = FileEncryptor()
    with pytest.raises(FileNotFoundError):
        encryptor.encrypt_file(
            str(tmp_path / "missing.txt"), str(tmp_path / "out.enc")
        )


def test_decrypt_with_wrong_key_raises_error(tmp_path):
    encryptor1 = FileEncryptor()
    encryptor2 = FileEncryptor()
    input_file = tmp_path / "input.txt"
    encrypted_file = tmp_path / "encrypted.enc"
    input_file.write_text("Secret", encoding="utf-8")
    encryptor1.encrypt_file(str(input_file), str(encrypted_file))
    with pytest.raises(ValueError):
        encryptor2.decrypt_file(str(encrypted_file), str(tmp_path / "out.txt"))


def test_save_and_load_key(tmp_path):
    encryptor1 = FileEncryptor()
    key_file = tmp_path / "key.key"
    encryptor1.save_key(str(key_file))
    encryptor2 = FileEncryptor()
    encryptor2.load_key(str(key_file))
    assert encryptor1.key == encryptor2.key


def test_encrypted_content_differs_from_original(tmp_path):
    encryptor = FileEncryptor()
    input_file = tmp_path / "input.txt"
    encrypted_file = tmp_path / "encrypted.enc"
    input_file.write_text("Readable text", encoding="utf-8")
    encryptor.encrypt_file(str(input_file), str(encrypted_file))
    original_bytes = input_file.read_bytes()
    encrypted_bytes = encrypted_file.read_bytes()
    assert original_bytes != encrypted_bytes
