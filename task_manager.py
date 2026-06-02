import json
from datetime import datetime


class Task:
    """
    Represents a single task.
    """

    def __init__(
        self,
        task_id,
        title,
        description,
        deadline,
        priority
    ):
        self.task_id = task_id
        self.title = title
        self.description = description
        self.deadline = deadline
        self.priority = priority
        self.completed = False
        self.created_at = datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"
        )

    def mark_complete(self):
        self.completed = True

    def to_dict(self):
        return {
            "task_id": self.task_id,
            "title": self.title,
            "description": self.description,
            "deadline": self.deadline,
            "priority": self.priority,
            "completed": self.completed,
            "created_at": self.created_at
        }


class TaskManager:

    def __init__(self):
        self.tasks = []
        self.file_name = "tasks.json"

    def add_task(
        self,
        title,
        description,
        deadline,
        priority
    ):

        task_id = len(self.tasks) + 1

        task = Task(
            task_id,
            title,
            description,
            deadline,
            priority
        )

        self.tasks.append(task)

        print("Task added successfully.")

    def display_tasks(self):

        if not self.tasks:
            print("No tasks available.")
            return

        print("\nTASK LIST")
        print("=" * 80)

        for task in self.tasks:

            status = (
                "Completed"
                if task.completed
                else "Pending"
            )

            print(f"ID: {task.task_id}")
            print(f"Title: {task.title}")
            print(f"Description: {task.description}")
            print(f"Deadline: {task.deadline}")
            print(f"Priority: {task.priority}")
            print(f"Status: {status}")
            print(f"Created: {task.created_at}")
            print("-" * 80)

    def complete_task(self, task_id):

        for task in self.tasks:

            if task.task_id == task_id:
                task.mark_complete()
                print("Task completed.")
                return

        print("Task not found.")

    def delete_task(self, task_id):

        for task in self.tasks:

            if task.task_id == task_id:
                self.tasks.remove(task)
                print("Task deleted.")
                return

        print("Task not found.")

    def search_tasks(self, keyword):

        results = []

        for task in self.tasks:

            if keyword.lower() in task.title.lower():
                results.append(task)

        return results

    def save_tasks(self):

        data = []

        for task in self.tasks:
            data.append(task.to_dict())

        with open(self.file_name, "w") as file:
            json.dump(data, file, indent=4)

        print("Tasks saved successfully.")

    def load_tasks(self):

        try:

            with open(self.file_name, "r") as file:

                data = json.load(file)

                for item in data:

                    task = Task(
                        item["task_id"],
                        item["title"],
                        item["description"],
                        item["deadline"],
                        item["priority"]
                    )

                    task.completed = item["completed"]
                    task.created_at = item["created_at"]

                    self.tasks.append(task)

        except FileNotFoundError:
            pass

    def statistics(self):

        total = len(self.tasks)

        completed = len([
            task for task in self.tasks
            if task.completed
        ])

        pending = total - completed

        print("\nPROJECT STATISTICS")
        print("=" * 40)
        print(f"Total Tasks: {total}")
        print(f"Completed: {completed}")
        print(f"Pending: {pending}")

    def overdue_tasks(self):

        print("\nOVERDUE TASKS")
        print("=" * 40)

        today = datetime.now()

        found = False

        for task in self.tasks:

            if task.completed:
                continue

            deadline = datetime.strptime(
                task.deadline,
                "%Y-%m-%d"
            )

            if deadline < today:

                found = True

                print(
                    f"{task.title} "
                    f"(Due {task.deadline})"
                )

        if not found:
            print("No overdue tasks.")


def display_menu():

    print("\nTASK MANAGEMENT SYSTEM")
    print("=" * 40)

    print("1. Add Task")
    print("2. View Tasks")
    print("3. Complete Task")
    print("4. Delete Task")
    print("5. Search Task")
    print("6. Statistics")
    print("7. Overdue Tasks")
    print("8. Save")
    print("9. Exit")


def main():

    manager = TaskManager()

    manager.load_tasks()

    while True:

        display_menu()

        choice = input(
            "\nEnter your choice: "
        )

        if choice == "1":

            title = input("Title: ")

            description = input(
                "Description: "
            )

            deadline = input(
                "Deadline (YYYY-MM-DD): "
            )

            priority = input(
                "Priority (High/Medium/Low): "
            )

            manager.add_task(
                title,
                description,
                deadline,
                priority
            )

        elif choice == "2":

            manager.display_tasks()

        elif choice == "3":

            task_id = int(
                input("Task ID: ")
            )

            manager.complete_task(task_id)

        elif choice == "4":

            task_id = int(
                input("Task ID: ")
            )

            manager.delete_task(task_id)

        elif choice == "5":

            keyword = input(
                "Search keyword: "
            )

            results = manager.search_tasks(
                keyword
            )

            if not results:
                print("No matching tasks.")
            else:

                for task in results:
                    print(
                        f"{task.task_id} - "
                        f"{task.title}"
                    )

        elif choice == "6":

            manager.statistics()

        elif choice == "7":

            manager.overdue_tasks()

        elif choice == "8":

            manager.save_tasks()

        elif choice == "9":

            manager.save_tasks()

            print(
                "Thank you for using "
                "Task Management System."
            )

            break

        else:

            print("Invalid option.")


if __name__ == "__main__":
    main()
