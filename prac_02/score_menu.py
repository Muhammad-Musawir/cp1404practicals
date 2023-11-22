
def main():
    MENU = """G - Enter Score \nP - Print result \nS = Show Stars \nQ = Quit"""
    print(MENU)
    choice = input("Enter a choice:").upper()
    while choice != "Q":
        if choice == "G":
            score = get_valid_score()
            print(MENU)
            choice = input("Enter a choice:").upper()
        elif choice == "P":
            score = get_valid_score()
            result = score_result(score)
            print(f"Result = {result}")
            print(MENU)
            choice = input("Enter a choice:").upper()
        elif choice == "S":
            score = get_valid_score()
            result = score_result(score)
            print(f"Result = {result}")
            for i in range(len(result)):
                print("*", end='')
            print(MENU)
            choice = input("Enter a choice:").upper()
        elif choice == "q":
            print("Quited")



def get_valid_score():
    score = float(input("Enter Your score:"))
    while score > 100 or score < 0:
        print("invalid score")
        score = float(input("Enter Your score"))
    return score

def score_result(score):
    if score < 0 or score > 100:
        prompt = "invalid score"
    elif score >= 50:
        prompt = "Passable"
    elif score < 50:
        prompt = "bad"
    return prompt
main()