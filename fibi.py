def fib(length, fib1 = 0, fib2=1):
    if length > 0:
        print(fib1)
        fib(length -1, fib2, fib1 + fib2) 

      
fib(5)


