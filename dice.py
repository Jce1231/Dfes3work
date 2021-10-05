import random
def roll(intTimes=1,diceType=6):
    results = []
    for i in range(intTimes):
        results.append(random.randint(1,diceType))
    return(results)

def averageRoll(listRolls):
    averageResult = 0
    for x in listRolls:
        averageResult+=x
    return(averageResult/len(listRolls))

def rollCount(listRolls,diceType=6):
    count = [] #Initialise an empty Array
    for i in range(diceType): #Ensures the array is empty and initialised each index to 0
        count.append(0)
    for x in listRolls:
        count[x-1] +=1
    return(count)