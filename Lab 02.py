class Catalog:
    books = []

    def delete_book(self, isbn):
        if isinstance(isbn, int):
            index = 0
            for book in self.books:
                if(book.isbn == isbn):
                    self.books.pop(index)
                index += 1
        else:
            exit

    def search(self, section, keyword):
        search_list = []
        for book in self.books:

            if(section == "Title"):
                if(keyword in book.title):
                    search_list.append(book)

            elif(section == "ISBN"):
                if(book.isbn == keyword):
                    search_list.append(book)

            elif(section == "DDS Number"):
                if(book.dds_number == keyword):
                    search_list.append(book)

            elif(section == "Author"):
                for author in book.authors:
                    if(keyword == author.name):
                        search_list.append(book)
                        break

        return search_list


class Book:
    _amount = 0

    def __init__(self):
        Book._amount += 1
        self._isbn = Book._amount
        self._authors = []

        # Catalog.books.append(self)

    #Get & Add - Author
    @property
    def authors(self):
        return self._authors

    def add_authors(self, author):
        self._authors.append(author)

    #Get - ISBN
    @property
    def isbn(self):
        return self._isbn

    #Set & Get - Title
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, new_title):
        if isinstance(new_title, str):
            self._title = new_title
        else:
            print("ERROR: please input title to string")
            exit()

    #Set & Get - Subject
    @property
    def subject(self):
        return self._subject

    @subject.setter
    def subject(self, new_subject):
        if isinstance(new_subject, str):
            self._subject = new_subject
        else:
            print("ERROR: please input subject to string")
            exit()

    # Set & Get - DDS Number
    @property
    def dds_number(self):
        return self._dds_number

    @dds_number.setter
    def dds_number(self, new_dds_number):
        if isinstance(new_dds_number, int):
            self._dds_number = new_dds_number
        else:
            print("ERROR: please input subject to int")
            exit()


class Author:
    def __init__(self, name):
        self.name = name

    #Set & Get - Name
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        if isinstance(new_name, str):
            self._name = new_name
        else:
            print("ERROR: please input author name to string")
            exit()


# Catalog -------------------------------
Book_Catalog = Catalog()
# Author --------------------------------
human1 = Author("KUNTHIDA PUKKALO")
human2 = Author("Sky Kung")
human3 = Author("Wanbura Han")
human4 = Author("Phongphiphat Senta")

# Book 1 --------------------------------
book1 = Book()
book1.title = "คิดต่างอย่างสร้างสรรค์"
book1.subject = "ปรัชญา"
book1.dds_number = 100
book1.add_authors(human1)
book1.add_authors(human3)

Book_Catalog.books.append(book1)

# Book 2 --------------------------------
book2 = Book()
book2.title = "กลัวเมียกลกัวหมาดีกว่า"
book2.subject = "ปรัชญา"
book2.dds_number = 100
book2.add_authors(human3)

Book_Catalog.books.append(book2)

# Book 3 --------------------------------
book3 = Book()
book3.title = "คุยอย่างไงให้สับรางเก่ง"
book3.subject = "บริหาร"
book3.dds_number = 350
book3.add_authors(human2)

Book_Catalog.books.append(book3)

# Book 4 --------------------------------
book4 = Book()
book4.title = "เรียนอังกฤษได้ภายใน 3 นาที"
book4.subject = "ภาษาศาสตร์"
book4.dds_number = 400
book4.add_authors(human4)
book4.add_authors(human3)

Book_Catalog.books.append(book4)

# Delete ---------------------------------
Book_Catalog.delete_book(2)

# Search ---------------------------------
search_data = Book_Catalog.search(keyword=100, section="DDS Number")

print("===========================")
for book in search_data:
    print(f"ID : {book.isbn}")
    print(f"Title : {book.title}")
    print(f"Subject : {book.subject}")
    print(f"DDS Number : {book.dds_number}")
    print(f"Author :")
    for author in book.authors:
        print(f"  - {author.name}")
    print("===========================")
