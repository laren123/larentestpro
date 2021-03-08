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
            create()
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
    for i in u:
        print("%10s"%i[0],"%10s"%i[1])
    mainmenu()

def mainmenu():
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
        time.sleep(2)
        sys.exit()
    if ch==945:
        display()

def newacc():
    global db
    name=input("Name:")
    username=input("Username:")
    passwd=input("Password:")
    email=input("Email:")
    password=hash(passwd)
    cur=db.cursor()
    cur.execute("insert into auth values('%s', '%s', '%s', '%s');"%(name, username, password, email))
    cur.commit()
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
        cur.commit()
        mainmenu()
    mainmenu()

def delete(username):
    global db
    cur=db.cursor()
    Confirm=input("Are You Sure You Want To Delete?(Y/n):")
    if Confirm.lower()=='y':
        cur.execute("delete from auth where Username=%s;"%(username))
        cur.commit()
        print("Your account is Deleted..")
        mainmenu()
    else:
        control(username)
def log_time():
	time=datetime.datetime.now()
	return time

def create():
    global db
    cur=db.cursor()
    cur.execute("create table auth (Name varchar(30) NOT NULL, Username varchar(30) NOT NULL UNIQUE, Password varchar(500) NOT NULL, Email varchar(60));")
    cur.commit()
    cur.execute("create table time (Username varchar(30) NOT NULL, Time varchar(28) NOT NULL);")
    cur.commit()

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
    out=cur.fetchone()
    if out[0]==password:
        enter(user)
        control(user)
        return True
    else:
        print ("Not Correct..")

def enter(username="Unknown"):
    global db
    cur=db.cursor()
    time=log_time()
    cur.execute("insert into time value('%s', '%s');"%(username, time))
    cur.commit()

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
            print("Closing the program..")
            print("Please wait..")
            time.sleep(2)
            sys.exit()
db=connect()
mainmenu()


