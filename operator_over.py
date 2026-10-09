class Book:
    def __init__(self,pages):
        self.pages=pages

    def __add__(self,other):
        return Book(self.pages+other.pages)

d=Book(100)
d1=Book(200)
d2=Book(300)
result=d+d1+d2

print(result.pages)