# Project Instructions for AI Assistant

## Project

This repo is a Firstbuild assignment. The application is a Python CLI task tracker.

## Tech Stack

- Python 3
- pytest for testing
- argparse for CLI commands
- JSON for local persistence

## File Boundaries

- Application code belongs in `src/task_tracker.py`.
- Tests belong in `tests/test_task_tracker.py`.
- Do not add a database, web framework, authentication, or external API.
- Keep the project small and focused.

## Coding Conventions

- Write clear, beginner-readable Python.
- Prefer small functions with descriptive names.
- Avoid unnecessary dependencies.
- Keep business logic testable without needing the CLI.

## Testing Expectations

- Tests must be written before implementation when adding features.
- Run all tests with:

```bash
python -m pytest tests/