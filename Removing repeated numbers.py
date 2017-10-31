L=[1,2,3,4,5,6,7,8,9]
L2=[11,2,3,5,12,34]
counter=0
for i in L:
    for j in L2:
        if i==j:
            counter=counter+1
            print(i)
print("The amount of repeated number is", counter)

def deleter():
    for i in L:
      for j in L2:
          if i==j:
              del(j)
    return (L+L2)
      
