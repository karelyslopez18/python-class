
city = open('cuidades.txt', 'r')
city2=city.readlines()
city.close()

name=[] 
dist=[]

for line in city2:
    line=line.strip()
    subline=line.split(',')
    name=subline[0].split('(')
    distance=subline[1].split(')')
    cityname.append(name[1]) 
    citydistance.append(distance[0])

print("The most distant city from San Juan is:")
print(cityname[citydistance.index((citydistance<50))])
