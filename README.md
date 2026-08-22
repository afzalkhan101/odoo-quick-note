# Odoo Quick Note

A simple and fast note-taking module for Odoo that allows users to create quick notes, manage tasks, and set reminders without leaving their current screen.

## Requirements

### 1. Quick Popup Shortcut

* Press **`Ctrl + Q`** from anywhere in the Odoo backend.
* A **Quick Note popup** should open immediately.
* The popup should allow users to quickly enter and save information.
* The popup should be lightweight and easy to use.

### 2. Todo List Integration

The Quick Note popup should support creating todo/task items.

Users should be able to:

* Add a todo/task.
* Enter task-related **text or description**.
* Set a **reminder date and time** for the task.
* Save the task directly to the **Todo List module**.
* View and manage the created todo from the Todo List module.

### 3. Basic Workflow

```text
Ctrl + Q
   ↓
Quick Note Popup
   ↓
Enter Note / Task
   ↓
Choose:
   ├── Save as Quick Note
   └── Create Todo
          ↓
     Add Description
          ↓
     Set Reminder
          ↓
     Save
          ↓
     Todo List Module
```

## Main Features

* Global **Ctrl + Q** keyboard shortcut.
* Quick popup for creating notes.
* Create todo/task directly from the popup.
* Task description support.
* Reminder date and time.
* Integration with Odoo Todo functionality.
* Fast and user-friendly interface.
* No need to navigate away from the current Odoo screen.

## Future Enhancements

* Task priority.
* Tags/categories.
* Recurring reminders.
* Browser notifications.
* Activity integration.
* Search and filter notes.
* Pin important notes.
* Quick note history.
* Mobile-friendly interface.

## Compatibility

* Odoo 18.0
* Python 3.x
* PostgreSQL

## License

OPL-1
