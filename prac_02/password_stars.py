def main():
    password = get_password()
    print_asterisks(password)


def print_asterisks(password):
    for i in range(len(password)):
        print("*", end='')


def get_password():
    password = input("Password:")
    while len(password) < 4:
        print("Password should be atleast 4 characters")
        password = input("Password:")
    return password


main()