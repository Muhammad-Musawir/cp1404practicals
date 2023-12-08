def main():
    user_dictionary = {}

    while True:
        email = input("Email: ").strip()

        if not email:
            break
        name = extract_name(email)

        confirmation = input(f"Is your name {name}? (Y/n) ").strip().lower()

        if confirmation != 'y':
            name = input("Name: ").strip().title()

        user_dictionary[email] = name

    for email, name in user_dictionary.items():
        print(f"{name} ({email})")


def extract_name(email):
    return email.split('@')[0].title()

main()