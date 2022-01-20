class publisher:
    def getbook(self):
        self.title=input("Title :")
        self.author=input("Author :")
class python(publisher):
    def getdetails(self):
        self.price=int(input("Price :"))
        self.nopages=int(input("No.pages :"))
    def display(self):
        print("Title of the book is :",self.title)
        print("Author of the book is :",self.author)
        print("Price is: ",self.price)
        print("Number of pages :",self.nopages)
        

a=python()
a.getbook()
a.getdetails()
a.display()
