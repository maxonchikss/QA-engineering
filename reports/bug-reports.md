# Bug Reports

## BUG-01: Gradebook - ZeroDivisionError on Empty Grades

**Severity:** Critical  
**Component:** `src/gradebook.py::get_student_average()`  
**Status:** Fixed

**Description:**  
The `get_student_average()` method raises `ZeroDivisionError` when called for a student who has no grades yet.

**Steps to Reproduce:**
1. Create a Gradebook instance
2. Add a student: `gb.add_student("Peter")`
3. Call `gb.get_student_average("Peter")` without adding any grades

**Expected Result:**  
Method should return `0.0`

**Actual Result:**  
`ZeroDivisionError: division by zero`

**Root Cause:**  
Missing check for empty grades list before calculating `sum(grades) / len(grades)`

**Fix Applied:**  
Added conditional check: `if not grades: return 0.0`

---

## BUG-02: BankAccount - Transfer Atomicity Violation

**Severity:** Critical  
**Component:** `src/bank_account.py::transfer()`  
**Status:** Fixed

**Description:**  
The `transfer()` method credits the target account but does not debit the sender's account, effectively creating money out of thin air.

**Steps to Reproduce:**
1. Create two accounts: Alice (1000.0) and Bob (500.0)
2. Call `alice.transfer(300.0, bob)`
3. Check both balances

**Expected Result:**  
Alice: 700.0, Bob: 800.0

**Actual Result:**  
Alice: 1000.0, Bob: 800.0

**Root Cause:**  
Missing `self.balance -= amount` operation in the transfer method

**Fix Applied:**  
Added debit operation before crediting target account

---

## BUG-03: Library - Return Unborrowed Book

**Severity:** Major  
**Component:** `src/library.py::return_book()`  
**Status:** Fixed

**Description:**  
The `return_book()` method allows returning any book, even if it was never borrowed, leading to data duplication.

**Steps to Reproduce:**
1. Add a book to library
2. Call `return_book()` for a book that was never borrowed
3. Check total book count

**Expected Result:**  
Raise `ValueError` or maintain correct count

**Actual Result:**  
Book is duplicated in `available_books`, total count increases incorrectly

**Root Cause:**  
Missing validation that book exists in `borrowed_books` list before returning

**Fix Applied:**  
Added strict validation with `ValueError` if book not in borrowed list

---

## BUG-04: TaskManager - Clear Completed Skips Consecutive Tasks

**Severity:** Major  
**Component:** `src/task_manager.py::clear_completed()`  
**Status:** Fixed

**Description:**  
The `clear_completed()` method fails to remove all completed tasks when they appear consecutively in the list.

**Steps to Reproduce:**
1. Add 3 tasks
2. Complete tasks 1 and 2
3. Call `clear_completed()`
4. Check remaining task count

**Expected Result:**  
1 task remaining

**Actual Result:**  
2 tasks remaining (one completed task was skipped)

**Root Cause:**  
Removing elements from a list while iterating over it causes index shifting, leading to skipped elements

**Fix Applied:**  
Replaced iteration with removal by list comprehension: `self.tasks = [t for t in self.tasks if not t["completed"]]`