rainfallList = []
print("rainfall for each month of the year ")
for i in range(12):
    print("rainfall of the month ",(i + 1),": ",sep="",end="")
    storeRainfall = float(input(""))
    rainfallList.append(storeRainfall)


total = 0
for element in rainfallList:
    total += element
averageRainfall = total / 12
print("total rainfall: ",format(total,',.2f'),sep="")
print("average rainfall : ",format(averageRainfall,',.2f'),sep="")
print("highest railfall: ",max(rainfallList))
print("lowest railfall: ",min(rainfallList))
