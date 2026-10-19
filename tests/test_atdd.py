import os
import pytest
from src.file_encryptor import FileEncryptor


def test_acceptance_encrypted_file_is_inaccessible_without_key(tmp_path):
    encryptor = FileEncryptor()
    input_file = tmp_path / "document.txt"
    encrypted_file = tmp_path / "document.enc"
    input_file.write_text("Confidential data", encoding="utf-8")
    encryptor.encrypt_file(str(input_file), str(encrypted_file))
    encrypted_content = encrypted_file.read_bytes()
    assert b"Confidential data" not in encrypted_content


def test_acceptance_original_file_deleted_when_requested(tmp_path):
    encryptor = FileEncryptor()
    input_file = tmp_path / "sensitive.txt"
    encrypted_file = tmp_path / "sensitive.enc"
    input_file.write_text("Top secret", encoding="utf-8")
    encryptor.encrypt_file(str(input_file), str(encrypted_file), delete_original=True)
    assert not input_file.exists()


def test_acceptance_original_file_preserved_when_not_requested(tmp_path):
    encryptor = FileEncryptor()
    input_file = tmp_path / "important.txt"
    encrypted_file = tmp_path / "important.enc"
    input_file.write_text("Keep me", encoding="utf-8")
    encryptor.encrypt_file(str(input_file), str(encrypted_file), delete_original=False)
    assert input_file.exists()
    assert encrypted_file.exists()


def test_acceptance_full_roundtrip_preserves_data_integrity(tmp_path):
    encryptor = FileEncryptor()
    input_file = tmp_path / "data.txt"
    encrypted_file = tmp_path / "data.enc"
    decrypted_file = tmp_path / "data_restored.txt"
    original_content = "Full roundtrip test with special chars: !@#$%^&*()"
    input_file.write_text(original_content, encoding="utf-8")
    encryptor.encrypt_file(str(input_file), str(encrypted_file))
    encryptor.decrypt_file(str(encrypted_file), str(decrypted_file))
    assert decrypted_file.read_text(encoding="utf-8") == original_content


def test_acceptance_key_persistence_across_sessions(tmp_path):
    key_file = tmp_path / "persistent.key"
    encryptor1 = FileEncryptor()
    encryptor1.save_key(str(key_file))
    input_file = tmp_path / "data.txt"
    encrypted_file = tmp_path / "data.enc"
    input_file.write_text("Persistent key test", encoding="utf-8")
    encryptor1.encrypt_file(str(input_file), str(encrypted_file))
    encryptor2 = FileEncryptor()
    encryptor2.load_key(str(key_file))
    decrypted_file = tmp_path / "data_restored.txt"
    encryptor2.decrypt_file(str(encrypted_file), str(decrypted_file))
    assert decrypted_file.read_text(encoding="utf-8") == "Persistent key test"