for num in range(1,100): 
    if (num % 7 == 0) and (num % 3 == 0): 
        print('FastCar')
    elif (num % 7 == 0): 
        print('Car')
    elif (num % 3 == 0):
        print('Fast')
    else: 
        print(num)