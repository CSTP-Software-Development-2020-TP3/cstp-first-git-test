import random
mynumber = random.randint(1,100)
guesses = 0
print("Guess my number between 1 and 100 ")
guess = input()
guess = int(guess)
while mynumber !="guess":
    guesses = guesses + 1
    print("Guess number ", guesses)
    if guess < mynumber:
        print("Too low")
        guess = input("Try again ")
        guess = int(guess)
    elif guess > mynumber:
        print("Too high")
        guess = input("Try again ")
        guess = int(guess)
    else:
        print("That's correct!!!")
        print("You took ", guesses, " guesses to find my number")
        break
leave = input()