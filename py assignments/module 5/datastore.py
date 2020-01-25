datastore = { "office" : {"medical":[
    {"room-number":100,"use":"reception","sq-feet":50,"price":75},
    {"room-number":101,"use":"waiting","sq-feet":250,"price":75},
    {"room-number":102,"use":"examination","sq-feet":125,"price":150},
    {"room-number":103,"use":"examination","sq-feet":125,"price":150},
    {"room-number":104,"use":"office","sq-feet":150,"price":100}],
    "parking":{"location":"primium","style":"covered","price":750}}}

def addOffice(ofcname,location,style,price):
    datastore['office'][ofcname]={'location':location,'style':style,'price':price}

def displayOfficeNames():
    for i in datastore['office'].keys():
        print(i)

def deleteOffice(name):
    for i in datastore['office'].keys():
        if i==name:
            del datastore['office'][i]
        
def changePriceByRno(rno,newp):
    for i in datastore['office']['medical']:
        if i['room-number']==rno:
            i['price']=newp

def changeUseByRno(rno,nuse):
    for i in datastore['office']['medical']:
        if i['room-number']==rno:
            i['use']=nuse

def changeAreaByRno(rno,newArea):
    for i in datastore['office']['medical']:
        if i['room-number']==rno:
            i['sq-feet']=newArea

def displayMedical():
    print("RoomNo.\t  Use\t\t Area\tPrice")
    print("========================================")
    for i in datastore['office']['medical']:
        print(i['room-number'],"\t",i['use'],"\t",i['sq-feet'],"\t",i['price'])
    print("========================================")

def addMedical(rno,use,area,price):
    datastore['office']['medical'].append({'room-number':rno,"use":use,"sq-feet":area,"price":price})

def delMedical(rno):
    for i in datastore['office']['medical']:
        if i['room-number']==rno:
            datastore['office']['medical'].remove(i)

def displayMedicalByRno(rno):   
    flag=False
    for i in datastore['office']['medical']:
        
        if i['room-number']==int(rno):
            print(rno)
            flag=True
            val=i
            break
    if flag:
        print("RoomNo.\t  Use\t\t Area\tPrice")
        print("========================================")
        print(val['room-number'],"\t",val['use'],"\t",val['sq-feet'],"\t",val['price'])
        print("========================================")
    else:
        print("Record not found")
            
def show():
    print("========================================")
    print("================MENU====================")
    print("========================================")
    print("1. \t Add new room to medical")
    print("2. \t Delete room to medical")
    print("3. \t To change price of any room")
    print("4. \t To change Area of any room")
    print("5. \t To change Use of any room")
    print("6. \t To Search any room detail")
    print("7. \t Display all records of room")
    print("8. \t Add New office")
    print("9. \t Delete office")
    print("10.\t To Display all offices")
    print("========================================")
    print("==========Enter your Choice=============")
    print("========================================")

def start():
    show()
    choice=int(input())
    if(choice==1):
        rno=input("Enter room no")
        use=input("Enter use of room")
        area=input("Enter size of room")
        price=input("Enter Price of room")
        addMedical(rno,use,area,price)
    elif(choice==2):
        rno=input("Enter room no which you want to delete")
        delMedical(rno)
    elif(choice==3):
        rno=input("Enter room no")
        newp=input("Enter new price of this room")
        changePriceByRno(rno,newp)
    elif(choice==4):
        rno=input("Enter room no")
        narea=input("Enter new Area of this room")
        changePriceByRno(rno,narea)
    elif(choice==5):
        rno=input("Enter room no")
        use=input("Enter new use of this room")
        changeUseByRno(rno,use)
    elif(choice==6):
        rno=input("Enter room no")
        displayMedicalByRno(rno)
    elif(choice==7):
        displayMedical()
    elif(choice==8):
        ofcname=input("Enter the name of office")
        location=input("Enter the location of office")
        style=input("Enter the style of office")
        price=input("Enter the price of office")
        addOffice(ofcname,location,style,price)
    elif(choice==9):
        ofcname=input("Enter the name of office which you want to delete")
        deleteOffice(ofcname)
    elif(choice==10):
        displayOfficeNames()
    else:
        print("Invalid Selection")
    close=input("Are you want to Exit ? Y|N")
    print("\n")
    if close=='N' or close=='n':
        start()


start()
        

    
