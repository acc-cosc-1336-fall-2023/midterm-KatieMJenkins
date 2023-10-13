#add import

import question_d

def try_again():
    while True:
        d = input("Would you like to guess again? y or n: ")
        if d == "y" or d == "Y" or d == "yes" or d == "Yes":
            run_main()
            break
        elif d == "n" or d == "N" or d == "No" or d == "no":
            print("Ending Program. Bye!")
            break
        else:
            print("Invalid selection: Type y or n")

def run_main():
    guess = None
    num = question_d.get_random_number()
    while guess != num:
        guess = input("Guess a whole number between 1 and 5: ")
        guess = int(guess)

        if guess == num:
            print("Wow! Congratulations! You won!!")
            break
        else:
            print("No, sorry. Try again.")

    try_again()
    
print("Try to guess the random number between 1 and 5!")
run_main()
