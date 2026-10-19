import pytest
from src.library import Library


def test_add_book():
    lib = Library()
    lib.add_book("Python Crash Course")
    assert lib.is_book_available("Python Crash Course")


def test_borrow_book():
    lib = Library()
    lib.add_book("Python Crash Course")
    lib.borrow_book("Python Crash Course")
    assert not lib.is_book_available("Python Crash Course")


def test_borrow_unavailable_book():
    lib = Library()
    with pytest.raises(ValueError):
        lib.borrow_book("Nonexistent Book")


def test_return_book():
    lib = Library()
    lib.add_book("Python Crash Course")
    lib.borrow_book("Python Crash Course")
    lib.return_book("Python Crash Course")
    assert lib.is_book_available("Python Crash Course")


def test_return_unborrowed_book():
    lib = Library()
    lib.add_book("Python Crash Course")
    with pytest.raises(ValueError):
        lib.return_book("Clean Code")


def test_get_total_books():
    lib = Library()
    lib.add_book("Book A")
    lib.add_book("Book B")
    lib.borrow_book("Book A")
    assert lib.get_total_books() == 2
