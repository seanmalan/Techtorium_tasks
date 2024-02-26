library = {"Ego is the Enemy": "Ryan Holiday", "Art of Seduction": "Robert Greene", "The Game": "Neil Strauss"} 


print(library)


user_library = []

book = {
  "title": input("Enter the title of the book: "),
  "author": input("Enter the author of the book: ")
}

user_library.append(book)

answer = input("Want to add another? ")

if answer == "yes":
   book = {
     "title": input("Enter the title of the book: "),
     "author": input("Enter the author of the book: ")
   }
   user_library.append(book)
   print(user_library)
else:
   print(user_library)
   print("Thank you for using the library")
    
