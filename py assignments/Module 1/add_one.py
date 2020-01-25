a=int(input("Enter any Five digit no"))
addone=0
while(a!=0):
    r=a%10
    r=r+1
    addone= addone*10+r
    a=int(a/10)
a=addone
addone=0
while(a!=0):
    r=a%10
    addone= addone*10+r
    a=int(a/10)
print(addone)

