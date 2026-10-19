import os
from behave import given, when, then, step
from cryptography.fernet import Fernet, InvalidToken
from src.file_encryptor import FileEncryptor


@given('a file named "{filename}" exists with content "{content}"')
def step_create_file_with_content(context, filename, content):
    context.work_dir = os.path.join(os.getcwd(), "bdd_temp")
    os.makedirs(context.work_dir, exist_ok=True)
    context.file_path = os.path.join(context.work_dir, filename)
    with open(context.file_path, "w", encoding="utf-8") as f:
        f.write(content)
    context.encryptor = FileEncryptor()


@given('a file named "{filename}" exists with empty content')
def step_create_empty_file(context, filename):
    context.work_dir = os.path.join(os.getcwd(), "bdd_temp")
    os.makedirs(context.work_dir, exist_ok=True)
    context.file_path = os.path.join(context.work_dir, filename)
    with open(context.file_path, "w", encoding="utf-8") as f:
        f.write("")
    context.encryptor = FileEncryptor()


@step('I encrypt "{filename}" to "{enc_filename}" with key A')
def step_encrypt_with_key_a(context, filename, enc_filename):
    context.encryptor_a = FileEncryptor()
    context.key_a = context.encryptor_a.key
    input_path = os.path.join(context.work_dir, filename)
    output_path = os.path.join(context.work_dir, enc_filename)
    context.encryptor_a.encrypt_file(input_path, output_path)


@when('I encrypt the file to "{enc_filename}"')
def step_encrypt_file(context, enc_filename):
    context.enc_path = os.path.join(context.work_dir, enc_filename)
    context.encryptor.encrypt_file(context.file_path, context.enc_path)


@when('I encrypt the file to "{enc_filename}" with deletion')
def step_encrypt_with_deletion(context, enc_filename):
    context.enc_path = os.path.join(context.work_dir, enc_filename)
    context.encryptor.encrypt_file(
        context.file_path, context.enc_path, delete_original=True
    )


@when('I encrypt the file to "{enc_filename}" without deletion')
def step_encrypt_without_deletion(context, enc_filename):
    context.enc_path = os.path.join(context.work_dir, enc_filename)
    context.encryptor.encrypt_file(
        context.file_path, context.enc_path, delete_original=False
    )


@when('I decrypt "{enc_filename}" to "{dec_filename}"')
def step_decrypt_file(context, enc_filename, dec_filename):
    enc_path = os.path.join(context.work_dir, enc_filename)
    context.dec_path = os.path.join(context.work_dir, dec_filename)
    context.encryptor.decrypt_file(enc_path, context.dec_path)


@when('I try to decrypt "{enc_filename}" with key B')
def step_decrypt_with_wrong_key(context, enc_filename):
    enc_path = os.path.join(context.work_dir, enc_filename)
    context.wrong_encryptor = FileEncryptor()
    context.decryption_error = None
    try:
        context.wrong_encryptor.decrypt_file(
            enc_path, os.path.join(context.work_dir, "wrong_dec.txt")
        )
    except ValueError as e:
        context.decryption_error = e


@then('the file "{filename}" should contain "{content}"')
def step_file_contains(context, filename, content):
    file_path = os.path.join(context.work_dir, filename)
    with open(file_path, "r", encoding="utf-8") as f:
        assert f.read() == content


@then('the file "{filename}" should contain empty content')
def step_file_contains_empty(context, filename):
    file_path = os.path.join(context.work_dir, filename)
    with open(file_path, "r", encoding="utf-8") as f:
        assert f.read() == ""


@then('the file "{filename}" should not exist')
def step_file_not_exists(context, filename):
    file_path = os.path.join(context.work_dir, filename)
    assert not os.path.exists(file_path)


@then('the file "{filename}" should exist')
def step_file_exists(context, filename):
    file_path = os.path.join(context.work_dir, filename)
    assert os.path.exists(file_path)


@then('a decryption error should be raised')
def step_decryption_error_raised(context):
    assert context.decryption_error is not None


@then('the encrypted file should not contain "{content}"')
def step_encrypted_not_contains(context, content):
    with open(context.enc_path, "rb") as f:
        encrypted_bytes = f.read()
    assert content.encode("utf-8") not in encrypted_bytes


@then('the file "{filename1}" should have identical binary content to "{filename2}"')
def step_files_identical_binary(context, filename1, filename2):
    path1 = os.path.join(context.work_dir, filename1)
    path2 = os.path.join(context.work_dir, filename2)
    with open(path1, "rb") as f1, open(path2, "rb") as f2:
        assert f1.read() == f2.read()


@then('the file "{filename1}" should not have identical content to "{filename2}"')
def step_files_not_identical(context, filename1, filename2):
    path1 = os.path.join(context.work_dir, filename1)
    path2 = os.path.join(context.work_dir, filename2)
    with open(path1, "rb") as f1, open(path2, "rb") as f2:
        assert f1.read() != f2.read()
