    #we need to welcome the usere to the game
print("Welcome to the Operator precedence calculator")
    #we need to tell the user what the equation is
print("Lets try to solve the equation of a = 5 * 2 + 3")


def equation1():
    #we need to ask them to perform the first operation
    print("Lets try to perform the first equation. According to BEDMAS, the order of operations is: Bracket, Exponents, Division, Multiplication, Addition, Subtraction. So, we need to perform the multiplication first. What is 5 * 2?")
    sum1 = int(input("Enter your answer here: "))
    result1 = 5 * 2
    if sum1 == result1:
        print("Correct! 5 * 2 = 10")
    else:
        print("Incorrect. try again")
        sum1 = int(input("5 * 2 is? "))
    #we need to give them the answer and explain why
    print("The answer is 10 because 5 * 2 = 10")


    
    
def equation2():
    #we need to ask them to solve the second operation
    sum2 = int(input("Now that we have 10, we can add 3 to it. What is 10 + 3? "))
    result2 = 10 + 3
    if sum2 == result2:
        print("Correct! 10 + 3 = 13")
    else:
        print("Incorrect. try again")
        sum2 = int(input("10 + 3 is? "))
    #we need to give them the answer and explain why
    print("The answer is 13 because 10 + 3 = 13")


def main():
    equation1()
    equation2()
    print("The final answer is 13")
    print("Thank you for playing the game")
    #for extra help go to a website
    print("for more infomartion on operator precedence, go to https://www.mathsisfun.com/operation-order-bodmas.html")
main()
    