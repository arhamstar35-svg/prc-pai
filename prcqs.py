class book:
    def __init__(self,title,author):
        self.t=title
        self.a=author
        self.available=True

class library:

    def __init__(self):
        self.books=[]

    def addbook(self,book):
        self.books.append(book)
        print(book.t,"Inserted")

    def displaybook(self):
        for book in self.books:
            print("Book : ",book.t)
            print("Book Author : ",book.a)
            print("Book availability : ",book.available)

    def borrowbook(self,name):
        for book in self.books:
            if(book.t == name):
                print("Book matched")
                if(book.available == True):
                    print("Book Borrowed")
                    book.available=False
                    return
                else:
                    print("Book Not available")
                    return

        print("Book Not found")

b1=book("harry potter","J-k Rowling")

l=library()
l.addbook(b1)

b2=book("lord of the rings","matt")
l.addbook(b2)

l.displaybook()

