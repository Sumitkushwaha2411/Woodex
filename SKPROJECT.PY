import mysql.connector as c
con=c.connect (host="localhost",
               user="root",
               passwd="4444",
               database="Project")
cursor=con.cursor()
s="create table Telephone_directory(Serial_No int primary key,Name varchar(40),Designation varchar(45),Mobile_No int(100),E_mail_Id varchar(40))"
cursor.execute(s)
con.commit()
s2="create table Telephone_database(USERNAME varchar(30),PASSWORD int(30) primary key)"
cursor.execute(s2)
query="insert into Telephone_directory(Serial_No,Name,Designation,Mobile_No,E_mail_Id)values({},'{}','{}',{},'{}')".format(1,'ANURAG','POLICE OFFICER',123456789,'ANURAG@GMAILCOM')
cursor.execute(query)
query="insert into Telephone_directory(Serial_No,Name,Designation,Mobile_No,E_mail_Id)values({},'{}','{}',{},'{}')".format(2,'BIKAJI','CHEIF EXECUTIVE OFFICER',1234568790,'BIKAJI@GMAILCOM')
cursor.execute(query)
query="insert into Telephone_directory(Serial_No,Name,Designation,Mobile_No,E_mail_Id)values({},'{}','{}',{},'{}')".format(3,'CHINTU','CHEIF TECNOLOGY OFFICER',2134567890,'CHINTU@GMAILCOM')
cursor.execute(query)
query="insert into Telephone_directory(Serial_No,Name,Designation,Mobile_No,E_mail_Id)values({},'{}','{}',{},'{}')".format(4,'DEV','CHEIF PRODUCTION OFFICER',1235467890,'DEV@GMAILCOM')
cursor.execute(query)
query="insert into Telephone_database(USERNAME,PASSWORD)values('{}',{})".format('ABHIJEET KUMAR',1234)
cursor.execute(query)
query="insert into Telephone_database(USERNAME,PASSWORD)values('{}',{})".format('SUMIT KUSHWAHA',5678)
cursor.execute(query)
con.commit()

cursor=con.cursor()
print("-"*65)
print(""*25,end='')
print("                 TELEPHONE DIRECTORY ")
print("-"*65)
print("\n")
cursor=con.cursor()
def telephone_directory_Image():
    print("                 ┌──────────────────┐┐")
    print("                 │                  ││") 
    print("                 │                  ││")
    print("                 │   TELEPHONE      ││")
    print("                 │       DIRECTORY  ││")
    print("                 │                  ││")
    print("                 │                  ││")
    print("                 │     ─────────    ││")
    print("                 └──────────────────┘┘")
    return('')
print(telephone_directory_Image())
def signing():
    print("-------------------")
    print(   "REGISTRATION")
    print("-------------------")
    choice=int(input("1->SIGN IN \n 2->SIGN UP \n 3->DELETE ACCOUNT \n 4->EXIT \n\n ENTER YOUR CHOICE:"))
    while True:
        if choice==2:
            name=input(" ENTER YOUR NAME:")
            paswd=int(input(" ENTER YOUR PASSWORD(NUMERIC):"))
            query="insert into Telephone_database(USERNAME,PASSWORD) values('{}',{})".format(name,paswd)
            cursor.execute(query)
            con.commit()
            print('SUCCESFULLY LOGIN ')
            print("-"*55)
            print(""*25,end='')
            print("       WELCOME TO TELEPHONE DIRECTORY")
            print("-"*55)
            break
            
        
            
        if choice==1:
             name=input(" ENTER YOUR NAME:")
             paswd=int(input(" ENTER YOUR PASSWORD:"))
             query="select * from Telephone_database where USERNAME='{}'and PASSWORD={}".format(name,paswd)
             cursor.execute(query)
             if True:
                 data=cursor.fetchone()
                 print("HII ",data[0])
                 print("-"*55)
                 print(""*25,end='')
                 print("WELCOME TO YOUR TELEPHONE DIRECTORY")
                 print("-"*55)
                 break
                 
             else:
                 print('WRONG USERNAME AND PASSWORD')
        if choice==3:
            if True:
                name=input(" ENTER YOUR NAME:")
                paswd=int(input(" ENTER YOUR PASSWORD:"))
                query="DELETE from Telephone_database where PASSWORD={}".format(paswd)
                cursor.execute(query)
                print("-----------------")
                print("ACCOUNT DELETED")
                print("-----------------")
                print("\n THANKU YOU")
                break
                exit
            else:
                print('WRONG NAME AND PASSWORD')
        if choice==4:
            print("\n THANKU YOU")
            break
            exit

