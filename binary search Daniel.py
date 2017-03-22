#binary search algorithm

def binary_search(key, array, lower,upper):
    """Function to return key index using recursive binary search algorithm"""
    if upper < lower:
        return -1
    else:
        mid_point = int((upper + lower) /2)

    if array[mid_point] < key:
        return binary_search(key, array, mid_point + 1, upper)
    elif array[mid_point] > key:
        return binary_search(key, array, mid_point - 1, lower)
    else:
        return binary_search(key, array, mid_point)

def linear_search(key,array,index):
    if index < len(array):
        


#-------------------------------------------------


test_array = ["Aardvark", "Badger", "Cat", "Dog", "Eagle", "Frog", "Gecko",
              "Honey Badger", "Iguana", "Jackal", "Kid", "Llama", "Monkey",
              "Narwhal", "Ostrich", "Penguin", "Quail", "Rhinoceros", "Snake",
              "Tapir", "Upupa", "Viper", "Whale", "Xenon", "Yellow Mongoose",
              "Zebra"]

test_cases = ["Viper", "Buffalo", "Hedgehog", "Jackal", "Kid", "Seahorse",
             "Penguin"]

#Loop to search for the test data eithin the test array
for case in test_cases:
    position = binary_search(case, test_array, 0, len(test_array) -1) +1
    if position > 0:
        print(case, "is found at position", position)
    else:
        print(case, "not found in the array")
