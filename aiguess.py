#number = 74
print("Enter a number for the Computer to guess ")
number = input()
number = int(number)
import random
aiguess = random.randint(1,100)
guesses = 0
print("Guess my number between 1 and 100 ")
#guess = input()
#guess = int(guess)
print(aiguess)
lowguess = 1
highguess = 100
while aiguess != number:
    guesses = guesses + 1
    print("Guess number", guesses, "is", aiguess)
    if aiguess < number:
        print(aiguess, "is too low")
        print("Try again ")
        lowguess = aiguess + 1
        aiguess = random.randint(lowguess,highguess)
    elif aiguess > number:
        print(aiguess, "is too high")
        print("Try again ")
        highguess = aiguess - 1
        aiguess = random.randint(lowguess,highguess)
#    else:
#guesses += 1
print(aiguess,"That's correct!!!")
print("You took ", guesses+1, " guesses to find my number")
leave = input()