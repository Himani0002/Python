'''

1 for snake 
-1 for water
0 for gun

'''

computer = -1

you = int(input("Enter your choice :- "))

youDice={"s":1 ,"w":-1, "g":0}

reverseDict={1:"snake" ,-1 :"water",0 : "gun"}

print(f" you chose {dict[you]}\n Computer chose {reverseDict[computer]}")

if (computer == you):
    print("you a draw")
    
else:

    if(computer == 1 and you == 0):

        print("you Win !")
        
    elif(computer == 0 and you == 1):
        
        print("you Lose !")

    elif(computer == 0 and you == -1):
        
        print("you Lose !")

    elif(computer == -1 and you == 0):
        
        print("you Lose !")
        
    elif(computer == 1 and computer ==-1):

        print("you win !")
        
        
    elif(computer == -1 and computer == 1):

        print("you Lose !")
        
    else: 
        
        print("Something went wrong !")

    
    

    



    

