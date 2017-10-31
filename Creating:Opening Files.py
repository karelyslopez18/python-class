

fout = open("students.txt","w")

fout.write("Ned\n")
fout.write("Bob\n")
fout.write("Jil\n")
fout.close()

fout= open("students.txt", "r")
line= fout.readline()
print('Line:', line)
fout.close()

fout= open("students.txt", "r")
alldata = fout.read()
print("All data:")
print(alldata)
fout.close()

fout= open("students.txt", "r")
count=0
for line in fout:
    count=count+1
    if count==2:
        print(line.strip())
fout.close()
print('amount of lines:', count)

fout= open("C:\Users\Karelys\Documents\CIIC3011")



