from Author import Author
from BOOK import BOOK
from Libary import Libary


au1 =Author("Ahmad","68884548","ahmadhg@gmail.com","25")
au2 =Author("sara","78564545","sarakg@gmail.com" ,"28")
au3 =Author("aseel","745845244","aseelog@gmail.com","26")
au4 =Author("hanaa","465845465","hanaalg@gmail.com","29")
au5 =Author("yasmin","85446486","yasminghourab@gmail.com","30")
au6 =Author("wafaa","854545455","wafaajk@gmail.com","40")

book1 =BOOK("JAVA"        ,"09-09-2009", 1 , au1.id)
book2 =BOOK("PYTHON"      ,"10-10-2010", 2 , au2.id)
book3 =BOOK("PHP"         ,"11-11-2011", 3 , au3.id)
book4 =BOOK("C#"          ,"12-12-2012", 4 , au4.id)
book5 =BOOK("JAVASCRIPT"  ,"08-08-2009", 5 , au1.id)
book6 =BOOK("LOJIC       ","13-10-2010", 6 , au3.id)
book7 =BOOK("HTML"        ,"06-06-2011", 7 , au6.id)
book8 =BOOK("CSS"         ,"01-01-2012", 8 , au5.id)



Lib = Libary()


Lib.add_author(au1)
Lib.add_author(au2)
Lib.add_author(au3)
Lib.add_author(au4)
Lib.add_author(au5)
Lib.add_author(au6)

Lib.add_book(book1)
Lib.add_book(book2)
Lib.add_book(book3)
Lib.add_book(book4)
Lib.add_book(book5)
Lib.add_book(book6)
Lib.add_book(book7)
Lib.add_book(book8)




for author in Lib.Author :
    print("name : ",author.name , "phone : " ,author.phone ,"Email :",author.Email,"age",author.age)

Lib.remove_author(au6.id)

for author in Lib.Author :
    print("name : ",author.name , "phone : " ,author.phone ,"Email :",author.Email,"age",author.age)
Lib.print_authors()

Lib.print_books()
Lib.remove_book(book1.id)
Lib.print_books()

Lib.print_author_books(au1.id)