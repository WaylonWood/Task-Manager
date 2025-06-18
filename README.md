# 🗂️ Task Manager CLI

A simple and beginner-friendly **Command Line Task Manager** written in Python.  
Manage tasks, due dates, priorities, and subtasks — all from your terminal.

---

## 🚀 Features

- ✅ Add tasks with due dates and priorities  
- 📋 View all pending tasks with color-coded due dates  
- 📌 Add nested subtasks under main tasks  
- ☑️ Mark tasks and subtasks as completed  
- 🗑️ Remove tasks or subtasks  
- 💾 Stores data in JSON for persistent storage  
- 🟢 View completed task history  
- 🎨 Color-coded output using `colorama`

---

## 🛠️ Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/your-username/task-manager.git
cd task-manager
```

---

### 2. Create a virtual environment  
_This is recommended to avoid system-wide package issues._

```bash
python3 -m venv .venv
source .venv/bin/activate  # For Mac/Linux
# OR
.venv\Scripts\activate     # For Windows
```

---

### 3. Install dependencies

```bash
pip install colorama
```

---

## ▶️ Usage

After activating the virtual environment, run the task manager:

```bash
python task-manager.py
```

You’ll see a menu like this:

```
 1. Add Task
 2. View Tasks
 3. Complete Task
 4. Remove Task
 5. Complete Subtask
 6. Remove Subtask
 7. View Completed Tasks
 8. Exit
```

---

## 📂 File Structure

```
task-manager/
├── task-manager.py
├── tasks.json
├── completed.json
├── .venv/               # Optional: virtual environment
├── README.md
└── LICENSE
```

> 💡 `tasks.json` and `completed.json` are created automatically when needed.

---

## 🤝 Contributing

Pull requests are welcome!  
If you have ideas for features or fixes, feel free to fork and submit a PR.

---

## 📄 License

This project is available under the [MIT License](LICENSE).
