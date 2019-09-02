class Book:
    """
    This is a class used to create Book objects.

    Attributes:
        author (str): The name of an author.
        title (str): The book title of an author.
    """
    def __init__(self, author, title):
        self.author = author
        self.title = title

    def display(self):
        print("{}, written by {}".format(self.author, self.title))