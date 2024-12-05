l = [1, 2, 3,4,5,6]
def isEven(number):
  if number % 2 == 0:
    return True
  return False

def filterFunc(list,func): 
  filtered_list = []
  for item in list: 
    if func(item) == True: 
      filtered_list.append(item)
  return filtered_list

print(filterFunc(l,isEven))