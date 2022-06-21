
#bulid a simple game that take a number form user and tell the user if this number even or odd
print("even or odd number game ")
print('''
--you well add the number
--and i well tell u if his even or odd
--Enter x on input section to exit
''')
while True:
    choise_num1= input("Enter the number: ")
    if choise_num1 == "x":
        print("Closeing the Game!")
        print("Tanks....")
        break
    try:
        number = int(choise_num1)
        if number%2 == 0:
            print("even number")
        else:
            print("Odd number")
    except ValueError:
        print("enter i valid number")
    print("_____________")
