num1 = input("Please enter a number: ")


def positive():
  if int(num1) == 0:
      print("The number is zero")
  elif int(num1) > 0:
      print("The number is positive")
  else:
      print("The number is negative")
      
positive()