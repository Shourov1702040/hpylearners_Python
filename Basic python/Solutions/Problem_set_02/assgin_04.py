
class Product:
    def __init__(self,id_, title, price):
        self.__id = id_
        self.__title = title
        self.__price = price
    def get_id_title_price(self):
        return "ID: "+str(self.__id)+" Title:"+self.__title+" Price: "+str(self.__price)

class Book(Product):
    def __init__(self,id_, title, price, isbn, pub):
        Product.__init__(self,id_, title, price)
        self.isbn = isbn
        self.pub = pub

    def printDetail(self):
        print(self.get_id_title_price())
        print("ISBN: ",self.isbn," Publisher: "+self.pub)

class CD(Product):
    def __init__(self,id_, title, price, Band, dur, gen):
        Product.__init__(self,id_, title, price)
        self.Band = Band
        self.dur = dur
        self.gen = gen

    def printDetail(self):
        print(self.get_id_title_price())
        print("Band: "+self.Band+" Publisher: ",self.dur,"minutes Genrc: "+self.gen)


book = Book(1,"The Alchemist",500,"97806","HarperCollins")
print(book.printDetail())
print("-----------------------")
cd = CD(2,"Shotto",300,"Warfaze",50,"Hard Rock")
print(cd.printDetail())
