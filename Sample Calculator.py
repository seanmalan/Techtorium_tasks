print ("Welcome to Seans Calculator app")



def calculator():
  
  accepted_operators = ["+", "-", "*", "/"]
  
  num1 = input("Enter the first number: ")
  print(num1)
  print("the input type is {}" .format(type(num1)))
  
  if num1.isdigit() == False:
    print("Error: Please enter a valid number.")
    calculator()
  else:
    num1 = float(num1)
    print("the output type is {}" .format(type(num1)))
    
  operator = input("Enter the operator: ")
  if operator not in accepted_operators:
    print("Error: Please enter a valid operator.")
    calculator()
  num2 = input("Enter the second number: ")
  

  if operator == "+":
    result = num1 + num2
    print(f"Addition: {num1} + {num2} = {result}")
  elif operator == "-":
    result = num1 - num2
    print(f"Subtraction: {num1} - {num2} = {result}")
  elif operator == "*":
    result = num1 * num2
    print(f"Multiplication: {num1} * {num2} = {result}")
  elif operator == "/":
    if num2 != 0:
      result = num1 / num2
      print(f"Division: {num1} / {num2} = {result}")
    else:
      print("Error: Cannot divide by zero.")
      calculator()
      

calculator();