import random

#pdb.set_trace()
# Goal: “Create a lottery ball, or Hat, 
# 
# - that takes a variable number of arguments that specify the 
# number of balls of each color that are in the hat. 
# 
# input 1 { red: 6, blue: 10, puce: 3}
# input 2 { mahogany: 5, teal: 23, saddlebrown: 40, mint_green: 1 }
# 

class Hat():
    def __init__(self,**balls):
        self.ballsdict = balls

# create a variable that has the total of each ball
        self.ballBag = []
        for i in self.ballsdict.keys():
            for j in range(self.ballsdict[i]):
                self.ballBag.append(i)

# input 1 [ red red red blue blue blue blue blue blue blue blue blue blue puce puce puce]
# input 2 [ mahogany mahogany mahogany mahogany mahogany teal teal teal teal teal teal teal teal teal teal teal teal teal teal teal teal teal teal teal teal teal teal teal ]

# Give the object the ability to pick a random number of balls 
# from the hat, 
# 
    def grabballs(self):
        randBalls = random.randint(0,len(self.ballBag))
        grabbedBalls = random.sample(self.ballBag, randBalls)
        probGrabber = self.ballBag.copy()
        probGrab = 1
        for i in grabbedBalls:
            probGrab = probGrab * (probGrabber.count(i)/len(probGrabber))
            probGrabber.remove(i)
        return (f"{grabbedBalls} {probGrab}") 



# which will then be used to compute the 
#
# probability of picking a certain distribution of balls ?!?!?
# 
# over a large _number_ of experiments”  <- user input


    def compute_probability(self,experinum):
        experivar = []
        for i in range(experinum):
            experivar.append(self.grabballs())
        return experivar


davethe = Hat(red=6,blue=10,puce=3)
print(davethe.compute_probability(10))