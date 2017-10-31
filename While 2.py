#STUDENT NAME:
#SECTION:
#DATE:

#def main():
login = input("Enter login name: ") #ask for the user name
user_info=open('users116.txt','r')
alluser=user_info.readlines() # create a list of strings where each line is a item in the list.
#Observe the how the username are arrange in the liST
l=len(alluser)
flag=0
C=0
line=user_info.readline()
while C<l:
    linet=tuple(alluser[C].split(','))
    C=C+1
    if login==linet[0]:
        flag=1
        passw = input("Enter password: ")
        if passw+'\n'==linet[1]:
            print("Login successful: )!\n")
        else:
            print("Incorrect password!\n")
         
if flag==0:
    print("User doesn't exist!\n")

user_info.close()


