"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""

"""
Pseudocode:
TARGET_VALUE = 1000
get sales
while sales >= 0:
    if sales < TARGET_VALUE :
        bonus = (10/100) * sales
    else:
        bonus = (15/100) * sales
    display bonus
    get sales
pr
"""
TARGET_VALUE = 1000
sales_amount = float(input("Enter salary:"))
while sales_amount >= 0:
    if sales < TARGET_VALUE :
        bonus = (10/100) * sales_amount
    else:
        bonus = (15/100) * sales_amount
    print(f"Your bonus amount is: {bonus}")
    sales = float(input("Enter salary:"))
print("ooops")
