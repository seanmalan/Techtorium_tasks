library = []

id = 1


def Action(id, library):
    action = input("Enter 'view' to view the library, 'add' to add a book, 'search' to search for a book or 'quit' to exit the library: ")
    if action == "view":
        print(library)
        Action(id, library)
    elif action == "add":
        add_book(library)
    elif action == "search":
        search_by_id(library)
    elif action == "quit":
        print("Goodbye")
    else:
        print("Invalid input")
        Action(id, library)



def add_book(library):
    global id
    new_book = {
        "id": id,
        "title": input("Enter the title of the book: "),
        "author": input("Enter the author of the book: "),
        "genre": input("Enter the genre of the book: ")
    }
    library.append(new_book)
    print("Book added successfully!")
    print(f"The book added was {new_book}")
    id += 1
    Action(id, library)



def search_by_id(library):
    search_id = int(input("Enter the id of the book you want to search for: "))
    for book in library:
        if book["id"] == search_id:
            print(f"The book with id {search_id} is {book}, the author is {book['author']} and the genre is {book['genre']}")
            return
    print("Book not found")



def main(id, library):
    Action(id, library)

main(id, library)
