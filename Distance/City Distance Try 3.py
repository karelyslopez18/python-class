# open the file for reading
city = open("ciudadesSJ.txt", "r")

#read the contents of the file into a list-each line in file will be an item in the list
info=city.readlines()

# once the content of the file in a list you can close de file
#close file
city.close()

#create empty lists to save the name of the cities and distances 
cityname=[] 
citydistance=[]

#extract information from each line in info
for line in info:
    line=line.strip()
    subline=line.split(',')
    name=subline[0].split('(')
    distance=subline[1].split(')')
    cityname.append(name[1]) # contains the name of the cities
    citydistance.append(int(distance[0])) # contains the distances of the cities and uses the function int to convert the values to integer. 

print("The most distant city from San Juan is:")
print(cityname[citydistance.index(max(citydistance))] + ' ' + str(max(citydistance)) + 'km') #observe that the maximum distance is obtained from a list of integers and str is chaning it to string to display it using print

print("The closest city to San Juan is:")
print(cityname[citydistance.index(min(citydistance))] + ' ' + str(min(citydistance)) + 'km') #observe that the minimum distance is obtained from a list of integers and str is chaning it to string to display it using print


