class Book:
    """
    A Book class used to create Book objects.

    Attributes:
        author (str): The name of an author.
        title (str): The book title of an author.
    """

    author = ''
    title = ''

    def __init__(self, author, title):
        """
        The constructor for the Book class.
        
        Parameters:
            author (str): The name of an author.
            title (str): The book title of an author. 
        """
        self.author = author
        self.title = title

    def display(self):
        """
        An auxilary method that prints a string using the 
        instance attributes `author` & `title`

        Parameters: None

        Returns: None
        """

        print("{}, written by {}".format(self.author, self.title))


if __name__ == '__main__':
    book_obj_1 = Book('Of Mice and Men', 'John Steinbeck')
    book_obj_2 = Book('To Kill a Mockingbird', 'Harper Lee')

    book_obj_1.display()
    book_obj_2.display()