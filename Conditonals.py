devs_money = 100
dev_can_play_smash = False
if devs_money > 10 and dev_can_play_smash:
    print("Dev enters a smash tournament!")
elif devs_money < 10 and dev_can_play_smash:
    print("Dev is too poor to enter")
else:
    print("Dev just can't play smash")


intMark = int(input("Please enter your mark: "))
if intMark >=85:
    print("Distintion, Good job")
elif intMark >= 65:
    print("Pass, congrats dude")
else:
    print("Fail, sorry man")

if intMark >= 85:
    print("Distinction, Congrats dude!")
if intMark >=65 and intMark <85:
    print("Pass, good job!")
if intMark < 65:
    print("Fail, sorry my guy")
