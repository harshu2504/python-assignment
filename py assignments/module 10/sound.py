import winsound
n=str(input("Enter the no."))
m=0
for i in n:
    p=len(n)-m
    q='0'*(p-1)
    i=i+''+q+'.wav'
    winsound.PlaySound(i,winsound.SND_NOSTOP) #we have files of sound name as 1.wav , 2.wav , 3.wav ......  100.wav , 200.wav , 300.wav , 1000.wav , 2000.wav etc 
    m+=1
        


        
    
        
        

