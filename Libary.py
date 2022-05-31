class Libary :
    Author = []
    BOOK   = []
    def add_author(self, author):
        self.Author.append(author)

    def remove_author(self ,id ):

        for author in self.Author:

            if author.id == id :
                self.Author.remove(author)

                return

        print("Author with id : " ,id, "is not found")
    def print_authors(self):
        for author in self.Author:
            print("name : ", author.name, "phone : ", author.phone, "Email :", author.Email,"aga",author.age)

    def print_author_books(self,id):
        is_author_exist =False
        author_name = ""
        for author in self.Author:
            if author.id == id :
                is_author_exist = True
                author_name = author.name
                break
        if is_author_exist == False :
            print("Author with id :", id ," is not found!")
            return

        print("books of author " , author_name , " : ")
        for book in self.BOOK:
            if book.id_author == id :
                print("title : ", book.title)


    def add_book (self,book):
        self.BOOK.append(book)

    def remove_book(self,id):
        for book in self.BOOK:
            if book.id == id:
                self.BOOK.remove(book)
                return
            print("Book with id ",id ,"is not found")

    def print_book(self,id):
        for book in self.BOOK:
            if book.id == id:
                print("Book with id ",id,"information")
                print("Title :",book.title)
                print("publishing date :",book.publishing_date)
                for author in self.Author:
                    if author.id == book.id_author :
                        print("Author :",author.name)
                        return

                    return
        print("BOOK with id ",id,"is not found!")


    def print_books(self):
        for book in self.BOOK:
            print("Book with id ", book.id, "information")
            print("Title :", book.title)
            print("publishing date :", book.publishing_date)
            for author in self.Author:
                if author.id == book.id_author:
                    print("Author :", author.name)
                    break
            print("__________________________________________\n")