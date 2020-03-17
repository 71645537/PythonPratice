import math

def Unary(k, b, x):
    y = k * x + b
    return y
def Quadratic(a, b, c, x):
    y = a*x**2 + b*x + c
    return y
#Trig
#Absolute

def main():
    print("Welcome to my first program")
    while(True):
        UserInput = int(input("Please choose a function\n\
        1)Unary\n\
        2)Qudratic\n\
        3)NA\n\
        4)NA\n\
        enter 0 to quit\
        "))
        print(UserInput)
        if (UserInput == 0):
            break
        if (UserInput == 1):
            for i in range(10):
                print("y =", Unary(2,1,i), "when x =", i)
        if (UserInput == 2):
            for i in range(10):
                print("y =", Quadratic(3,1,3,i), "when x =", i)
            break

main()