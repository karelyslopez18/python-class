import random
lottery = []
for i in range(7):
    lotteryNumber = random.randint(0,9)
    lottery.append(lotteryNumber)

print("lottery number is: ",end="")

for element in lottery:
    print(element ,end="")

