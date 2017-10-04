"""A number-guessing game."""

# Put your code here
import random
import math

name = raw_input("Hi, what's your name?\n")

comp = raw_input("Do you want the computer to play? (Y or N)\n")
if comp.lower() == 'y':
    too_low = 0 
    too_high = 101 
    user_eval = None

    while user_eval != "you win":
        guess = (too_high - too_low)/2 + too_low
        print "Computer guessed: {}".format(guess)
        user_eval = raw_input("Enter: 'too low' or 'too high' or 'you win' \n")
        if user_eval.lower() == 'too low':
            too_low = guess 
        else: 
            too_high = guess

    print "The computer wins!"

else:
    difficulty = raw_input("Guess my number! We can make it: Easy (E), medium (M) or hard(H) [default is hard]")

    def max_range_function(difficulty):
        if difficulty.lower() == "e":
            return 10
        elif difficulty.lower() == "m":
            return 20
        else: 
            return 100

    def conversion_function(difficulty):
        if difficulty.lower() == "e":
            return 3
        elif difficulty.lower() == "m":
            return 2
        else: 
            return 1

    max_range = max_range_function(difficulty)
    conversion = conversion_function(difficulty)
    print max_range
    print conversion



    print "{}, I'm thinking of a number between 1 and {} (inclusive).\n".format(name, max_range)
    print "Try to guess my number.\n"

    correct_num = random.randint(1, max_range)
    guess_count = 0
    wins = 0
    guess_log = []
    guess = None
    max_guess = 3

    print correct_num

    while guess != correct_num:    
        if guess_count >= max_guess:
            print "Out of Turns!"
            guess_count = 0
            play_again = raw_input("Play again? Y/N: \n")
            if play_again.lower() == "y":
                difficulty = raw_input("Guess my number! We can make it: Easy (E), medium (M) or hard(H) [default is hard]")
                max_range = max_range_function(difficulty)
                conversion = conversion_function(difficulty)
                print "{}, I'm thinking of a number between 1 and {} (inclusive).\n".format(name, max_range)
                print "Try to guess my number.\n"
                correct_num = random.randint(1, max_range)
                print correct_num
                continue
            else:
                print "Thanks, come again"
                break
        else:    
            try:
                guess = int(raw_input("What is your guess?\n"))
            except ValueError:
                print "Please enter a valid integer between 1 and 100"
                continue
            if guess < 1 or guess > max_range:
                print "Out of range, guess again"
                continue
            guess_count += 1
            if guess < correct_num:
                print "Too low! Guess again. Total guesses so far: {}".format(guess_count)
            elif guess > correct_num:
                print "Too high! Guess again. Total guesses so far: {}".format(guess_count)
            elif guess == correct_num:
                print "Congrats, you guessed correctly after {} guesses!".format(guess_count)
                wins += 1
                guess_log.append(guess_count * conversion)
                print "You won {} times. Lowest # guesses: {}".format(wins, min(guess_log))
               
                play_again = raw_input("Play again? Y/N: \n")
               
                if play_again.lower() == "y":
                    difficulty = raw_input("Guess my number! We can make it: Easy (E), medium (M) or hard(H) [default is hard]")
                    max_range = max_range_function(difficulty)
                    conversion = conversion_function(difficulty)
                    print "{}, I'm thinking of a number between 1 and {} (inclusive).\n".format(name, max_range)
                    print "Try to guess my number.\n"
                    correct_num = random.randint(1, max_range)
                    print correct_num
                    continue
                else:
                    print "Thanks, come again"