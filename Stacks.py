
my_stack = []

my_stack.append(1)
my_stack.append(2)
my_stack.append(3)

print(my_stack)

my_stack.reverse()

print(my_stack)


user_stack = []

def user_input():
  user_name = input("Enter your name: ")
  user_stack.append(user_name)

  user_age = input("Enter your age: ")
  user_stack.append(user_age)

  print(user_stack)
  
  undo = input("Do you want to undo? (yes/no): ")
  if undo == "yes":
    user_stack.pop()
    print(user_stack)
  else:
    print("No undo")
    
user_input()