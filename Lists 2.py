numbersl = []
print("the 20 numbers in a list ")
for i in range(20):
    print("Enter the number ",(i + 1),": ",sep="",end="")
    numbers = int(input(""))
    numbersl.append(numbers)

total = 0
for element in numbersl:
    total += element
averageNumbers = total / 20
print("The lowest :",min(numbersl))
print("The highest  :",max(numbersl))
print("The total: ",format(total,',.2f'),sep="")
print("The average : ",format(averageNumbers,',.2f'),sep="")
