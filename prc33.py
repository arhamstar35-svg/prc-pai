import json

def addbook():

    try:
        file = open("books.json", "r")
        books = json.load(file)
        file.close()

    except FileNotFoundError:
        books = []

    id = input("Enter book ID: ")
    title = input("Enter book title: ")
    author = input("Enter book author: ")
    availability = input("Enter book availability: ")

    data = {
        "id": id,
        "title": title,
        "author": author,
        "availability": availability
    }

    books.append(data)

    file = open("books.json", "w")
    json.dump(books, file, indent=4)
    file.close()

addbook()