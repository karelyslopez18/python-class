import csv 
def sc():
    menu = "\n Welcome!\n\n"+\
"1. Sign In\n"+\
"2. Create Account\n"+\
"3. Exit"
    
    inputu=0
    while inputu !=3:
        print(menu)
        inputu = eval(input("Choose an option: "))

        if inputu == 1:
            susr = input('Enter username: ')
            spsw = input('Enter password: ')
            with open('116.csv', newline='') as csvfile:
                user_info = csv.reader(csvfile, delimiter=' ', quotechar='|')
                for row in user_info:
                    if user_info >= 0:
                        if spsw.find(spsw) >= 0:
                            print("Login is successful. Welcome "+susr+"!")
                        else:
                            print("Incorrect Password")
                    else:
                        print("Username does not exist")
    

        if inputu == 2:
            cusr = input('Please create a username: ')
            cpsw = input('Please create a pasword: ')
            with open('116.csv', 'w', newline='') as csvfile:
                user_info = csv.writer(csvfile, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
                user_info.writerow(cusr)
                user_info.writerow(cpsw)
