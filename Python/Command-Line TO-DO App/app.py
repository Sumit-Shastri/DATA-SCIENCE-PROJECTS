import sys
import os
import json

TASK_FILE ="tasks.json"

def load_tasks():
    if not os.path.exists(TASK_FILE):
        return []
    with open(TASK_FILE, "r") as file:
        return json.load(file)

def save_tasks(tasks):
    with open(TASK_FILE , "w") as file:
        json.dump(tasks, file , indent= 4)

def add_tasks(task_text):
    tasks = load_tasks()
    tasks.append(task_text)
    save_tasks(tasks)
    print(f" Task Added : {task_text}")

def list_tasks():
    tasks = load_tasks()
    if not tasks:
        print("Your To-Do list is empty")
    else:
        print("Your Tasks : ")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {tasks}")

def remove_task(index):
    tasks = load_tasks()
    if 0 < index <= len(tasks):
        removed = tasks.pop(index - 1)
        save_tasks(tasks)
        print(f"❌ Removed task: {removed}")
    else:
        print("⚠️ Invalid task number.")
def main():
    if len(sys.argv) < 2:
        print("⚠️ Please provide a command: add, list, or remove")
        return

    command = sys.argv[1]

    if command == "add":
        if len(sys.argv) < 3:
            print("⚠️ Please provide the task to add.")
        else:
            task_text = " ".join(sys.argv[2:])
            add_tasks(task_text)

    elif command == "list":
        list_tasks()

    elif command == "remove":
        if len(sys.argv) < 3 or not sys.argv[2].isdigit():
            print("⚠️ Please provide the task number to remove.")
        else:
            index = int(sys.argv[2])
            remove_task(index)

    else:
        print(f"  Unknown command: {command}")

if __name__ == "__main__":
    main()
