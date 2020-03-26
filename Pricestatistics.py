data = ""
UserName = ""
NumberOfEntry = 0
RoomCost = 0
ServiceCost = 0
TotalCostPerDay = 0
DaysStaying = 0
TotalCost = 0
TotalAfterDiscount = 0

def Name():
    global UserName
    UserName = input("Please give me your name\n>")

def RoomType():
    global RoomCost
    print("What type of room do you want(number of guests)")
    print(">1 person\n>2 person\n>3 person\n>otherwise for more")
    userInput = int(input("What would you like?\n>"))
    if(userInput==1):RoomCost += 100
    elif(userInput==2):RoomCost += 200
    elif(userInput==3):RoomCost += 300
    else:
            userInput = int(input("How Many?\n>"))
            if userInput <= 3 : userInput += 1
            RoomCost += userInput * 90
def Services():
    global ServiceCost
    if(int(input("Do you need parking\n(1 for yes otherwise for false)\n>")) == 1):
        ServiceCost += 15
    if(int(input("Do you need laundry\n(1 for yes otherwise for false)\n>")) == 1):
        ServiceCost += 10
    if(int(input("Do you need meals\n(1 for yes otherwise for false)\n>")) == 1):
        ServiceCost += 50
def Totals():
    global TotalCostPerDay
    TotalCostPerDay = RoomCost + ServiceCost
    print("Your totals per day would be: ", TotalCostPerDay)

def DayStaying():
    global TotalCost
    global DaysStaying
    userInput = int(input("How many days are you staying?\n>"))
    while(userInput <= 0):
        userInput = int(input("Please enter a valid number\n>"))
    TotalCost = TotalCostPerDay * userInput
    DaysStaying = userInput

def VIP():
    global TotalAfterDiscount
    if(input("Are you a VIP? (yes/no)\n>") == "yes"):
        TotalAfterDiscount = 0.9 * (TotalCost)

def appendData():
    global data
    if(NumberOfEntry == 1):data += "\n===================================\n"
    data += str(NumberOfEntry)
    data += " For " + UserName + "\n"
    data += "    Room Cost            " + str(RoomCost)+ "\n"
    data += "    Service Cost         " + str(ServiceCost) + "\n"
    data += "    Total / day          " + str(TotalCostPerDay) + "\n"
    data += "    Staying for          " + str(DaysStaying) + "\n"
    data += "    Calculated    " + str(DaysStaying) + " * " + str(TotalCostPerDay) + " = " + str(TotalCost)
    if(TotalAfterDiscount != 0):
        data += "\n    After VIP discount... " + str(TotalAfterDiscount)
    data += "\n===================================\n"

def quit():
    global NumberOfEntry
    if(NumberOfEntry==0):
        print("================================================")
        print("==Welcome to the auto price calculation system==")
        print("================================================")
    NumberOfEntry+=1
    userInput = int(input("enter 0 to quit, otherwise to continue:\n>"))
    if(userInput == 0):
        return True
    return False

def main():
    global UserName
    global NumberOfEntry
    global RoomCost
    global ServiceCost
    global TotalCostPerDay
    global DaysStaying
    global TotalCost
    global TotalAfterDiscount
    
    Name()
    RoomType()
    Services()
    Totals()
    DayStaying()
    VIP()
    appendData()
    
    RoomCost = 0
    ServiceCost = 0
    TotalCostPerDay = 0
    DaysStaying = 0
    TotalCost = 0
    TotalAfterDiscount = 0

    return
while(quit() == False):
    print()
    main()

print(data)
