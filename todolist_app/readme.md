# To-Do List CLI Application

A lightweight, object-oriented Command-Line Interface (CLI) To-Do List application built with Python. It supports full CRUD (Create, Read, Update, Delete) operations with automatic JSON data persistence.

---

## Features

- **Add Tasks (`at`)**: Quickly create new tasks.
- **Show Tasks (`st`)**: View all current tasks and their status.
- **Update Task (`ut`)**: Rename an existing task title.
- **Mark Done (`md`)**: Mark a task as completed.
- **Delete Task (`dt`)**: Remove a task from your list.
- **Auto Persistence**: Task state is automatically saved to JSON after every command.
- **Auto-Clearing UI**: Clears the console after every operation for a clean interface.

---

## Development Notes & AI Transparency

This project was designed and implemented using core Object-Oriented Programming (OOP) principles. Generative AI was integrated into the development workflow as a supportive coding assistant rather than a primary code generator.

### Justification for AI Usage

1. **Targeted Technical Debugging:**  
   AI was utilized to quickly diagnose low-level Python runtime issues—such as object vs. dictionary mutation traps (`to_dict()`) and in-place list modification bugs during iteration—reducing debugging overhead.

2. **Cross-Platform Executable Resolution:**  
   Building a standalone executable with PyInstaller introduces path resolution challenges (`sys.frozen` runtime paths vs. standard file paths). AI assisted in writing a robust `get_data_filepath()` function to guarantee reliable JSON data persistence regardless of execution environment.

3. **Syntactical & Structural Refinement:**  
   AI served as an immediate code reviewer to double-check pattern matching (`match-case`) syntax, optimal data structure operations, and documentation structure.

> **Summary:** The core architecture, domain logic, and CRUD design remain entirely human-driven. AI was applied strategically to accelerate problem-solving for specific edge cases, optimize pathing logic, and streamline project documentation.

---

## Project Structure

```text
todolist_app/
├── data/
│   └── taskdata.json       # JSON file where task state is persisted
├── src/
│   ├── managers/
│   │   ├── datamanager.py  # Handles loading and saving JSON data
│   │   └── task_manager.py # Handles task collection logic (CRUD)
│   ├── model/
│   │   └── task.py         # Task model definition
│   └── main.py             # CLI entry point and command handler
├── .gitignore
└── README.md