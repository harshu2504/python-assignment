a=int(input("Enter any Five digit no"))
rev=0
while(a!=0):
    r=a%10
    rev= rev*10+r
    a=int(a/10)
print(rev)
