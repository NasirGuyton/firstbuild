import sys
from pathlib import Path

import pytest

sys.path.append(str(Path(__file__).resolve().parents[1] / "src"))

from task_tracker import (
    add_task,
    complete_task,
    format_tasks,
    load_tasks,
    save_tasks,
)


def test_load_tasks_returns_empty_list_when_file_does_not_exist(tmp_path):
    task_file = tmp_path / "missing_tasks.json"

    tasks = load_tasks(task_file)

    assert tasks == []


def test_save_and_load_tasks(tmp_path):
    task_file = tmp_path / "tasks.json"
    tasks = [
        {"id": 1, "title": "Finish homework", "completed": False}
    ]

    save_tasks(task_file, tasks)
    loaded_tasks = load_tasks(task_file)

    assert loaded_tasks == tasks


def test_add_task_creates_task_with_title_and_id():
    tasks = []

    updated_tasks = add_task(tasks, "Finish homework")

    assert len(updated_tasks) == 1
    assert updated_tasks[0]["id"] == 1
    assert updated_tasks[0]["title"] == "Finish homework"
    assert updated_tasks[0]["completed"] is False


def test_add_task_assigns_unique_ids():
    tasks = [
        {"id": 1, "title": "First task", "completed": False}
    ]

    updated_tasks = add_task(tasks, "Second task")

    assert updated_tasks[1]["id"] == 2
    assert updated_tasks[1]["title"] == "Second task"


def test_add_task_rejects_empty_title():
    tasks = []

    with pytest.raises(ValueError, match="Task title cannot be empty"):
        add_task(tasks, "   ")


def test_complete_task_marks_task_complete():
    tasks = [
        {"id": 1, "title": "Finish homework", "completed": False}
    ]

    updated_tasks = complete_task(tasks, 1)

    assert updated_tasks[0]["completed"] is True


def test_complete_task_rejects_missing_id():
    tasks = [
        {"id": 1, "title": "Finish homework", "completed": False}
    ]

    with pytest.raises(ValueError, match="No task found with ID 99"):
        complete_task(tasks, 99)


def test_format_tasks_shows_empty_message_for_no_tasks():
    output = format_tasks([])

    assert output == "No tasks found."


def test_format_tasks_shows_task_status_and_title():
    tasks = [
        {"id": 1, "title": "Finish homework", "completed": False},
        {"id": 2, "title": "Submit project", "completed": True},
    ]

    output = format_tasks(tasks)

    assert "[ ] 1: Finish homework" in output
    assert "[x] 2: Submit project" in output