def listDivide(numbers, divide = 2):
    """a function that takes a number list, a 
    divide param and returns the amount of items that are 
    divisible by the divide param.

    Args:
    numbers - List[Int]: A list of integer values.
    divide - Int: A integer value.
    
    Returns | Raises:
    An integer representing the sum of the list items divisible by divide
    or an Exception if a scenario defined by the examples below fails.

    Examples:
    >>> listDivide([1,2,3,4,5])
    2
    >>> listDivide([2,4,6,8,10])
    5
    >>> listDivide([30, 54, 63,98, 100], divide=10)
    2
    >>> listDivide([])
    0
    >>> listDivide([1,2,3,4,5], 1)
    5
    >>> listDivide([1], 5)
    Traceback (most recent call last):
        File "assignment1_part1.py", line ##, in listDivide
        raise ListDivideException
        __main__.ListDivideException
    """

    #If `numbers` has no items, return a 0.
    if not numbers:
        return 0

    #If `numbers` has items, extract `n`'s that are fully divisible by `divide`.      
    remainderList = [n for n in numbers if n % divide == 0]

    # If the `remainderList` has items return the length of it.
    if remainderList:
        return len(remainderList)
    #Else raise a custom error ListDivideException exception.
    else: 
        raise ListDivideException

def testDivide():
    """" an auxilary function used to call 
    listDivide.

    Args: None

    Returns | Raises: Returns None, if there's an error an exception is raised

    """
    
    listDivide([1,2,3,4,5])
    listDivide([2,4,6,8,10])
    listDivide([30, 54, 63,98, 100], divide=10)
    listDivide([])
    listDivide([1,2,3,4,5], 1)
    # Comment-Out line below to test Exception logic
    # listDivide([1], 5)

class ListDivideException(Exception):
    pass

if __name__ == '__main__':
    testDivide()