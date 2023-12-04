numbers = []
# print("Enter 5 numbers")
# for i in range(5):
#     user_input = int(input(f"Number {i+1}: "))
#     numbers.append(user_input)
# print(f"The first number is {numbers[0]}")
# print(f"the last number is {numbers[4]}")
# print(f"The smallest number is {min(numbers)}")
# print(f"The largest number is {max(numbers)}")
# print(f"The3 average of number is {sum(numbers)/5}")

usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn',
             'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']

name = input("Enter username: ").lower()
if name not in usernames:
    print("Access Denied")
else:
    print("Access Granted")