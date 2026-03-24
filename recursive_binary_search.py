def recursive_binary_search(list, target):
  # if an empty list is passed in, return False
  if len(list) == 0:
    return False
  else:
    midpoint = (len(list)) // 2
    
    if list[midpoint] == target:
      return True
    else:
      if list[midpoint] < target:
        # create a sublist which starts at midpoint + 1, and go es all the way to the end.
        return recursive_binary_search(list[midpoint+1:], target)
      else:
        # create a sublist at the beginning and then go all the way up to the midpoint.
        return recursive_binary_search(list[:midpoint], target)
      
def verify(result):
  print("Target found: ", result)
  
numbers = [1,2,3,4,5,6,7,8]

result = recursive_binary_search(numbers, 12)
verify(result)

result = recursive_binary_search(numbers, 6)
verify(result)

