import pickle
alist=[]
class Contact:
    # name phoneNo email
    def __init__(self,name,phone,email):
        self.__name=name
        self.__phone=phone
        self.__email=email        
    def set_name(self,newname):
        self.__name=newname
    def set_phone(self,newphone):
        self.__phone=newphone
    def set_email(self,newemail):
        self.__email=newemail
    def get_name(self):
        return self.__name
    def get_phone(self):
        return self.__phone
    def get_email(self):
        return self.__email
    def __str__(self):
        return f'Name of person is : {self.__name} \nPhone of Person is: {self.__phone} \nEmail of person is {self.__email}\n'

def view():
    print("========================================")
    print("================MENU====================")
    print("========================================")
    print("1. \t Display Records")
    print("2. \t Add an new Record")
    print("3. \t Change an Existing Record")
    print("4. \t Delete a Record")
    print("5. \t Exit")
    print("========================================")
    print("==========Enter your Choice=============")
    print("========================================")

def saveData(content):
    outfile =open('contact.dat','wb')
    pickle.dump(content,outfile)
    outfile.close()

def readData():
    infile = open('contact.dat','rb')
    content=dict(pickle.load(infile))
    infile.close()
    return content
     
def addRecord():
    content={}
    rno=int(input("Enter the Roll number"))
    name=input("Enter the name")
    phone=int(input("Enter the no"))
    email=input("Enter the email")
    c=Contact(name,phone,email)
    content=readData()
    content[rno]=c
    saveData(content)

def diplayRecords():
    content=readData()
    if content!=None:
        print("Rno\t  Name\t\t  Phone\t\t\tEmail")
        for id,val in content.items():
            print(id,"\t",val.get_name(),"\t",val.get_phone(),"\t",val.get_email())
    else:
        print("no records found !!!!")

def deleteRecord():
    rno=int(input("Enter the roll no to delete its record"))
    readData()
    del content[rno]
    saveData(content)
def change():
    rno=int(input("Enter the roll no to delete its record"))
    content=readData()
    for i in content.keys():
        if i==rno:
            break
    changeoption(content,i)

def changeoption(content,item):
    print("Which change do you want")
    print("3.1 \t Change Name\n3.2 \t Change Phone\n3.3 \t Change Email")
    choice=int(input())
    if choice ==1:
        name=input("Enter new Name")
        content[item].set_name(name)
        saveData(content)
    elif choice==2:
        phone=int(input("Enter new Phone"))
        content[item].set_phone(phone)
        saveData(content)
    elif choice==3:
        email=input("Enter new Email")
        content[item].set_email(email)
        saveData(content)
    else:
        print("Invalid selection")
        changeopetion(content,item)

   
def main():
    try:
        view()
        choice=int(input())
        if choice!=5 :
            if choice==1:
                diplayRecords()
            elif choice==2:
                addRecord()
            elif choice==3:
                change()
            elif choice==4:
                deleteRecord()
            else:
                print("Invalid choice")
                main()
        c=input("Are you want to Exit ? Y|N")
        if c=='Y' or c!='y':
            main()
    except ValueError:
        print("ERROR : Hour worked and hourly pay rate must")
        print("be valid numbers")

main()
