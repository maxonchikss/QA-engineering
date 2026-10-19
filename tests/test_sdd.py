import os
import pytest
from src.file_encryptor import FileEncryptor


@pytest.mark.parametrize(
    "content,delete_original,expected_original_exists",
    [
        ("Simple text", True, False),
        ("Another text", False, True),
        ("Binary-like: \x00\x01\x02", True, False),
        ("Unicode: Привет мир", False, True),
        ("", True, False),
    ],
)
def test_sdd_encryption_scenarios(
    tmp_path, content, delete_original, expected_original_exists
):
    encryptor = FileEncryptor()
    input_file = tmp_path / "input.txt"
    encrypted_file = tmp_path / "encrypted.enc"
    decrypted_file = tmp_path / "decrypted.txt"
    input_file.write_text(content, encoding="utf-8")
    encryptor.encrypt_file(str(input_file), str(encrypted_file), delete_original)
    assert input_file.exists() == expected_original_exists
    assert encrypted_file.exists()
    encryptor.decrypt_file(str(encrypted_file), str(decrypted_file))
    assert decrypted_file.read_text(encoding="utf-8") == content


@pytest.mark.parametrize(
    "file_size_bytes",
    [1, 100, 1024, 10240, 102400],
)
def test_sdd_various_file_sizes(tmp_path, file_size_bytes):
    encryptor = FileEncryptor()
    input_file = tmp_path / "input.bin"
    encrypted_file = tmp_path / "encrypted.enc"
    decrypted_file = tmp_path / "decrypted.bin"
    input_file.write_bytes(os.urandom(file_size_bytes))
    original_bytes = input_file.read_bytes()
    encryptor.encrypt_file(str(input_file), str(encrypted_file))
    encryptor.decrypt_file(str(encrypted_file), str(decrypted_file))
    assert decrypted_file.read_bytes() == original_bytes


@pytest.mark.parametrize(
    "filename",
    [
        "simple.txt",
        "with spaces.txt",
        "with-dashes.txt",
        "with_underscores.txt",
        "file.with.multiple.dots.txt",
    ],
)
def test_sdd_various_filenames(tmp_path, filename):
    encryptor = FileEncryptor()
    input_file = tmp_path / filename
    encrypted_file = tmp_path / f"{filename}.enc"
    decrypted_file = tmp_path / f"restored_{filename}"
    input_file.write_text("Test content", encoding="utf-8")
    encryptor.encrypt_file(str(input_file), str(encrypted_file))
    encryptor.decrypt_file(str(encrypted_file), str(decrypted_file))
    assert decrypted_file.read_text(encoding="utf-8") == "Test content"
