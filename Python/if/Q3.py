p1="Make a lot of money"

p2="buy now"

p3="subscribe this"

message=input("Enter your comment :- ")

if((p1 in message or p2 in message or p3 in message )):
    
    print("This comment is a spam")

else :
    
    print("This comment is not a spam")