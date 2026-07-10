class Book:
    def __init__(self,title,author):
        self.title=title
        self.author=author
    
    def __str__(self):
        return f"{self.title} by {self.author}"
        
book1= Book("the jungle book" ,"j.k rowling")
book2= Book("wings of fire" ,"apj abdul kalam")
my_lst=list()

print((my_lst))
print((book1))
print(book2)

