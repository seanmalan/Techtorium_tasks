



def answer_check():
#I need to write the questions
  question1 = "What is the capital of France? "
  question2 = "What is the capital of Germany? "
  question3 = "What is the capital of Italy? "
  question4 = "What is the capital of Spain? "
  question5 = "What is the capital of Portugal? "
  #I need to write the answers
  answer1 = "Paris"
  answer2 = "Berlin"
  answer3 = "Rome"
  answer4 = "Madrid"
  answer5 = "Lisbon"

  #I need to give the answers a score
  correct_score = 1

  # I need to initialize the score
  score = 0

  # ask the user for input
  user_answer1 = input(question1)
  user_answer2 = input(question2)
  user_answer3 = input(question3)
  user_answer4 = input(question4)
  user_answer5 = input(question5)


  # check if the input is correct
  if user_answer1 == answer1:
  # if the input is correct, add 1 to the score
      score = score + correct_score
      print("Correct")
  else:
      print("Incorrect")
  # if the input is incorrect, go to next question
      
  if user_answer2 == answer2:
      score = score + correct_score
      print("Correct")
  else:
      print("Incorrect")
      
  if user_answer3 == answer3:
      score = score + correct_score
      print("Correct")
  else:
      print("Incorrect")
      
  if user_answer4 == answer4:
      score = score + correct_score
      print("Correct")
  else:
      print("Incorrect")
      
  if user_answer5 == answer5:
      score = score + correct_score
      print("Correct")
  else:
      print("Incorrect")


  # print the score
  print(f"Your score is {score} out of 5")

  #ask the user if they want to play again
  def play_again():
      play_again = input("Do you want to play again? (yes/no) ")
      if play_again == "yes":
  # if the user wants to play again, go to the first question
          answer_check()
      else:
  # if the user does not want to play again, print "Goodbye"
          print("Goodbye")
          
  play_again()



  #end
answer_check()

