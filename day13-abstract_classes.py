from abc import ABCMeta, abstractmethod
class Book:
    __metaclass__ = ABCMeta
    def __init__(self,title,author):
        self.title=title
        self.author=author   
    @abstractmethod
    def display(): pass
    
#Write MyBook class
class MyBook(Book):
    def __init__(self, title, author, price):
        super(Book, self).__init__()
        self.price = price 
        
    def display(self):
        print "Title: " + title
        print "Author: " + author
        print "Price: " + str(price)

title=raw_input()
author=raw_input()
price=int(raw_input())
new_novel=MyBook(title,author,price)
new_novel.display()
