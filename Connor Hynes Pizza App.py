import time
from datetime import datetime
import random

#MODULE IMPORTS
print ("Hello and Welcome to the Pizza App where you can order the best pizza ever!")
print ("We are a small buisness and we tried our hardest so please bear with us if our app is clunky or not")
time.sleep(1)
def main():
    

    """Pizza Application which returns all the values as a list"""



    topcount = 0
    topinsert = 1
    toplist = [] 
    #USED FOR TOPPINGS

    cost = 0
    deliver = random.choice([15, 30, 45, 60])
    minuteover = 0
    dellist = []
    #USED FOR DELIVERY TIME

    addlist = []
    the = [] #EMPTY LIST WHICH WE WILL PUT SOME STUFF IN TO BE RETURNED AT THE END
    #LOCAL VARIABLES

    size = str(input("What is the size of our pizza? (L for Large, M for Medium, and S for Small) "))
    size = size.lower()
    picked = False #THIS IS USED FOR STUFF THAT REQUIRES TO BE PICKED MULTIPLE TIMES
    while picked != (True): #WHILST PICKED IS NOT TRUE
        if size == ("l"):
            print("You have picked a Large pizza")
            cost = cost + 20
            picked = True
        elif size == ("m"):
            print("You have picked a Medium pizza")
            cost = cost + 13
            picked = True
        elif size == ("s"):
            print("You have picked a Small pizza")
            cost = cost + 5
            picked = True
        else:
            print("That is not an option. ")
            size = str(input("What is the size of our pizza? "))
            size = size.lower()
    the.insert(0, size) #WHATEVER SIZE IS
    picked = False
    print ("Now onto the fun part toppings.")
    time.sleep(1)
    print ("We have four options Pepperoni (1.25), Jalapeños (0.75), Mushrooms (0.50), Sausage (1.75), and additional options for extra cheese and sauce (1.50 and 1.30)")
    time.sleep(2)
    toppings = str(input("What kind of toppings should we get? (P for Pepperoni, J for Jalapeño, M for Mushroom, S for sausage, C for more Cheese, and Sa for more Sauce. Type in d to finish) "))
    toppings = toppings.lower()
    while picked != (True):
        if toppings == ("p"):
            print("You have added Pepperoni")
            topcount = topcount + 1
            cost = cost + 1.25
            toplist.insert(topinsert, toppings)
            topinsert = topinsert + 1
            toppings = str(input("What kind of toppings should we get? (P for Pepperoni, J for Jalapeño, M for Mushroom, S for sausage, C for more Cheese, and Sa for more Sauce. Type in d to finish) "))
            toppings = toppings.lower()
        elif toppings == ("j"):
            print ("You have added Jalapeños")
            topcount = topcount + 1
            cost = cost + 0.75
            toplist.insert(topinsert, toppings)
            topinsert = topinsert + 1
            toppings = str(input("What kind of toppings should we get? (P for Pepperoni, J for Jalapeño, M for Mushroom, S for sausage, C for more Cheese, and Sa for more Sauce. Type in d to finish) "))
            toppings = toppings.lower()
        elif toppings == ("m"):
            print ("You have added Mushrooms")
            topcount = topcount + 1
            cost = cost + 0.50
            toplist.insert(topinsert, toppings)
            topinsert = topinsert + 1
            toppings = str(input("What kind of toppings should we get? (P for Pepperoni, J for Jalapeño, M for Mushroom, S for sausage, C for more Cheese, and Sa for more Sauce. Type in d to finish) "))
            toppings = toppings.lower()
        elif toppings == ("s"):
            print ("You have added Sausage")
            topcount = topcount + 1
            cost = cost + 1.75
            toplist.insert(topinsert, toppings)
            topinsert = topinsert + 1
            toppings = str(input("What kind of toppings should we get? (P for Pepperoni, J for Jalapeño, M for Mushroom, S for sausage, C for more Cheese, and Sa for more Sauce. Type in d to finish) "))
            toppings = toppings.lower()
        elif toppings == ("s"):
            print ("You have added Sausage")
            topcount = topcount + 1
            cost = cost + 1.75
            toplist.insert(topinsert, toppings)
            topinsert = topinsert + 1
            toppings = str(input("What kind of toppings should we get? (P for Pepperoni, J for Jalapeño, M for Mushroom, S for sausage, C for more Cheese, and Sa for more Sauce. Type in d to finish) "))
            toppings = toppings.lower()
        elif toppings == ("c"):
            print ("You have added extra Cheese")
            topcount = topcount + 1
            cost = cost + 1.50
            toplist.insert(topinsert, toppings)
            topinsert = topinsert + 1
            toppings = str(input("What kind of toppings should we get? (P for Pepperoni, J for Jalapeño, M for Mushroom, S for sausage, C for more Cheese, and Sa for more Sauce. Type in d to finish) "))
            toppings = toppings.lower()
        elif toppings == ("sa"):
            print ("You have added extra Sauce")
            topcount = topcount + 1
            cost = cost + 1.30
            toplist.insert(topinsert, toppings)
            topinsert = topinsert + 1
            toppings = str(input("What kind of toppings should we get? (P for Pepperoni, J for Jalapeño, M for Mushroom, S for sausage, C for more Cheese, and Sa for more Sauce. Type in d to finish) "))
            toppings = toppings.lower()
        elif toppings == ("pineapple"):
            print ("no")
            time.sleep(2.5)
            toppings = str(input("What kind of toppings should we get? (P for Pepperoni, J for Jalapeño, M for Mushroom, S for sausage, C for more Cheese, and Sa for more Sauce. Type in d to finish) "))
            toppings = toppings.lower()
        elif toppings == ("d"):
            toplist.insert(0, topcount)
            if topcount == 0:
                print("Wow you cheapskate!")
                toplist.insert(1, "nt")
            the = the + [toplist]
            picked = True
            time.sleep(1)
        else:
            print("That is not a valid option")
            toppings = str(input("What kind of toppings should we get? (P for Pepperoni, J for Jalapeño, M for Mushroom, S for sausage, C for more Cheese, and Sa for more Sauce. Type in d to finish) "))
            toppings = toppings.lower()
    print("Now please give us a delivery address")
    time.sleep(1)
    address = str(input("Please type an address (or something stupid if you want) "))
    addlist.insert(0, address)
    the.insert(2, addlist)
    hour = int(input("Could you please give me the time in Hours? ")) #HOUR USED FOR DELIVERY
    hbd = hour #HOUR BEFORE DELIVERY
    minute = int(input("Could you also give me the time in Minutes? ")) #MINUTE USED FOR DELIVERY
    mbd = minute #MINUTES BEFORE DELIVERY
    minuteover = minute + deliver
    time.sleep(1)
    while mbd >= 60:
        hbd = hbd + 1
        mbd = round(mbd - 60, 2)

    while hbd > 12:
        hbd = hbd - 12
        if hbd == 0:
            hbd = hbd + 1

    while minuteover >= 60:
        hour = hour + 1
        minuteover = round(minuteover - 60, 2)

    while hour > 12:
        hour = hour - 12
        if hour == 0:
            hour = hour + 1

    print("Your Pizza should be here at around {}:{}".format(hour, minuteover))
    dellist.insert(0, hbd)
    dellist.insert(1, mbd)
    dellist.insert(2, hour)
    dellist.insert(3, minuteover)
    the = the + dellist
    roundedcost = round(cost, 2)
    the.insert(7, roundedcost)
    return the

        
