import pytest
from src.gradebook import Gradebook


def test_add_student():
    gb = Gradebook()
    gb.add_student("Alice")
    assert "Alice" in gb.students


def test_add_duplicate_student():
    gb = Gradebook()
    gb.add_student("Alice")
    with pytest.raises(ValueError):
        gb.add_student("Alice")


def test_add_grade():
    gb = Gradebook()
    gb.add_student("Alice")
    gb.add_grade("Alice", 5)
    assert 5 in gb.students["Alice"]


def test_add_invalid_grade():
    gb = Gradebook()
    gb.add_student("Alice")
    with pytest.raises(ValueError):
        gb.add_grade("Alice", 6)


def test_get_student_average():
    gb = Gradebook()
    gb.add_student("Alice")
    gb.add_grade("Alice", 5)
    gb.add_grade("Alice", 4)
    assert gb.get_student_average("Alice") == 4.5


def test_get_student_average_no_grades():
    gb = Gradebook()
    gb.add_student("Alice")
    assert gb.get_student_average("Alice") == 0.0


def test_get_excellent_students():
    gb = Gradebook()
    gb.add_student("Alice")
    gb.add_student("Bob")
    gb.add_grade("Alice", 5)
    gb.add_grade("Alice", 5)
    gb.add_grade("Bob", 3)
    excellent = gb.get_excellent_students()
    assert "Alice" in excellent
    assert "Bob" not in excellent


def test_remove_student():
    gb = Gradebook()
    gb.add_student("Alice")
    gb.remove_student("Alice")
    assert "Alice" not in gb.students
