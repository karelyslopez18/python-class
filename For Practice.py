#STUDENT NAME:
#SECTION:
#DATE:

#def main():
login = input("Enter login name: ") #ask for the user name
user_info=open('users116.txt','r')
alluser=user_info.readlines() # create a list of strings where each line is a item in the list.
#Observe the how the username are arrange in the liST

for line in alluser:
    linet=tuple(line.split(','))
    if login==linet[0]:
        passw = input("Enter password: ")
        if passw+'\n'==linet[1]:
            print("Login successful :)!\n")
            break
        else:
            print("Incorrect password!\n")
            break
#print("User doesn't exist!\n")
    





