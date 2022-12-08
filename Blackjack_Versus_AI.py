import random
import math
import time



def handvaluewithace(list,choice):
#Count the value of a hand containing an ACE
    value=0
    for i in range(len(list)):
        if(list[i]=='J' or list[i]=='Q' or list[i]=='K'): #JQK are 10
            value += 10
        elif(list[i]!='A'): #Numbers are numbers themselves
            value += list[i]
        else:
            if(choice==1):
                value += 1
            elif(choice==11):
                value += 11
    return value

def handvalue(list):
#Count the value of a hand not containing an ACE
    value=0
    for i in range(len(list)):
        if(list[i]=='J' or list[i]=='Q' or list[i]=='K'): #JQK are 10
            value += 10
        elif(list[i]=='A'):
            value+= 11
        else:
            value += list[i]
    return value

def blackjack(list):

    #Initialize Player and Computer Hands

    time.sleep(0.5)
    initiallist = list #Saves the unaltered deck for recursion when the player wants to play again
    playerhand=[]
    for i in range(2):
        card=random.choice(list) #Draw random card
        playerhand.append(card)
        list.remove(card)        #Remove that card from the deck
    print(f"Your hand: {playerhand}")#Show initial hand
    time.sleep(0.5)
    computerhand=[]
    for j in range(2):
        card=random.choice(list)
        computerhand.append(card)
        list.remove(card)

    #Automatic wins or loses or ties if player or computer or both have 21 from the 2 draws

    continueornot='Yes' #So that the rest of the code does not execute if recursive part is executed
    
    if(handvaluewithace(computerhand,1)==21 or handvaluewithace(computerhand,11)==21): #If initial hand is 21:
        if(handvaluewithace(playerhand,1)==21 or handvaluewithace(playerhand,11)==21): #If both hands are 21, tie automatically
            print("We both have blackjack, its a tie!")
            time.sleep(0.5)
            print(f"Your Hand : {playerhand}")
            time.sleep(0.5)
            print(f"My Hand : {computerhand}")
            continueornot=input("Would you like to play again? (Y/N): ")
            if(continueornot=='Y'):
                blackjack(initiallist) #Recurse with the unaltered list

        if(continueornot=='Yes)'):
            print("Blackjack! I win with 21!") #Only computer hand is 21
            time.sleep(0.5)
            print(f"Your Hand : {playerhand}")
            time.sleep(0.5)
            print(f"My Hand : {computerhand}")
            continueornot=input("Would you like to play again? (Y/N): ")
            if(continueornot=='Y'):
                blackjack(initiallist) 
        
    
    if(handvaluewithace(playerhand,1)==21 or handvaluewithace(playerhand,11)==21): #Only initial player hand is 21, win automatically
        print("You win with a blackjack 21!")
        time.sleep(0.5)
        print(f"My Hand : {computerhand}")
        continueornot=input("Would you like to play again? (Y/N): ")
        if(continueornot=='Y'):
            blackjack(initiallist) 

    #If no one got 21 immediately, then continue the game and execute the rest of the code

    if(continueornot=='Yes'):
        continueornot1='Yes'

        #PLAYER PLAYS
        playerinput=input("Hit or Stand, (H/S): ")
        while(playerinput!='S'):
            card=random.choice(list)
            playerhand.append(card)
            list.remove(card)
            if(handvaluewithace(playerhand,1)==21 or handvaluewithace(playerhand,11)==21):# If player gets 21, win immediately
                print(f"Your hand: {playerhand}")
                time.sleep(0.5)
                print("You win with a blackjack 21!")
                time.sleep(0.5)
                print(f"Your Hand : {playerhand}")
                time.sleep(0.5)
                print(f"My Hand : {computerhand}")
                time.sleep(0.5)
                continueornot1=input("Would you like to play again? (Y/N): ")
                if(continueornot1=='Y'):
                    blackjack(initiallist) 
                break
            if(handvaluewithace(playerhand,1)>21 and handvaluewithace(playerhand,11)>21):# If player busts, lose immediately
                if('A' in playerhand):# If there is an Ace, a hand could have 2 values, one with Ace = 1 and the other with Ace = 11
                    print(f"Your hand: {playerhand}")
                    time.sleep(0.5)
                    print(f"You have {handvaluewithace(playerhand,1)} or {handvaluewithace(playerhand,11)}, Bust! You Lose!")
                    print(f"My Hand : {computerhand}")
                    time.sleep(0.5)
                else:
                    print(f"Your hand: {playerhand}")
                    time.sleep(0.5)
                    print(f"You have {handvalue(playerhand)}, Bust!, You Lose!")
                    print(f"My Hand : {computerhand}")
                    time.sleep(0.5)
                time.sleep(0.5)
                continueornot1=input("Would you like to play again? (Y/N): ")
                if(continueornot1=='Y'):
                    blackjack(initiallist) 
                break
            print(f"Your hand: {playerhand}")
            
            playerinput=input("Hit or Stand, H/S: ")
        #PLAYER FINISHES

        if(continueornot1=='Yes'): #If player does not get 21 nor bust after their play, continue the game and execture the rest of the code
            #COMPUTER PLAYS
            if('A' in computerhand):
                if(6 in computerhand):
                    card=random.choice(list)
                    computerhand.append(card)
                    list.remove(card)
                    
            while(handvalue(computerhand)<16):
                card=random.choice(list)
                computerhand.append(card)
                list.remove(card)
            #COMPUTER FINISHES

            #WIN OR LOSE???
            time.sleep(0.5)
            if('A' in playerhand or 'A' in computerhand):
                if(handvaluewithace(computerhand,1)>21 and handvaluewithace(computerhand,11)>21):
                    print(f"I have {handvalue(computerhand)}, I went bust..., You Win!")
                else:
                    #No one went bust with both ace values,thus:
                    if(handvaluewithace(playerhand,11)<=21):
                        playerhandvalue = handvaluewithace(playerhand,11)
                    else:
                        playerhandvalue = handvaluewithace(playerhand,1)
                    if(handvaluewithace(computerhand,11)<=21):
                        computerhandvalue = handvaluewithace(computerhand,11)
                    else:
                        computerhandvalue = handvaluewithace(computerhand,1)
                    if(computerhandvalue>playerhandvalue):
                        print(f"My {computerhandvalue} beats your {playerhandvalue}, You Lose!")
                    elif(computerhandvalue<playerhandvalue):
                        print(f"Your {playerhandvalue} beats my {computerhandvalue}, You Win!")
                    elif(computerhandvalue==playerhandvalue):
                        print(f"I have {computerhandvalue} and you have {playerhandvalue}, so its a draw!")

            else:
                if(handvalue(playerhand)>21):
                    print(f"You have {handvalue(playerhand)}, Bust! You Lose!")
                elif(handvalue(computerhand)>21):
                    print(f"I have {handvalue(computerhand)}, I went bust..., You Win!")
                elif(handvalue(computerhand)>handvalue(playerhand)):
                    print(f"My {handvalue(computerhand)} beats your {handvalue(playerhand)}, You Lose!")
                elif(handvalue(computerhand)<handvalue(playerhand)):
                    print(f"Your {handvalue(playerhand)} beats my {handvalue(computerhand)}, You Win!")
                elif(handvalue(computerhand)==handvalue(playerhand)):
                    print(f"I have {handvalue(computerhand)} and you have {handvalue(playerhand)}, so its a draw!")
            time.sleep(0.5)
            print(f"Your Hand : {playerhand}")
            print(f"My Hand : {computerhand}")
            #play again or no
            user=input("Do you want to play again Y/N : ")
            if(user=='Y'):
                blackjack(initiallist)


if __name__ == '__main__' :
    deck = [2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,8,8,8,8,9,9,9,9,10,10,10,10,'J','J','J','J','Q','Q','Q','Q','K','K','K','K','A','A','A','A']
    blackjack(deck)

        


