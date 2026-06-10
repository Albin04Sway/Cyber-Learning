secret = 21

guess = input("Guess the secret number: ")

if guess.isdigit():
    
    if int(guess) > 21:
        print(f"Your number {guess} is too high")
    elif int(guess) < 21:
        print(f"Your number {guess} is too low")
    else:
        print(f"{guess} is the correct number!!")

else:
    print("You did not enter a number")

