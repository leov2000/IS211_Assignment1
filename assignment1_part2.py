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