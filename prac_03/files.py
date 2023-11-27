# Asking the user for their name
user_name = input("Enter your name: ")

with open("name.txt", "w") as file:
    file.write(user_name)


# Reading the name from "name.txt"
with open("name.txt", "r") as file:
    stored_name = file.read()
print(f"Your name is {stored_name}")


# Reading the first two numbers from "numbers.txt"
with open("numbers.txt", "r") as file:
    num1 = int(file.readline())
    num2 = int(file.readline())
print("Sum of the first two numbers:", num1 + num2)

# Reading all numbers from "numbers.txt" and calculating the total
total = 0
with open("numbers.txt", "r") as file:
    for line in file:
        total += int(line)

# Printing the total
print("Total of all numbers:", total)

