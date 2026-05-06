import argparse
import json
from pathlib import Path


DEFAULT_TASK_FILE = Path("tasks.json")


def load_tasks(task_file):
    """Load tasks from a JSON file.

    If the file does not exist, return an empty list.
    """
    task_file = Path(task_file)

    if not task_file.exists():
        return []

    with task_file.open("r", encoding="utf-8") as file:
        return json.load(file)


def save_tasks(task_file, tasks):
    """Save tasks to a JSON file."""
    task_file = Path(task_file)

    with task_file.open("w", encoding="utf-8") as file:
        json.dump(tasks, file, indent=2)


def get_next_id(tasks):
    """Return the next available task ID."""
    if not tasks:
        return 1

    highest_id = max(task["id"] for task in tasks)
    return highest_id + 1


def add_task(tasks, title):
    """Add a new task to the task list."""
    cleaned_title = title.strip()

    if not cleaned_title:
        raise ValueError("Task title cannot be empty")

    new_task = {
        "id": get_next_id(tasks),
        "title": cleaned_title,
        "completed": False,
    }

    return tasks + [new_task]


def complete_task(tasks, task_id):
    """Mark a task as complete by ID."""
    found_task = False
    updated_tasks = []

    for task in tasks:
        if task["id"] == task_id:
            updated_task = {
                **task,
                "completed": True,
            }
            updated_tasks.append(updated_task)
            found_task = True
        else:
            updated_tasks.append(task)

    if not found_task:
        raise ValueError(f"No task found with ID {task_id}")

    return updated_tasks


def format_tasks(tasks):
    """Format tasks for CLI display."""
    if not tasks:
        return "No tasks found."

    lines = []

    for task in tasks:
        status = "[x]" if task["completed"] else "[ ]"
        lines.append(f"{status} {task['id']}: {task['title']}")

    return "\n".join(lines)


def handle_add(args):
    tasks = load_tasks(args.file)
    updated_tasks = add_task(tasks, args.title)
    save_tasks(args.file, updated_tasks)

    added_task = updated_tasks[-1]
    print(f"Added task {added_task['id']}: {added_task['title']}")


def handle_list(args):
    tasks = load_tasks(args.file)
    print(format_tasks(tasks))


def handle_complete(args):
    tasks = load_tasks(args.file)
    updated_tasks = complete_task(tasks, args.task_id)
    save_tasks(args.file, updated_tasks)

    print(f"Completed task {args.task_id}")


def build_parser():
    parser = argparse.ArgumentParser(
        description="A simple CLI task tracker."
    )

    parser.add_argument(
        "--file",
        default=DEFAULT_TASK_FILE,
        help="Path to the JSON file used to store tasks.",
    )

    subparsers = parser.add_subparsers(
        dest="command",
        required=True,
    )

    add_parser = subparsers.add_parser("add", help="Add a new task.")
    add_parser.add_argument("title", help="Title of the task.")
    add_parser.set_defaults(func=handle_add)

    list_parser = subparsers.add_parser("list", help="List all tasks.")
    list_parser.set_defaults(func=handle_list)

    complete_parser = subparsers.add_parser(
        "complete",
        help="Mark a task as complete.",
    )
    complete_parser.add_argument(
        "task_id",
        type=int,
        help="ID of the task to complete.",
    )
    complete_parser.set_defaults(func=handle_complete)

    return parser


def main():
    parser = build_parser()
    args = parser.parse_args()

    try:
        args.func(args)
    except ValueError as error:
        print(f"Error: {error}")
        raise SystemExit(1)


if __name__ == "__main__":
    main()