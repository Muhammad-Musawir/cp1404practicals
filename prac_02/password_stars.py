password =input("Password:")
while len(password) < 4:
    print("Password should be atleast 4 characters")
    password = input("Password:")
for i in range(len(password)):
    print("*", end='')