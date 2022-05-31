class Author:

    __id_author = 0
    def __init__(self,name,phone,Email,age):
        Author.__id_author+=1
        self.id    = Author.__id_author
        self.name  = name
        self.phone = phone
        self.Email =Email
        self.age   =age



au1 =Author("Ahmad","68884548","ahmadhg@gmail.com","25")
au2 =Author("sara","78564545","sarakg@gmail.com" ,"28")
au3 =Author("aseel","745845244","aseelog@gmail.com","26")
au4 =Author("hanaa","465845465","hanaalg@gmail.com","29")
au5 =Author("yasmin","85446486","yasminghourab@gmail.com","30")
au6 =Author("wafaa","854545455","wafaajk@gmail.com","40")


print(au1.id)
print(au2.id)
print(au3.id)
print(au4.id)
print(au5.id)
print(au6.id)



