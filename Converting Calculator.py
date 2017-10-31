#Conversion Calculator by Karelys Lopez Rivera
def mtok(x):
    return (x*1.609)
def ktom(x):
    return (x/1.609)
def ptok(x):
    return (x*.45359237)
def ktop(x):
    return (x*2.2046244202)
def ctof(x):
    return (x*9/5.0)+32
def ftoc(x):
    return (x-32)*5/9
def mhtokh(x):
    return (x*1.609344)
def khtomh(x):
    return (x*0.62137119223733)
def get_uinput():
    uinput = 0
    while type(uinput) != type(1.0):
        uinput = eval(input("Enter value: "))
        try:
            uinput = float(uinput)
        except:
            print (uinput + " is not a valid entry")
    return uinput

def ConvCal():
    menu = "\n Welcome to unit conversion program. Please, choose an option: \n\n"+\
"1. Miles to Kilometers\n"+\
"2. Kilometers to Miles\n"+\
"3. Pounds to Kilograms\n"+\
"4. Kilograms to Pounds\n"+\
"5. Celsuis to Fahrenheit\n"+\
"6. Faherenheir ro Celsuis\n"+\
"7. Miles/hour to Kilometers/hour\n"+\
"8. Kilometers/hour to Miles/hour\n"+\
"9. Exit"
    
    uinput = 0
    while uinput != 9:
        print (menu)
        user_input = eval(input("Please enter an option: "))
        try:
            uinput = int(user_input)
        except:
            print (uinput + " is not a valid selection, please try again\n")
        if user_input == 1:
            x = get_uinput()
            print (str(x) + " miles is " + str((mtok(x))) + " in kilometers")
        elif uinput == 2:
            x = get_uinput()
            print (str(x) + " kilometers is " + str((ktom(x))) + " in miles")
        elif uinput == 3:
            x = get_uinput()
            print (str(x) + " pounds is " + str((ptok(x))) + " in kilograms")
        elif uinput == 4:
            x = get_uinput()
            print (str(x) + " kilograms is " + str((ktop(x))) + " in pounds")
        elif uinput == 5:
            x = get_uinput()
            print (str(x) + " celsuis degree is " + str((ctof(x))) + " in degree fahrenheit")
        elif uinput == 6:
            x = get_uinput()
            print (str(x) + " fahrenheit degree is " + str((ftoc(x))) + " in degree celsuis")
        elif uinput == 7:
            x = get_uinput()
            print (str(x) + " miles/hour is " + str((mhtokh(x))) + " in kilometers/hour")
        elif uinput == 8:
            x = get_uinput()
            print (str(x) + " kilometers/hour is " + str((khtomh(x))) + " in miles/hour")
        elif uinput == 9:
            quit()
        else:
            print (str(uinput) + " is not a legal selection, please try again\n")
