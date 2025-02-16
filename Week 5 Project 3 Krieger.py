import math
smaller = int(input("Enter the smaller number: "))
larger = int(input("Enter the larger number: "))
maxguess = math.log(larger - smaller + 1)
count = 0
while count < maxguess:
    count += 1
    print(smaller,larger)
    guess = int((smaller + larger) / 2)
    print("The number is", guess)
    hint = input("Enter >, <, or =: ")
    if hint == "<":
        larger = guess
    elif hint == ">":
        smaller = guess
    elif hint == "=":
        print("Yes! I've got it in", count, "tries!")
        break
else:
    print("I'm out of guesses, and you cheated!")
