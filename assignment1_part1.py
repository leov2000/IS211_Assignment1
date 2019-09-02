def listDivide(numbers, divide = 2):
    if not numbers:
        return 0
    
    remainderList = [n for n in numbers if n % divide == 0]

    if remainderList:
        return len(remainderList)

    else: 
        raise ListDivideException

def testDivide():
    listDivide([1,2,3,4,5])
    listDivide([2,4,6,8,10])
    listDivide([30, 54, 63,98, 100], divide=10)
    listDivide([])
    listDivide([1,2,3,4,5], 1)

class ListDivideException(Exception):
    pass

