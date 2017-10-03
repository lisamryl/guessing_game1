"""A number-guessing game."""

# Put your code here
import random

name = raw_input("Hi, what's your name?\n")

print "{}, I'm thinking of a number between 1 and 100 (inclusive).\n".format(name)
print "Try to guess my number.\n"

correct_num = random.randint(1, 100)
guess_count = 0
guess = None

print correct_num

while guess != correct_num:
    guess = int(raw_input("What is your guess?\n"))
    if guess < 1 or guess > 100:
        print "Out of range, guess again"
    else:
        guess_count += 1
        if guess < correct_num:
            print "Too low! Guess again. Total guesses so far: {}".format(guess_count)
        elif guess > correct_num:
            print "Too high! Guess again."
        elif guess == correct_num:
            print "Congrats, you guessed correctly after {} guesses!".format(guess_count)