result = main()
counter = result[1][0]
accum = 1
gstno = result[7]
gst = round(gstno * 1.05, 2)
receipt = False
while receipt == False:
    print ("""---------------------------------------------------
    RECEIPT
---------------------------------------------------""")
    if result[0] == "s":
       print("\tSmall Pizza\t 5.00")
       result[0] = "a"
    elif result[0] == "m":
        print("\tMedium Pizza\t 13.00")
        result[0] = "a"
    elif result[0] == "l":
        print("\tLarge Pizza\t 20.00")
        result[0] = "a"
    print ("""---------------------------------------------------
    TOPPINGS
---------------------------------------------------""")
    while accum != counter + 1:
        if result[1][accum] == "p":
            print("Pepperoni\t 1.25")
            result[1][accum] = "a"
            accum = accum + 1
            
        elif result[1][accum] == "j":
            print("Jalapeños\t 0.75")
            result[1][accum] = "a"
            accum = accum + 1
        
        elif result[1][accum] == "m":
            print("Mushrooms\t 0.50")
            result[1][accum] = "a"
            accum = accum + 1

        elif result[1][accum] == "s":
            print("Sausage\t\t 1.75")
            result[1][accum] = "a"
            accum = accum + 1

        elif result[1][accum] == "c":
            print("Cheese\t\t 1.50")
            result[1][accum] = "a"
            accum = accum + 1

        elif result[1][accum] == "sa":
            print("Sauce\t\t 1.30")
            result[1][accum] = "a"
            accum = accum + 1
        
        elif result[1][accum] == "nt":
            print("No Toppings\t 0.00")
            result[1][accum] = "a"
            accum = accum + 1
    print("""---------------------------------------------------
    Time Ordered: {}:{}
    Estimate time of Arrival: {}:{}
---------------------------------------------------""".format(result[3], result[4], result[5], result[6]))
    print("""---------------------------------------------------
    TO BE DELIVERED TO: {}
---------------------------------------------------""".format(result[2][0]))
    print("""---------------------------------------------------
    COST: {}
---------------------------------------------------""".format(gst))
    receipt = True
time.sleep(3)
print("Thank you for using our Pizza Program")
print("We hoped you enjoy it and order from our place again!")