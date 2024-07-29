
f=open("po.txt")
content = f.read()

if("Gold" in content):
    print("The Word Gold is present in content")    
else:
    print("The Word Gold is not present in content")

f.close()