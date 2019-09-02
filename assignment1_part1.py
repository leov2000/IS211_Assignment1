def listDivide(numbers, divide = 2):
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