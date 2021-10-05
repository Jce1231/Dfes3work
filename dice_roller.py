import dice

#roll some dice
roll_times = int(input("Please enter how many times you want to roll the dice: "))
roll_Type = int(input("Please enter what type of dice to roll: "))
rolledNum = dice.roll(roll_times,roll_Type)
for i in range (roll_times):
    print("The result from dice roll",i+1,"is",rolledNum[i])


rollAccumulate = dice.rollCount(rolledNum,roll_Type)
totalRolls = 0
for i in range(roll_Type):
    print(f"The times {i+1} was rolled is {rollAccumulate[i]} ")
    totalRolls+=rollAccumulate[i]
print(f"The total rolls is :{totalRolls}")
print(f"The average dice roll is {dice.averageRoll(rolledNum)}")