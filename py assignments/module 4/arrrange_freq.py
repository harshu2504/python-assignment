a=[4,4,4,6,6,5]
B={}
rslt=[]
for i in a:
    count=a.count(i)
    B[i]=count
print(a)
print(B.sort())
print(min(B.values()))
print(B.index(min(B.values())))
