class Book:

    def __init__(self, author, title):
        self.author = author
        self.title = title

    def display(self):
        print("{}, written by {}".format(self.author, self.title))