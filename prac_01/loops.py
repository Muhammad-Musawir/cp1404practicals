for i in range(1, 21, 2):
    print(i, end=' ')
print()
for i in range(0, 101, 10):
    print(i, end=' ')
print()
for i in range(20, 0, -1):
    print(i, end=' ')
print()

star_number = int(input("Number of Stars:"))
for i in range(star_number):
    print("*", end="")