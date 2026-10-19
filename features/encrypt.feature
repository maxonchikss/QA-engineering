Feature: File Encryption and Decryption
  As a security-conscious user
  I want to encrypt and decrypt files with various edge cases
  So that I can protect sensitive data under any circumstances

  Scenario: Successful encryption and decryption roundtrip
    Given a file named "secret.txt" exists with content "My secret message"
    When I encrypt the file to "secret.enc"
    And I decrypt "secret.enc" to "secret_restored.txt"
    Then the file "secret_restored.txt" should contain "My secret message"

  Scenario: Original file is deleted after encryption when requested
    Given a file named "sensitive.txt" exists with content "Top secret data"
    When I encrypt the file to "sensitive.enc" with deletion
    Then the file "sensitive.txt" should not exist
    And the file "sensitive.enc" should exist

  Scenario: Decryption fails with wrong key
    Given a file named "locked.txt" exists with content "Protected content"
    And I encrypt "locked.txt" to "locked.enc" with key A
    When I try to decrypt "locked.enc" with key B
    Then a decryption error should be raised

  Scenario: Empty file encryption and decryption
    Given a file named "empty.txt" exists with empty content
    When I encrypt the file to "empty.enc"
    And I decrypt "empty.enc" to "empty_restored.txt"
    Then the file "empty_restored.txt" should contain empty content
    And the file "empty.enc" should exist

  Scenario: File with Unicode content including emoji and CJK characters
    Given a file named "unicode.txt" exists with content "Hello world"
    When I encrypt the file to "unicode.enc"
    And I decrypt "unicode.enc" to "unicode_restored.txt"
    Then the file "unicode_restored.txt" should contain "Hello world"