import numpy as np
import matplotlib.pyplot as plt

def Unary(k, b):
    x = np.linspace(-20,20,81)
    y = k * x + b
    return y
def Quadratic(a, b, c):
    x = np.linspace(-20,20,81)
    y = a*x**2 + b*x + c
    return y
def Qubic(a,b,c,d):
    x = np.linspace(-20,20,81)
    y = a*x**3 + b*x**2 + c*x + d
    return y
def Trig(a,b):
    x = np.linspace(-20,20,81)
    y = a*np.sin(x)+b*np.sin(x)
    return y
def Absoulute():
    x = np.linspace(-20,20,81)
    y = np.abs(x)
    return y
def e(a):
    x = np.linspace(-20,20,81)
    y = np.power(np.e, a * x)
    return y
def log(a,b):
    x = np.linspace(-20,20,81)
    y = a*np.log(b * x)
    return y
def plotDiagram(y):
    x = np.linspace(-20,20,81)
    fig,ax = plt.subplots()
    ax.plot(x,y)
    ax.axhline(y=0, color='k')
    ax.axvline(x=0, color='k')
    ax.grid(True, which='both')
    fig.show()

def main():
    print("Welcome to my first program")
    while(True):
        UserInput = int(input("Please choose a function\n\
        1)Unary\n\
        2)Qudratic\n\
        3)Qubic\n\
        4)Trig\n\
        5)Abs\n\
        6)e\n\
        7)log\n\
        enter 0 to quit\
        "))
        print(UserInput)
        if (UserInput == 0):
            break
        if (UserInput == 1):
            print("For Unary:")
            plotDiagram(Unary(2,1))
        if (UserInput == 2):
            print("For Quadratic:")
            plotDiagram(Quadratic(2,1,3))
        if (UserInput == 3):
            print("For Qubic:")
            plotDiagram(Qubic(1,1,1,1))
        if (UserInput == 4):
            print("For Trig:")
            plotDiagram(Trig(2,1))
        if (UserInput == 5):
            print("For Abs:")
            plotDiagram(Absoulute())
        if (UserInput == 6):
            print("For e:")
            plotDiagram(e(-0.1))
        if (UserInput == 7):
            print("For log:")
            plotDiagram(log(2,1))

main()