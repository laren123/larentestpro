#importing all necessary modules
import hashlib
import datetime
import time
import sys
import mysql.connector as sql


def connect():
    """Creating a connection with Database"""
    db=sql.connect(host="localhost", user="root", password="pass", database="test")
    if db.is_connected==False:      #verify wheather connection has establised
        print ("Not connected..")
        print ("Exiting..")
        time.sleep(2)
        sys.exit()
    else:
        print ("Connected to DB")
        try:
            create(db)
            print ("Ready to use...")
        except:
            print ("Please wait..")
    return db

def display():
    global db
    con=db.connect()
    cur=db.cursor()
    cur.execute("select * from auth;")
    u=cur.fetchall()
    print("%10s"%"Name","%10s"%"Username","%10s"%"Email","%20s"%"Password")
    for i in u:
        print("%10s"%i[0],"%10s"%i[1],"%10s"%i[3],"%20s"%i[2])
    cur.execute("select * from time;")
    u=cur.fetchall()
    print("%10s"%"Username","%10s"%"Time")
    for t in u:
        print("%10s"%t[0],"%10s"%t[1])
    mainmenu()

def mainmenu():
    global db
    print ("1- Login")
    print ("2- New Account")
    print ("3- Exit")
    ch=int(input(">"))

    if ch==1:
        login()
    if ch==2:
        newacc()
    if ch==3:
        print("Exiting")
        db.close()
        time.sleep(2)
        sys.exit()
    if ch==945:
        display()
def log_time():
    print(datetime.datetime.now())
    time1=time.ctime(time.time())
    return time1

def newacc():
    global db
    name=input("Name:")
    username=input("Username:")
    passwd=input("Password:")
    email=input("Email:")
    password=hash(passwd)
    cur=db.cursor()
    cur.execute("insert into auth values('%s', '%s', '%s', '%s');"%(name, username, password, email))
    db.commit()
    print("Successfully created!")
    mainmenu()

def update_pass(username):
    global db
    cur=db.cursor()
    passwd=input("New Password:")
    check=str(input("Confirm Password:"))
    if passwd==check:
        password=hash(passwd)
        cur.execute("update auth set Password='%s' where Username='%s';"%(password, username))
        db.commit()
        mainmenu()
    mainmenu()

def delete(username):
    global db
    cur=db.cursor()
    Confirm=input("Are You Sure You Want To Delete?(Y/n):")
    if Confirm.lower()=='y':
        cur.execute("delete from auth where Username='%s';"%(username))
        db.commit()
        print("Your account is Deleted..")
        mainmenu()
    else:
        control(username)

def create(db):
    cur=db.cursor()
    cur.execute("create table auth (Name varchar(30) NOT NULL, Username varchar(30) NOT NULL UNIQUE, Password varchar(500) NOT NULL, Email varchar(60));")
    db.commit()
    cur.execute("create table time (Username varchar(30) NOT NULL, Time varchar(60) NOT NULL);")
    db.commit()

def hash(item):
    """SHA-512 password digest algorithm"""
    try:
        return hashlib.sha512(item.encode("utf-8")).hexdigest()
    except:
        return ''

def login():
    global db
    user=input("Username:")
    passwd=input("Password:")
    password=hash(passwd)
    cur=db.cursor()
    cur.execute("select Password from auth where Username='%s';"%user)
    out=cur.fetchall()
    for i in out:
        if i[0]==password:
            enter(user)
            control(user)
            return True
        else:
            print ("Not Correct..")
    #except:
     #   print("Incorrect Username.")
    mainmenu()
    

def enter(username="Unknown"):
    global db
    cur=db.cursor()
    time1=log_time()
    cur.execute("insert into time value('%s', '%s');"%(username, time1))
    db.commit()

def control(user):
    global db
    while True:
        print ("1) Delete your account")
        print ("2) Update password")
        print ("3) Exit")
        c=int(input(">"))
        if c==1:
            delete(user)
            mainmenu()
        if c==2:
            update_pass(user)
        if c==3:
            print("Please wait..")
            time.sleep(2)
            mainmenu()
db=connect()
mainmenu()


