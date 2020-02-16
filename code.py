#calculator
print("Hi, i'm calculator ")
calc = int (input('What operation do you want to perform?\n 1 addition \n 2 subtraction \n 3 division \n 4 multiplication \n 5 exponentiation \n '))
if calc == 1:
    print("you have chosen addition!")
    q1 = int (input('enter the first number: '))
    q2 = int (input('enter the second number: '))
    x = q1 + q2
    w = ("addition")
    a = w
elif calc == 2:
    print("you have chosen subtraction!")
    q1 = int (input('enter the first number: '))
    q2 = int (input('enter the second number: '))
    x = q1 - q2
    e = ("subtraction")
    a = e
elif calc == 3:
    print("you have chosen division!")
    q1 = int (input('enter the first number: '))
    q2 = int (input('enter the second number: '))
    x = q1 / q2
    r = ("division")
    a = r
elif calc == 4:
    print("you have chosen multiplication!")
    q1 = int (input('enter the first number: '))
    q2 = int (input('enter the second number: '))
    x = q1 * q2
    t = ("multiplication")
    a = t
elif calc == 5:
    print("you have chosen exponentiation!")
    q1 = int (input('enter the number: '))
    q2 = int (input('what number to raise to a power: '))
    x = q1 ** q2
    y = ("exponentiation")
    a = y
print ('Result ',a,' = ',x)
