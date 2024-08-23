import mysql.connector as sq
con=sq.connect(host="localhost", user="root", passwd="star")
def start():
     print("                      Welcome to our E-Library                            ")
     print("Press 1 for Admin \nPress 2 for Client\n ")
     x=int(input("Enter your key: "))
     if x==1:
          admn()
     elif x==2:
          psswd()
     else:
          print("wrong key")
def admn():
     pw=input("Enter the Admin Password: ")
     if pw=='admn123':
          cu=con.cursor()
          cu.execute("show databases;")
          m=cu.fetchall()
          if ("library",) in m:
               print("Database already exist\n>-------------------------------------------------------------------------------------<")
               adpswd()
          else:
               cu.execute("create database library")
               cu.execute("use library")
               cu.execute("create table addbook(bcode varchar(10) primary key, bname varchar(30), author varchar(30), total int)")
               cu.execute("create table issuebook(regno varchar(10) primary key, name varchar(30), bcode varchar(10) references addbook(bcode), issue date)")
               cu.execute("create table submitbook(regno varchar(10) primary key, name varchar(30), bcode varchar(10) references addbook(bcode), submission date)")
               print("Database created\n")
               con.commit()
               adpswd()
     else:
          print("Wrong Password")
          admn()
               
def adpswd():
     cu=con.cursor()
     cu.execute("use library")
     homead()
     
def psswd():
     cu=con.cursor()
     cu.execute("use library")
     ps=input("Enter the User Password: ")
     if ps=='py123':
          homecl()
     else:
          print("Wrong Password")
          psswd()
def homead():        
    print("""
            ----------------------------------------------------------------
                             !!Welcome to our e-Library!!
            ----------------------------------------------------------------
                         
                  * * * * * * * * * * * * * * * * * * * * * * * * * * *
                  *                 LIBRARY MANAGER                   *
                  * * * * * * * * * * * * * * * * * * * * * * * * * * *
                  *                                                   *
                  *               1. Add Book                         *
                  *               2. Issue Book                       *
                  *               3. Submit Book                      *
                  *               4. Delete Book                      * 
                  *               5. Display Book                     * 
                  *                                                   *
                  * * * * * * * * * * * * * * * * * * * * * * * * * * *                 """)
    ch=int(input("Press your key:"))
    if ch==1:
          addbook()
    elif ch==2:
          issuebook()
    elif ch==3:
          submitbook()
    elif ch==4:
          deletebook()
    elif ch==5:
         print(" 1.All  2.Issued ")
         t=int(input("Enter the choice:"))
         if t==1:
               das()
         else:
              dis()
    else:
         print("Wrong choice.......")
         homead()

def homecl():        
    print("""
               ----------------------------------------------------------------
                                   Welcome to our e-Library!!
               ----------------------------------------------------------------
                         
                      * * * * * * * * * * * * * * * * * * * * * * * * * * *
                      *               !!LIBRARY MANAGER!!                 *
                      * * * * * * * * * * * * * * * * * * * * * * * * * * *
                      *                                                   *
                      *               1. Issue Book                       *
                      *               2. Submit Book                      *
                      *               3. Display Book                     *
                      *                                                   *
                      * * * * * * * * * * * * * * * * * * * * * * * * * * *                 """)
    ch=int(input("Press your key:"))
    if ch==1:
          issuebook()
    elif ch==2:
          submitbook()
    elif ch==3:
         print(" 1.All  2.Issued ")
         t=int(input("Enter the choice:"))
         if t==1:
               das()
         else:
              dis()
    else:
         print("Wrong choice.......")
         homecl()

         
def addbook():
     bkcd=input("Enter the book code here: ")
     bknm=input("Enter the book name here: ")
     autr=input("Enter the author name here: ")
     tno=int(input("Enter the total no of  books: ")) #
     cu=con.cursor()
     st="insert into addbook values('{}','{}','{}',{})"
     cu.execute(st.format(bkcd,bknm,autr,tno))
     con.commit()
     print(">---------------------------------------------------------------<")
     print("\t\tData entered sucessfully!!")
     import os
     os.system('cls')
     homead()
     
     
def issuebook():
     regno=input("Enter the Reg. No: ")
     sw=input("Enter the Name: ")
     bkcd=input("Enter the book code here: ")
     d=input("Enter Date: ")
     cu=con.cursor()
     si="insert into issuebook values('{}','{}','{}','{}')"
     cu.execute(si.format(regno,sw,bkcd,d))
     con.commit()
     print("This book is issued to:",sw)
     print("\t>---------------------------------------------------------------<")
     updb(bkcd,-1)
     homecl()

def submitbook():
     regno=input("Enter the Reg. No: ")
     sw=input("Enter the Name: ")
     bkcd=input("Enter the book code here: ")
     d=input("Enter Date: ")
     cu=con.cursor()
     si="insert into submitbook values('{}','{}','{}','{}')"
     cu.execute(si.format(regno,sw,bkcd,d))
     h="delete from issuebook where regno='{}'"
     cu.execute(h.format(regno))
     con.commit()
     print("This book is submitted by:",sw)
     print("\t>--------------------------------------------------------------<")
     updb(bkcd,1)
     homecl()
     
def updb(bkcd,u):
     cu=con.cursor()
     c="select total from addbook where bcode='{}'"
     cu.execute(c.format(bkcd))
     my=cu.fetchone()
     t=my[0]+u
     d="update addbook set total={} where bcode='{}'"
     cu.execute(d.format(t,bkcd))
     con.commit()
     homead()
     
def deletebook():
     bc=input("Enter the book code here: ")
     d="delete from addbook where bcode='{}'"
     cu=con.cursor()
     cu.execute(d.format(bc))
     con.commit()
     print("The Book is removed from the table")
     homead()
    
def das():
     ar="select * from addbook"
     cu=con.cursor()
     cu.execute(ar)
     db=cu.fetchall()
     print("List of Books")
     print("-"*80)
##     print("Bcode\t\tBname\t\tAuthor\t\tTotal")
     print("-"*80)
     for i in db:
          v=list(i)
          k=["Bcode","Bname","Author","Total"]
          dt=dict(zip(k,v))
          
          print(dt)
##          print(i[0],"\t",i[1],"\t",i[2],"\t",i[3])
     homecl()

def dis():
     ir="select * from issuebook"
     cu=con.cursor()
     cu.execute(ir)
     db=cu.fetchall()
     print("Record of Issued Books")
     rg=input("Enter the reg. no of student:")
     print("-"*98)
     for i in db:
          if i[0]==rg:
               print("Reg.No :",i[0])
               print("Name :",i[1])
               print("Bcode :",i[2])
               print("Issued Date :",i[3])
     print("-"*98)
     
     homecl()     
start()     
      
