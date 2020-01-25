import pickle
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

def main():
    name=input("Enter Name")
    phone=int(input("Enter Phone"))
    email=input("Enter Email")
    c = Contact(name,phone,email)
    infile=open("Contact.dat",'ab')
    pickle.dump(c,infile)
    infile.close()

main()
outfile = open('Contact.dat','rb')
detail = pickle.load(outfile)
print(detail)
outfile.close()

