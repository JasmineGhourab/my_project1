class BOOK:

    __id_BOOK = 0

    def __init__(self, title, publishing_date, version, id_author):
        BOOK.__id_BOOK +=1
        self.id = BOOK.__id_BOOK
        self.title =title
        self.publishing_date = publishing_date
        self.version =version
        self.id_author =id_author