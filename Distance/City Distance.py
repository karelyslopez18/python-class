def closest_city():
    fin = open ("cuidadesSJ.txt","r")
    dic = []
    for line in fin:
        if line != 0:
            dic.append(line)
    print("This city is closes to San Juan: " + str(min(dic)))
 
def farthest_city():
    fin = open ('cuidadesSJ.txt', 'r')
    dic = []
    for line in fin:
        if line != 0:
            dic.append(line)
    print ("This city is the farthest from San Juan: " + str(max(dic)))
