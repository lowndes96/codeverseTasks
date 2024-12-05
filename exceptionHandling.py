# def maximum(a, b):
#     if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
#         raise Exception()
#     return a if a > b else b 
#1) How to inform the caller of the function that an exceptional situation has occurred and 
# 2) How to handle the exceptional situation when it occurs.
# try:
#   maximum(3, 'World')
# except:
#   print('Wrong arguments passed to max')

#   Write a Calculator class having methods to add, subtract, divide and multiply 2 numbers. 
#   Ensure that the methods throw appropriate exceptions. 
#   Finally, write a class CalculatorUser which makes use of this implementation and handles exceptions appropriately.
import logging

class CalculatorUser: 
    def __init__(self):
        pass

    def add(self,num1,num2):
        try:
            print(float(num1)+float(num2))
        except ValueError:
            print('error - please use numerical input only')
        except Exception as e:
            logging.exception(e)

    def subtract(self,num1,num2): 
        try:
            print(float(num1)-float(num2))
        except ValueError:
            print('error - please use numerical input only')
        except Exception as e:
            logging.exception(e)
    
    def divide(self,num1,num2):
        try:
            print(float(num1)/float(num2))
        except ValueError as e:
            print('error - please use numerical input only')
        except ZeroDivisionError as e:
            print(" you can't divide a number by zero")
        except Exception as e:
            logging.exception(e)
    def multipy(self,num1,num2):
        try:
            print(float(num1)*float(num2))
        except ValueError as e:
            print('error - please use numerical input only')
        except Exception as e:
            logging.exception(e)


calc = CalculatorUser()

calc.add(3, 2)
calc.add(1,'who?')
calc.add('what','who?')

calc.divide(5,0)
calc.multipy(0,5)