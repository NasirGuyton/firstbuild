# Firstbuild: Task Tracker CLI

A small Python command-line task tracker built with a test-first AI workflow.

## Project Overview

This app lets a user manage a simple task list from the terminal. Users can add tasks, list saved tasks, and mark tasks as complete. Tasks are stored in a local JSON file so the data persists between runs.

## Features

- Add a task
- List all tasks
- Complete a task by ID
- Save and load tasks from JSON
- Handle edge cases like empty task names and missing task IDs

## Tech Stack

- Python 3
- pytest
- JSON file storage
- argparse for CLI commands

## Install

pip install -r requirements.txt

## Run Tests

python -m pytest tests/

## CLI Usage

Add a task:

python src/task_tracker.py add "Finish homework"

List tasks:

python src/task_tracker.py list

Complete a task:

python src/task_tracker.py complete 1

Use a custom storage file:

python src/task_tracker.py --file my_tasks.json add "Study Python"

## Workflow Documentation

### Single-file, multi-step task

The first complexity task was building the core task logic in `src/task_tracker.py`. This was mostly contained in one file but required multiple steps: creating task objects, assigning IDs, validating input, and saving to JSON.

Approach used:

1. Write tests for expected behavior first.
2. Run tests and confirm they fail.
3. Implement the minimum code needed.
4. Run tests again.
5. Refactor while keeping tests green.

### Multi-file task with design decisions

The second complexity task connected the CLI interface, storage behavior, and tests. This required decisions about how commands should work, how the JSON file should be passed in, and how tests should avoid touching the real user's files.

Approach used:

1. Keep pure logic functions testable.
2. Use temporary files in tests.
3. Keep CLI behavior separate from storage functions.
4. Verify everything with `python -m pytest tests/`.

## AI Usage

I used ChatGPT as my AI development assistant. I used it to help plan the project, write the specification, create tests, implement the CLI, and check whether the project satisfied the Firstbuild requirements.

## Final Verification

All tests should pass with:

python -m pytest tests/