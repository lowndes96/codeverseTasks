current_list = [1,2,3]

def square(number):
  return number * number 

def map(list, func):
    output_list = []
    for num in list: 
        output_list.append(func(num))
    return output_list


print(map(current_list,square))
