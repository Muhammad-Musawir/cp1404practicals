"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""
import random


def main():
    score = float(input("Enter score:"))
    result = score_result(score)
    print(result)
    score = random.randint(0,100)
    result = score_result(score)
    print(f"Random score = {score}, which is {result}")


def score_result(score):
    if score < 0 or score > 100:
        prompt = "invalid score"
    elif score >= 50:
        prompt = "Passable"
    elif score < 50:
        prompt = "bad"
    return prompt

main()