with open("teams.txt",'w') as file:
    varString = "Liverpool\nManchester\nHolland\nBrazil\nSheffield\n"
    file.write(varString)
with open("teams.txt") as file:
    varList = file.readlines()
    print(varList[0])
    print(varList[3])


with open("teams.txt",'r') as file:
    varString = "This is a new line \n"
    varList = file.readlines()
    for i in varList:
        varString += i
with open("teams.txt",'w') as file:
    file.write(varString)

with open("teams.txt") as file:
    for i in file.readlines():
        print(i)