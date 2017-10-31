def sc():
    menu = "\n Welcome!\n\n"+\
"1. Create Account\n"+\
"2. Sign In\n"+\
"3. Exit"
    
    inputu=0
    while inputu !=3:
        print(menu)
        inputu = eval(input("Choose an option: "))
        if inputu==1:
            cusr = input('Please create a username: ')
            cpsw = input('Please create a pasword: ')
            file=open("users116.txt","w")
            file.write(cusr+","+cpsw+"\n")
            file.close()


        if inputu==2:
            found = False
            search= input('Enter username: ')
            search2= input('Enter password: ')
            userpass= open('users116.txt','r')
            descr= userpass.readline()
            i= 
            while descr != '':
                descr= descr.rstrip('\n')
                if descr == search:
                    return (search2)
                elif descr != search:
                    print("Username does not exist")
                elif descr == search2:
                    print("Login is successful. Welcome "+search+"!")
                elif descr != search2:
                    print("Incorrect Password")
                    
                found = True
                descr= userpass.readline()
                userpass.close()
            if not found:
                print('That item was not found in th file.')
                sc()
                
        if inputu==3:
            exit()
        
