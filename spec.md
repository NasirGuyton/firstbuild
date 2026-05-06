# Specification: Task Tracker CLI

## Overview

The Task Tracker CLI is a small Python command-line application that lets users add tasks, list tasks, complete tasks, and persist task data in a JSON file.

## Out of Scope

- No web server
- No database
- No login system
- No due dates or categories
- No external APIs

## V1.0 - MVP Requirements

The app must support:

1. Adding a task with a non-empty title.
2. Listing all saved tasks.
3. Completing a task by ID.
4. Saving tasks to a JSON file.
5. Loading tasks from a JSON file.

## V1.1 - Refinements

The app must handle:

1. Empty task titles.
2. Missing task files.
3. Completing a task ID that does not exist.
4. Multiple tasks with unique IDs.

## V1.2 - Polish

The app must include:

1. Clear CLI messages.
2. Tests for main behavior and edge cases.
3. Documentation of workflow choices in the README.

## Quality Gates

### Gate 1: Unit Tests

Invocation:

python -m pytest tests/

Success criteria:

- Exit code is 0.
- All tests pass.
- No test writes to a real user task file.

Failure response:

- Fix the failing behavior.
- Re-run the gate before continuing.

### Gate 2: Manual Add and List Check

Invocation:

python src/task_tracker.py --file demo_tasks.json add "Finish homework"
python src/task_tracker.py --file demo_tasks.json list

Success criteria:

- The add command confirms the task was added.
- The list command shows the task title.
- The task appears as incomplete.

Failure response:

- Fix the CLI or storage behavior.
- Re-run the gate before continuing.

### Gate 3: Manual Complete Check

Invocation:

python src/task_tracker.py --file demo_tasks.json complete 1
python src/task_tracker.py --file demo_tasks.json list

Success criteria:

- The complete command confirms the task was completed.
- The list command shows the task as complete.

Failure response:

- Fix the complete behavior.
- Re-run the gate before continuing.

## Acceptance Criteria

### Add Task

Given an empty task list,
When the user adds a task titled "Finish homework",
Then the task list should contain one task with that title.

### Unique IDs

Given a task list with one existing task,
When the user adds another task,
Then the second task should have a different ID from the first task.

### List Tasks

Given a task list with saved tasks,
When the user lists tasks,
Then the output should show each task's ID, status, and title.

### Complete Task

Given a task list with an incomplete task,
When the user completes that task by ID,
Then the task should be marked as complete.

### Empty Title Edge Case

Given a user tries to add a task with an empty title,
When the add task function runs,
Then the program should reject the task and raise a ValueError.

### Missing Task ID Edge Case

Given a task list that does not contain task ID 99,
When the user tries to complete task ID 99,
Then the program should raise a ValueError.

### Missing File Edge Case

Given the storage file does not exist,
When the program loads tasks,
Then it should return an empty task list instead of crashing.