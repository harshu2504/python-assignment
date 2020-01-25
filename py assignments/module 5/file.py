def write():
    outfile = open('abc.txt','w')
    outfile.write('Hello\n')
    outfile.write('This ')
    outfile.write('is\n')
    outfile.write('Aditya')
    outfile.close()
    print("File has been writted")

def read():
    infile = open('abc.txt','r')
    content = infile.read()
    infile.close()
    print(content)

def append(string):
    apfile = open('abc.txt','a')
    apfile.write(string)
    apfile.close()
    print("File has been rewritted\n")

def readByLine():
    infile= open('abc.txt','r')
    line = infile.readline()
    print(line,end='')
    while line!='':
        #convert line to a float
        #amount=float(line)
        #read lines from the file
        line = infile.readline()
        print(line,end='')
    infile.close()
 
readByLine()
        


    
