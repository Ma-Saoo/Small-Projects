import random

def montyhall(iteration):
    wins=0
    losses=0
    for i in range(iteration):
        prizes=['car','goat','xbox']
        a = random.choice(prizes)
        door_1 = a
        prizes.remove(a)
        b = random.choice(prizes)
        door_2 = b
        prizes.remove(b)
        c = random.choice(prizes)
        door_3 = c
        prizes.remove(c)
        doors=[door_1,door_2,door_3]# list of doors

        guess = random.choice(doors)# player randomly guess a door
        doorsthatarenotcar=[]# list of doors that does not lead to a car
        for i in range(len(doors)):
            if(doors[i]!='car'):
                doorsthatarenotcar.append(doors[i])
        #If the player's initial door guess leads to the car, then the host just chooses any of the 2 doors to open from list doorsthatarenotcar
        if(guess=='car'):
            hosttellsthatthisdoorisntcar=random.choice(doorsthatarenotcar)
        #If the player's initial door guess does not have a car, then the host MUST choose the door 
        #that does NOT contain the car nor the door that the player initially guessed
        if(guess!='car'):
            for i in range (len(doors)):
                if(doors[i]!='car' and doors[i]!=guess):
                    hosttellsthatthisdoorisntcar=doors[i]

        #Switch guess
        for i in range(len(doors)):
            if(doors[i]!=guess and doors[i]!=hosttellsthatthisdoorisntcar):
                new_guess=doors[i]
        
        #Uncomment for the win probability without switching guesses
        if(new_guess=='car'):
            wins+=1
        else:
            losses+=1

    print(f"In Monty Hall Problem, Win percentage is: {100*wins/iteration}% and loss is {100*losses/iteration}%")

def hundredprisoners(iteration):
    wins=0
    losses=0

    for i in range(iteration):
        prisoners_win=0
        drawer=[]
        onetohundred=[]
        for a in range(1,101):
            onetohundred.append(a)
        for b in range(100):
            number=random.choice(onetohundred)
            drawer.append(number)
            onetohundred.remove(number)

        for k in range(1,101):
            temp=k
            for c in range(50):
                if(drawer[temp-1]==k):
                    prisoners_win+=1
                    break
                else:
                    temp = drawer[temp-1]
        if(prisoners_win==100):
            wins+=1
        else:
            losses+=1
    print(f"In Hundred Prisoners Problem, Win percentage is: {100*wins/iteration}% and loss is {100*losses/iteration}%")
        
        
if __name__=='__main__':
    montyhall(100000)
    hundredprisoners(5000)
