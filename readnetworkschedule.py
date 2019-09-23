with open("D:\Vishal\Tactical Solution\CFTO-Network_Schd.txt", "r") as f:
    lineList = f.read().splitlines()
print(len(lineList))
j = 0;
for i in lineList:
    print("Start " + i)
    j += 1;
    if j == 10:
        break
