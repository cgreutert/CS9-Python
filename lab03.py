'''
Lab03
'''
def multiply(x,y):
    '''the parameters x and y are positive integers (including 0)
      returns the product of x and y'''
    if x<y:
        return multiply(y, x)
    elif x!=0 and y != 0:
        return x + multiply(x, y-1)
    if x == 0 or y == 0:
        return 0

def collectOddValues(listOfInt):
    '''the parameter is a list containing positive integer values and returns a list of odd values'''
    if not listOfInt:
        return []
    if listOfInt[0] % 2 == 1:
        return [listOfInt[0]] + collectOddValues(listOfInt[1:])
    return collectOddValues(listOfInt[1:])
    
def countInts(listOfInt, num):
    '''parameter is a list of integer values and num is an integer, returns the number of times num
      appears in the list'''
    if listOfInt == []:
        return 0
    if listOfInt[0] == num:
        return 1 + countInts(listOfInt[1:], num)
    return countInts(listOfInt[1:], num)

def reverseString(s):
    '''s is a string, returns a string in the reverse order of s'''
    if len(s) == 0:
        return s
    else:
        return s[-1] + reverseString(s[:-1])

def removeSubString(s, sub):
    '''s and sub are strings of at least one character, returns a string where all occurrences of sub
      are removed'''
    if not s:
        return ""
    if s[0:len(sub)] == sub:
        return removeSubString(s[len(sub):], sub)
    else:
        return s[0] + removeSubString(s[1:], sub)

            
