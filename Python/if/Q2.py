marks1 = int(input("Enter the Marks 1"))
marks2 = int(input("Enter the Marks 2"))
marks3 = int(input("Enter the Marks 3"))

Total = (100*(marks1+marks2+marks3))/300


if(Total>=40 and marks1>=33 and marks2>=33 and marks3>=33):
    print("You are pass")
else:
    print("You are failed")
