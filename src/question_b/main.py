#add import
import question_b

def try_again():
    while True:
        b = input("Would you like another sum of even numbers? y or n: ")
        if b == "y" or b == "Y" or b == "yes" or b == "Yes":
            run_main()
            break
        elif b == "n" or b == "N" or b == "no" or b == "No":
            print("Exiting the program. See ya!")
            break
        else:
            print("Invalid selection. type y or n: ")

def run_main():
    while True:
        try:
            num =int(input("Please enter a whole number: "))
            break
        except ValueError:
            print("This is not a whole number!")
    b =(question_b.get_sum_of_evens(num))
    print(b)
    try_again()

print("This program will return a sum of all the even numbers up to your chosen value.")
run_main()
