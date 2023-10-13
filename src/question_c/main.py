#add import

import question_c

def try_again():
    while True:
        c = input("Would you like to calculate another bonus pay? y or n: ")
        if c == "y" or c == "Y" or c == "yes" or c == "Yes":
            run_main()
            break
        elif c == "n" or c == "N" or c == "no" or c == "No":
            print("Exiting now.")
            break
        else: 
            print("Invalid option. Please type y or n")

def run_main():
    while True:
        try:
            sales = int(input("Enter total sales between 0 and 2000: "))
            break
        except ValueError:
            print("Not a number between 0 and 2000")
    if sales < 0 or sales > 1999:
        print("Invalid argument")
        try_again()
    else:
        c = question_c.get_bonus_pay_amount(sales)
        print(f'Your bonus pay is ${c:.2f}')
        try_again()
print("This program will calculate your bonus pay.")
run_main()
