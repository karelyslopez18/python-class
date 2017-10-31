saleList = []
for i in range(7):
    print("store sale of the day",(i + 1),": ",sep="",end="")
    storeSale = float(input(""))
    saleList.append(storeSale)
total= 0

for element in saleList:
    total += element
    
print("total sales for the week : ",format(total,',.2f'),sep="")
