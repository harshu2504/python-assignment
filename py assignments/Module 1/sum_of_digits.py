a=int(input("Enter any Five digit no"))

sum=0
while(a!=0):
    r=a%10
    sum = sum + r
    a=int(a/10) 
print(sum)
