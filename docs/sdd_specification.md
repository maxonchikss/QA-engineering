# Specification by Example: File Encryptor

## Overview
This document contains concrete examples that define the expected behavior of the File Encryptor system. These examples serve as both requirements specification and automated test cases.

## Example 1: Basic Encryption with Original File Deletion

| Input Parameter | Value |
|---|---|
| Input file content | "Simple text" |
| Delete original | True |
| Expected: original exists | False |
| Expected: encrypted file exists | True |
| Expected: decrypted content | "Simple text" |

## Example 2: Encryption with Original File Preservation

| Input Parameter | Value |
|---|---|
| Input file content | "Another text" |
| Delete original | False |
| Expected: original exists | True |
| Expected: encrypted file exists | True |
| Expected: decrypted content | "Another text" |

## Example 3: Binary Content Handling

| Input Parameter | Value |
|---|---|
| Input file content | Binary data (\x00\x01\x02) |
| Delete original | True |
| Expected: original exists | False |
| Expected: encrypted file exists | True |
| Expected: decrypted content | Binary data (\x00\x01\x02) |

## Example 4: Unicode Content Handling

| Input Parameter | Value |
|---|---|
| Input file content | "Привет мир" (Cyrillic) |
| Delete original | False |
| Expected: original exists | True |
| Expected: encrypted file exists | True |
| Expected: decrypted content | "Привет мир" |

## Example 5: Empty File Handling

| Input Parameter | Value |
|---|---|
| Input file content | "" (empty) |
| Delete original | True |
| Expected: original exists | False |
| Expected: encrypted file exists | True |
| Expected: decrypted content | "" (empty) |

## Example 6: Various File Sizes

| File Size | Expected Behavior |
|---|---|
| 1 byte | Successfully encrypted and decrypted |
| 100 bytes | Successfully encrypted and decrypted |
| 1 KB | Successfully encrypted and decrypted |
| 10 KB | Successfully encrypted and decrypted |
| 100 KB | Successfully encrypted and decrypted |

## Example 7: Various Filename Formats

| Filename | Expected Behavior |
|---|---|
| simple.txt | Successfully processed |
| with spaces.txt | Successfully processed |
| with-dashes.txt | Successfully processed |
| with_underscores.txt | Successfully processed |
| file.with.multiple.dots.txt | Successfully processed |

## Security Requirements (Examples)

| Scenario | Expected Behavior |
|---|---|
| Encrypted file inspection | Original plaintext is not readable |
| Decryption with wrong key | ValueError raised |
| Missing input file | FileNotFoundError raised |