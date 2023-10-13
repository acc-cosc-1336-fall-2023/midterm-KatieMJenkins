import question_a

def try_again():
    while True:
        a = input("Would you like to reverse another string? y or n?:")
        if a == "y" or a == "Y" or a == "yes" or a == "Yes":
            run_main()
            break
        elif a == "n" or a == "N" or a == "no" or a == "No":
            print("exiting program. Goodbye.")
            break
        else:
            print("Invalid option. Please type y or n")

def run_main():
    while True:
        try:
            string1 = str(input("Enter a series of characters to be reversed: "))
            break
        except ValueError:
            print("Not a series of characters!")
    a = question_a.reverse_string(string1)
    print(a)
    try_again()
print("This program will reverse a string.")
run_main()      