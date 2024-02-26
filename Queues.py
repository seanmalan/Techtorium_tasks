

to_do = ["wash the car", "buy groceries", "feed the cat", "pick up the kids"]

print("To Do List: ", to_do)

def add_task():
  task = input("Add a task to the list: ")
  to_do.append(task)
  print(to_do)
  finished = input(f"are you finished with the task '{to_do[0]}' (y/n): ")
  if finished == "y":
    to_do.pop(0)
    print(to_do)
  else:
    print("Goodbye!")
    exit()

add_task()



