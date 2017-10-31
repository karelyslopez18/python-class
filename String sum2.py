
def initials():
    fullname = input("Enter your First, Middle and last name please:")
    inin = fullname.split()
    print('the initials of', fullname, 'is')
    for x in inin:
        print(x[0] + ".")
