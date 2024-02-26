#Add a task:

todo_list = []


class Task:
    def __init__(self, task, priority):
        self.task = task
        self.priority = priority
        self.completed = False

    def __str__(self):
        return f"{self.task} - {self.priority}"

    def mark_completed(self):
        self.completed = True
        

def add_task(todo_list):
  new_task = {
    "id": len(todo_list) + 1,
    "task": input("Enter the task: "),
    "priority": input("Enter the priority (high, medium, low): "),
    "completed": False
  }
  todo_list.append(new_task)
  
  
  


#Users can input a task along with its priority (high, medium, low).


#Each task should have a unique identifier (ID).


#Task details should be stored in a file.



#Display all tasks:

#Users can see a list of all tasks in the ToDo list.



#The list should display each task's ID, description, and priority.



#Mark a task as completed:


#Users can mark a task as completed, and completed tasks should be visually distinguished in the list.