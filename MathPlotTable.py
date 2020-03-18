import math

def Unary(k, b, x):
    y = k * x + b
    return y
def Quadratic(a, b, c, x):
    y = a*x**2 + b*x + c
    return y
def Trig(a,b,x):
    y = a*math.sin(x)+b*math.sin(x)
    return y
#Absolute

def main():
    TableMax = 10
    print("Welcome to my first program")
    while(True):
        UserInput = int(input("Please choose a function\n\
        1)Unary\n\
        2)Qudratic\n\
        3)Trig\n\
        4)NA\n\
        enter 0 to quit\
        "))
        print(UserInput)
        if (UserInput == 0):
            break
        if (UserInput == 1):
            print("For Unary:")
            for i in range(TableMax):
                print("y =", Unary(2,1,i), "when x =", i)
        if (UserInput == 2):
            print("For Quadratic:")
            for i in range(TableMax):
                print("y =", Quadratic(3,1,3,i), "when x =", i)
        if (UserInput == 3):
            print("For Trig:")
            for i in range(TableMax):
                print("y =", Trig(1,0,i), "when x =", i)

main()