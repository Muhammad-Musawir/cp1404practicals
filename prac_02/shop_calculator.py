"""
total_price = 0
get number_of_items
while number_of_items <= 0:
    display "Invalid Number of Items"
    get number_of_items

for i in range(number_of_items):
    get item_price
    total_price = total_price + item_price
display total_price
if total_price > 100:
    discounted_price = total_price - 10/100 * total_price
    display discounted_price


"""


total_price = 0
number_of_items = int(input("Number of items:"))
while number_of_items <= 0:
    print("Invalid Number of Items!!")
    number_of_items = int(input("Number of items:"))

for i in range(number_of_items):
    item_price = float(input(f"Price of Item_{i+1} :"))
    total_price += item_price
print(f"Total price = {total_price: .2f}")
if total_price > 100:
    discounted_price = total_price - 10/100 * total_price
    print(f"Price after 10% discount = {discounted_price}")
