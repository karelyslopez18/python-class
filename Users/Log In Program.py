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
            fout = open(“users116.txt","r")
            susr = input('Enter username: ')
            spsw = input('Enter password: ')
            alldata= fout.read()
            if susr.find(susr) >= 0:
                if spsw.find(spsw) >= 0:
                    print("Login is successful. Welcome "+susr+"!")
                else:
                    print("Incorrect Password")
            else:
                print("Username does not exist")
    

        if inputu == 2:
            cusr = input('Please create a username: ')
            cpsw = input('Please create a pasword: ')
            fout = open("116.txt","w")
            fout.write(cusr+","+cpsw+"\n")
            fout.close()
            
