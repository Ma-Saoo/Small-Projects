import random
import math
import time
#For a better version use classes to create a linked list
#1. Deal your hand
#2. 
def handvaluewithace(list,choice):
    #choice is 1 or 11 for value of A
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
    #choice is 1 or 11 for value of A
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
    time.sleep(0.5)
    initiallist = list
    playerhand=[] #Initialize player hand into empty list
    for i in range(2):
        card=random.choice(list)
        playerhand.append(card)
        list.remove(card)
    print(f"Your hand: {playerhand}")
    time.sleep(0.5)
    computerhand=[]
    for j in range(2):
        card=random.choice(list)
        computerhand.append(card)
        list.remove(card) #Computer gets 2 cards
    #print(f"C Hand is {computerhand}, Deck is {list}")

    continueornot='Yes'
    
    if(handvaluewithace(computerhand,1)==21 or handvaluewithace(computerhand,11)==21):
        if(handvaluewithace(playerhand,1)==21 or handvaluewithace(playerhand,11)==21):
            print("We both have blackjack, its a tie!")
            time.sleep(0.5)
            print(f"Your Hand : {playerhand}")
            time.sleep(0.5)
            print(f"My Hand : {computerhand}")
            continueornot=input("Would you like to play again? (Y/N): ")
            if(continueornot=='Y'):
                blackjack(initiallist)
        if(continueornot=='Yes)'):
            print("Blackjack! I win with 21!")
            time.sleep(0.5)
            print(f"Your Hand : {playerhand}")
            time.sleep(0.5)
            print(f"My Hand : {computerhand}")
            continueornot=input("Would you like to play again? (Y/N): ")
            if(continueornot=='Y'):
                blackjack(initiallist) 
        
    
    if(handvaluewithace(playerhand,1)==21 or handvaluewithace(playerhand,11)==21):
        print("You win with a blackjack 21!")
        time.sleep(0.5)
        print(f"My Hand : {computerhand}")
        continueornot=input("Would you like to play again? (Y/N): ")
        if(continueornot=='Y'):
            blackjack(initiallist) 

    if(continueornot=='Yes'):
        continueornot1='Yes'
        #PLAYER PLAYS
        playerinput=input("Hit or Stand, (H/S): ")
        while(playerinput!='S'):
            card=random.choice(list)
            playerhand.append(card)
            list.remove(card)
            if(handvaluewithace(playerhand,1)==21 or handvaluewithace(playerhand,11)==21):
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
            if(handvaluewithace(playerhand,1)>21 and handvaluewithace(playerhand,11)>21):
                if('A' in playerhand):
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

        if(continueornot1=='Yes'):
            #ALGORITHM FOR HIGHEST COMPUTER WINNING CHANCE:
            #IF MORE THAN 18 STAND
            #IF 17 WITH ACE = 11, HIT
            #IF LESS THAN OR EQUAL TO 17 BUT WITH NO ACE, HIT
            if('A' in computerhand):
                if(6 in computerhand):
                    card=random.choice(list)
                    computerhand.append(card)
                    list.remove(card)
                    
            while(handvalue(computerhand)<16):
                card=random.choice(list)
                computerhand.append(card)
                list.remove(card)
            #COMPUTER HAND DONE

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

        