def telephone_directory():
    while True:
        choice=int(input("1->ADD CONTACT\n2->EDIT CONTACT\n3->DISPLAY CONTACT DETAIL\n4->SEARCH CONTACT \n5->DELETE CONTACT \n6->LOG OUT \n ENTER YOUR CHOICE"))
        serialno=5
        print('---------------\n')
        if choice==1:
            serialno+=1   
            name=input("ENTER YOUR NAME:")
            phno=int(input("ENTER YOUR PHONE NUMBER:"))
            designation=input("ENTER YOUR DESIGNATION:")
            Email=input("ENTER YOUR E-MAIL ADDRESS:")
            query="insert into telephone_directory(Serial_No,Name,Designation,Mobile_No,E_mail_Id) values({},'{}','{}',{},'{}')".format(serialno,name,designation,phno,Email)
            cursor.execute(query)
            con.commit()
            print('\n')
            print("--------------------------\n")
            print(  "BOOKED SUCCESSFULLY    ")
            print("YOUR SERIAL NO.=>",serialno,"\n")
            print("--------------------------")
        if choice==2:
             choice=int(input("EDIT CONTACT THROUGH \n 1->PHONE NUMBER \n 2->E-MAIL ADDRESS \n\n ENTER YOUR CHOICE:"))
             if choice==1:
                 phno=int(input("ENTER YOUR PHONE NUMBER:"))
                 print('---------------\n')
                 if True:
                     name=input("ENTER YOUR NAME")
                     designation=input("ENTER YOUR DESIGNATION")
                     pho=int(input("ENTER YOUR MOBILE NUMBER"))
                     email=input("ENTER YOUR E-MAIL")
                     query="UPDATE telephone_directory set Name='{}' where Mobile_NO={}".format(name,phno)
                     cursor.execute(query)
                     query="UPDATE telephone_directory set Designation='{}' where Mobile_NO={}".format(designation,phno)
                     cursor.execute(query)
                     query="UPDATE telephone_directory set Mobile_No={} where Mobile_NO={}".format(pho,phno)
                     cursor.execute(query)
                     query="UPDATE telephone_directory set E_mail_Id='{}' where Mobile_NO={}".format(email,phno)
                     cursor.execute(query)
                     print('-----------------------------\n')
                     print("DETAILS UPDATED SUCCESSFULLY \n")
                     print('-----------------------------')
                     con.commit()
                     
                
             elif choice==2:
                 email=input("ENTER YOUR E-MAIL ADDRESS:")
                 print('---------------\n')
                 if True:
                     name=input("ENTER YOUR NAME")
                     designation=input("ENTER YOUR DESIGNATION")
                     pho=int(input("ENTER YOUR MOBILE NUMBER"))
                     email=input("ENTER YOUR E-MAIL")
                     query="UPDATE telephone_directory set Name='{}' where E_mail_Id='{}'".format(name,email)
                     cursor.execute(query)
                     query="UPDATE telephone_directory set Designation='{}' where E_mail_Id='{}'".format(designation,email)
                     cursor.execute(query)
                     query="UPDATE telephone_directory set Mobile_No={} where E_mail_Id='{}'".format(pho,email)
                     cursor.execute(query)
                     query="UPDATE telephone_directory set E_mail_Id='{}' where E_mail_Id='{}'".format(email,email)
                     cursor.execute(query)
                     print('-----------------------------\n')
                     print("DETAILS UPDATED SUCCESSFULLY \n")
                     print('-----------------------------')
                     con.commit()
                     
        if choice==3:
            serialno=int(input("ENTER YOUR SERIAL NO.:"))
            query="select * from Telephone_directory where Serial_No={}".format(serialno)
            cursor.execute(query)
            ('\n')
            if True:
                    data=cursor.fetchone()
                    print('------------------------------')
                    print("ACCOUNTS DETAILS ARE:\n")
                    print("NAME:         ",data[1])
                    print("DESIGNATION:  ",data[2])
                    print("MOBILE NUMBER:",data[3])
                    print("E-MAIL ADDRESS",data[4])
                    print('------------------------------')
                       
        if choice==4:
            choice1=int(input("SEARCH CONTACT THROUGH \n 1->PHONE NUMBER \n 2->E-MAIL ADDRESS\n ENTER YOUR CHOICE:"))
            if choice1==1:
                phno=int(input("ENTER YOUR PHONE NUMBER:"))
                query1="select * from Telephone_directory where Mobile_NO={}".format(phno)
                cursor.execute(query1)
                print('\n')
                if True:
                    data=cursor.fetchone()
                    print('--------------------------')
                    print("ACCOUNTS DETAILS ARE:\n")
                    print("SERIAL NO.:   ",data[0])
                    print("NAME:         ",data[1])
                    print("DESIGNATION:  ",data[2])
                    print("E-MAIL ADDRESS:",data[4])
                    print('--------------------------')
                    
            elif choice1==2:
                email=input("ENTER YOUR E-MAIL ADDRESS:")
                query="select * from Telephone_directory where E_mail_Id='{}'".format(email)
                cursor.execute(query)
                print('---------------\n')
                if True:
                    data=cursor.fetchone()
                    print('--------------------------')
                    print("ACCOUNTS DETAILS ARE:\n")
                    print("SERIAL NO.:   ",data[0])
                    print("NAME:         ",data[1])
                    print("DESIGNATION:  ",data[2])
                    print("MOBILE NUMBER:",data[3])
                    print('--------------------------')
                   
                else:
                    print("ACCOUNTS DETAILS ARE NOT FOUND")
                 
        if choice==5:
            phno=int(input("ENTER YOUR PHONE NUMBER:"))
            query="DELETE from Telephone_directory where Mobile_No={}".format(phno)
            cursor.execute(query)
            print('\n')
            print('--------------------------')
            print("DETAILS DELETED SUCCESSFULLY")
            print('--------------------------')
        if choice==6:
            print("THANK YOU")
            break
            exit
while True:
    print(signing())
    if True:
        print(telephone_directory())
         
            


