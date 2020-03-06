#Name: Jayson Sandhu
#Student ID: 100659589

#Part 1
#class for defining a stack
class Stack:
    def __init__(self):
        self.items = []

    #method to check whether the stack is empty or not
    def isEmpty(self):
        return len(self.items) == 0

    #method for pushing an item on a stack
    def push(self, item):
        self.items.append(item)
    
    #method for popping an item from a stack
    def pop(self):
        return self.items.pop()
    
    #method to get the top of the stack
    def top(self):
        return len(self.items)

#Testing Output
s=Stack()
print('isEmpty():',s.isEmpty())
print('empty:',s)
s.push(1)
print('after push(1):',s)
print('isEmpty():',s.isEmpty())
s.push(10)
print('after push(10):',s)
print('pop():',s.pop())
print('after pop():',s)
s.push(2)
print('after push(2):',s)
s.push(3)
print('after push(3):',s)
s.push(4)
print('after push(4):',s)
print('pop():',s.pop())
print('after pop():',s)
print('pop():',s.pop())
print('after pop():',s)
print('pop():',s.pop())
print('after pop():',s)
print('pop():',s.pop())
print('after pop():',s)
print('isEmpty():',s.isEmpty())

#Part 2
def isPalindrome(str):
    strStack = Stack()
    n = len(str)
    palindrome = False
     
    for char in str:
        strStack.push(char)
         
    for char in str:
        if char == strStack.pop():
            palindrome = True
        else:
            palindrome = False
             
    return palindrome

#Output Function
print(isPalindrome('ablewasiereisawelba'))#True
print(isPalindrome('racecar'))#True
print(isPalindrome('racecars'))#False
print(isPalindrome('level'))#True
print(isPalindrome('lever'))#False

#Part 3
operators = {
  "+": (lambda a, b: a + b),
  "-": (lambda a, b: a - b),
  "*": (lambda a, b: a * b),
  "/": (lambda a, b: a / b)
}

def isInteger(str):
   for chr in str:
      if (chr < '0') or (chr > '9'):
         return False
   return True

#Cast string/character to an integer value
def toInteger(str):
   return int(str)

#Calculate the Reverse Polish Notation of the expressions 
def calculateRPN(expression):
  tokens = expression.split()
  stack = []

#for every token (value separated by spaces):
#if the token is a number:
#push the number to the stack
#if the token is an operator:
#Pop two numbers off of the stack (in reverse order)
#Apply the operator with the two numbers as operands
#Push the result to the stack
#The result is the only value left on the stack

  for token in tokens:
    if token in operators:
      arg2 = stack.pop()
      arg1 = stack.pop()
      result = operators[token](arg1, arg2)
      stack.append(result)
    else:
      stack.append(toInteger(token))

  return stack.pop()
  
#Output Function
print(calculateRPN("8 4 * 7 2 / + 4 1 + -"))
print(calculateRPN("1 2 5 7 9 + "))
print(calculateRPN("10 12 26 + *"))
print(calculateRPN("1000 99 108 46 + * +"))

