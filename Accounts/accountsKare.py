#accounts.csv must be in C://
import csv

def createAcct(username, password):
    try:
        with open('accounts.csv', 'a', newline='') as csvfile:
            fw = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
            fw.writerow([username, password])
            print("Account was successfully created.")
    except FileNotFoundError as e:
        print("Please create an account file first.")

def verifyAcct(username, password):
    with open('accounts.csv','r') as csvIn:
        csvInRead = csv.DictReader(csvIn)
        found = False
        for row in csvInRead:
            if(row['username'] == username):
                found = true
                if(row['password'] == password):
                    print("\nWelcome back " + username + "!\n")
                else:
                    print("\nPassword is not correct!\n")
        if(found != True):
            print("\nUsername does not exist.\n")

def main():
    menu = "\n Welcome!\n\n 1. Sign In\n 2. Create Account\n 3. Exit\n"
    inputu = 0
    while inputu != 3:
        print(menu)
        inputu = eval(input("Choose an option: "))

        if(inputu == 1):
            susr = input('Enter username: ')
            spsw = input('Enter password: ')
            try:
                verifyAcct(susr,spsw)
            except FileNotFoundError as e:
                print("\nPlease create an account file first.\n")
        elif(inputu == 2):
            cusr = input('Please create a username: ')
            cpsw = input('Please create a pasword: ')
            createAcct(cusr,cpsw)
        elif(inputu == 3):
            print("\nThank you for using the system. System will close now.\n")
            exit()
        else:
            print("\nInvalid selection. Try again.\n")

if __name__ == '__main__':
    main()
