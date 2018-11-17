#handles invalid user input errors, if it should be an integer and the user enters a string for example
try:
    number = int(input("Enter a Number: "))
    print(number)
except ZeroDivisionError:
    print("Divided by Zero!")
    #must add a value = 10 / 0 to trigger this exception
except ValueError:
    print("Invalid Input. Try Again!")