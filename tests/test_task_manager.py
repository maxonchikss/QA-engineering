import pytest
from src.task_manager import TaskManager


def test_add_task():
    tm = TaskManager()
    tm.add_task("Buy groceries")
    assert tm.get_total_tasks_count() == 1


def test_add_empty_task():
    tm = TaskManager()
    with pytest.raises(ValueError):
        tm.add_task("   ")


def test_complete_task():
    tm = TaskManager()
    tm.add_task("Buy groceries")
    tm.complete_task("Buy groceries")
    completed = tm.get_completed_tasks()
    assert len(completed) == 1
    assert completed[0]["title"] == "Buy groceries"
    assert completed[0]["completed"] is True


def test_complete_nonexistent_task():
    tm = TaskManager()
    with pytest.raises(KeyError):
        tm.complete_task("Nonexistent")


def test_get_pending_tasks():
    tm = TaskManager()
    tm.add_task("Task 1")
    tm.add_task("Task 2")
    tm.complete_task("Task 1")
    pending = tm.get_pending_tasks()
    assert len(pending) == 1
    assert pending[0]["title"] == "Task 2"
    assert pending[0]["completed"] is False


def test_clear_completed():
    tm = TaskManager()
    tm.add_task("Task 1")
    tm.add_task("Task 2")
    tm.add_task("Task 3")
    tm.complete_task("Task 1")
    tm.complete_task("Task 2")
    tm.clear_completed()
    assert tm.get_total_tasks_count() == 1
    assert tm.get_pending_tasks()[0]["title"] == "Task 3"


def test_clear_completed_consecutive():
    tm = TaskManager()
    tm.add_task("Task 1")
    tm.add_task("Task 2")
    tm.add_task("Task 3")
    tm.complete_task("Task 1")
    tm.complete_task("Task 2")
    tm.clear_completed()
    assert tm.get_total_tasks_count() == 1
