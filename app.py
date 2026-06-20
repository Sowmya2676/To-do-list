from flask import Flask, render_template, request, redirect
import json
import os

app = Flask(__name__)

FILE_NAME = "tasks.json"


def load_tasks():
    if os.path.exists(FILE_NAME):
        try:
            with open(FILE_NAME, "r") as file:
                tasks = json.load(file)

                for task in tasks:
                    task.setdefault("name", "")
                    task.setdefault("deadline", "")
                    task.setdefault("completed", False)

                return tasks

        except json.JSONDecodeError:
            return []

    return []


def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file, indent=4)


def get_next_due(tasks):
    pending = [
        task for task in tasks
        if not task["completed"] and task["deadline"]
    ]

    if not pending:
        return None

    pending.sort(key=lambda x: x["deadline"])

    return pending[0]


@app.route("/")
def home():
    tasks = load_tasks()

    total = len(tasks)
    completed = len([task for task in tasks if task["completed"]])
    pending = total - completed

    next_due = get_next_due(tasks)

    return render_template(
        "index.html",
        tasks=tasks,
        total=total,
        completed=completed,
        pending=pending,
        next_due=next_due
    )


@app.route("/add", methods=["POST"])
def add_task():
    task_name = request.form["task"]
    deadline = request.form["deadline"]

    tasks = load_tasks()

    tasks.append({
        "name": task_name,
        "deadline": deadline,
        "completed": False
    })

    save_tasks(tasks)

    return redirect("/")


@app.route("/complete/<int:index>")
def complete_task(index):
    tasks = load_tasks()

    if 0 <= index < len(tasks):
        tasks[index]["completed"] = True
        save_tasks(tasks)

    return redirect("/")


@app.route("/delete/<int:index>")
def delete_task(index):
    tasks = load_tasks()

    if 0 <= index < len(tasks):
        tasks.pop(index)
        save_tasks(tasks)

    return redirect("/")


@app.route("/update/<int:index>", methods=["POST"])
def update_task(index):
    tasks = load_tasks()

    if 0 <= index < len(tasks):
        tasks[index]["name"] = request.form["updated_task"]
        tasks[index]["deadline"] = request.form["updated_deadline"]

        save_tasks(tasks)

    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)