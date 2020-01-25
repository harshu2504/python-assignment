import pickle
class MyApp:
    datastore = { "office" : {"medical":[
    {"room-number":100,"use":"reception","sq-feet":50,"price":75},
    {"room-number":101,"use":"waiting","sq-feet":250,"price":75},
    {"room-number":102,"use":"examination","sq-feet":125,"price":150},
    {"room-number":103,"use":"examination","sq-feet":125,"price":150},
    {"room-number":104,"use":"office","sq-feet":150,"price":100}],
    "parking":{"location":"primium","style":"covered","price":750}}}

    def saveChanges(self):
        choice = input("Do you want to save changes ? Y|N")
        if choice=='Y' or choice=='y':
            infile = open('datastore.dat','wb')
            pickle.dump(self.datastore,infile)
            infile.close()
        elif choice=='N' or choice=='n' :
            print()
        else:
            print("You have selected wrong option")
            saveChanges()
    def createNewFile(self):
        infile = open('datastore.dat','wb')
        pickle.dump(self.datastore,infile)
        infile.close()
        
    def addOffice(self,ofcname,location,style,price):
        self.datastore['office'][ofcname]={'location':location,'style':style,'price':price}

    def displayOfficeNames(self):
        for i in self.datastore['office'].keys():
            print(i)

    def deleteOffice(self,name):
        for i in self.datastore['office'].keys():
            if i==name:
                del self.datastore['office'][i]
            
    def changePriceByRno(self,rno,newp):
        for i in self.datastore['office']['medical']:
            if i['room-number']==rno:
                i['price']=newp

    def changeUseByRno(self,rno,nuse):
        for i in self.datastore['office']['medical']:
            if i['room-number']==rno:
                i['use']=nuse

    def changeAreaByRno(self,rno,newArea):
        for i in self.datastore['office']['medical']:
            if i['room-number']==rno:
                i['sq-feet']=newArea

    def displayMedical(self):
        print("RoomNo.\t  Use\t\t Area\tPrice")
        print("========================================")
        for i in self.datastore['office']['medical']:
            print(i['room-number'],"\t",i['use'],"\t",i['sq-feet'],"\t",i['price'])
        print("========================================")

    def addMedical(self,rno,use,area,price):
        self.datastore['office']['medical'].append({'room-number':rno,"use":use,"sq-feet":area,"price":price})

    def delMedical(self,rno):
        for i in self.datastore['office']['medical']:
            if i['room-number']==rno:
                self.datastore['office']['medical'].remove(i)

    def displayMedicalByRno(self,rno):   
        flag=False
        for i in self.datastore['office']['medical']:
            
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
                
    def show(self):
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

    def start(self):
        self.show()
        choice=int(input())
        if(choice==1):
            rno=input("Enter room no")
            use=input("Enter use of room")
            area=input("Enter size of room")
            price=input("Enter Price of room")
            self.addMedical(rno,use,area,price)
            self.saveChanges()
        elif(choice==2):
            rno=input("Enter room no which you want to delete")
            self.delMedical(rno)
            self.saveChanges()
        elif(choice==3):
            rno=input("Enter room no")
            newp=input("Enter new price of this room")
            self.changePriceByRno(rno,newp)
            self.saveChanges()
        elif(choice==4):
            rno=input("Enter room no")
            narea=input("Enter new Area of this room")
            self.changePriceByRno(rno,narea)
            self.saveChanges()
        elif(choice==5):
            rno=input("Enter room no")
            use=input("Enter new use of this room")
            self.changeUseByRno(rno,use)
            self.saveChanges()
        elif(choice==6):
            rno=input("Enter room no")
            self.displayMedicalByRno(rno)
        elif(choice==7):
            self.displayMedical()
        elif(choice==8):
            ofcname=input("Enter the name of office")
            location=input("Enter the location of office")
            style=input("Enter the style of office")
            price=input("Enter the price of office")
            self.addOffice(ofcname,location,style,price)
            self.saveChanges()
        elif(choice==9):
            ofcname=input("Enter the name of office which you want to delete")
            self.deleteOffice(ofcname)
            self.saveChanges()
        elif(choice==10):
            self.displayOfficeNames()
        else:
            print("Invalid Selection")
        close=input("Are you want to Exit ? Y|N")
        print("\n")
        if close=='N' or close=='n':
            self.start()

m = MyApp()
m.start()
        

    
