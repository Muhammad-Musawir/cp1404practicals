numbers = [3, 1, 4, 5, 9, 2]
"""
numbers[0] = 3
numbers[-1] = 2
numbers[3] = 5
numbers[:-1] = [3, 1, 4, 5, 9]
numbers[3:4] = 5
5 in numbers = True
7 in numbers = False 
"3" in numbers = False
numbers + [6, 5, 3] = [3, 1, 4, 5, 9, 2, 6, 5, 3]
"""
# Change the first element of numbers to "ten" (the string, not the number 10)
numbers[0]= "ten"
print(numbers)