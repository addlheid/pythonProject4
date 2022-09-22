message = input("What is your name?")
print(f"\nWelcome to Anderson University, {message}")
print(f'\n{message}, how much money do you make?')

prompt = "If you give us your budget, we can help you buy a processor."
budget = input("What is your budget, in numbers?")
budget = int(budget)

if budget >= 100:
    print("\nYou can afford the i3 or i5 processor.")
if budget >= 200:
    print("\nYou can probably afford the i7 or i9 processor.")

number = input("Enter a number, and I'll tell you if it's even or odd: ")
number = int(number)

if number % 2 == 0:
    print(f"\nThis number {number} is even.")
else:
    print(f"\nThis number {number} is odd.")



