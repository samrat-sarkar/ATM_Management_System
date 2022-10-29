from tkinter import *
from tkinter import messagebox
import mysql.connector

# Database Connection ###################################################
try:
    conn = mysql.connector.connect(user='root', password='', host='127.0.0.1', database='bank')
except Exception as e:
    if "Can't connect to MySQL server" in str(e):
        messagebox.showerror("Error", '''Unable to Connect Database
Please Turn ON SQL Server''')
        exit()
    elif "Unknown database" in str(e):
        messagebox.showerror("Error", "Unable to Find Database in Your Server")
        exit()
    elif "Access denied for user" in str(e):
        messagebox.showerror("Error", '''Unable to Login Database Server
Incorrect username or password ''')
        exit()
    elif "Unknown MySQL server host" in str(e):
        messagebox.showerror("Error", '''Unable to Connect Database
Unknown Host ''')
        exit()
# Database Connection ###################################################

# Temp ###################################################
My_AC_No = 0
My_IFSC = ''
My_Name = ''
My_PIN = 0
My_Balance = 0
Phone_Number = 0
Email = ''
# Temp ###################################################

# Request Records ###########################################
def Request_Records():
    try:
        cursor = conn.cursor()
        query = "select My_AC_No from atm"
        cursor.execute(query)
        result = cursor.fetchone()
        for i in result:
            global My_AC_No
            My_AC_No = i
        query = "select My_IFSC from atm"
        cursor.execute(query)
        result = cursor.fetchone()
        for i in result:
            global My_IFSC
            My_IFSC = i
        query = "select My_Name from atm"
        cursor.execute(query)
        result = cursor.fetchone()
        for i in result:
            global My_Name
            My_Name = i
        query = "select My_PIN from atm"
        cursor.execute(query)
        result = cursor.fetchone()
        for i in result:
            global My_PIN
            My_PIN = i
        query = "select My_Balance from atm"
        cursor.execute(query)
        result = cursor.fetchone()
        for i in result:
            global My_Balance
            My_Balance = i
        query = "select Phone_Number from atm"
        cursor.execute(query)
        result = cursor.fetchone()
        for i in result:
            global Phone_Number
            Phone_Number = i
        query = "select Email from atm"
        cursor.execute(query)
        result = cursor.fetchone()
        for i in result:
            global Email
            Email = i

    except Exception as e:
        print(e)
        if "doesn't exist" in str(e):
            messagebox.showerror("Error", "Table Doesn't Exist in Your Database")
            exit()
        elif "Unknown column 'My_AC_No'" in str(e):
            messagebox.showerror("Error", "`My_AC_No` Column Doesn't Exist in Your Table")
            exit()
        elif "Unknown column 'My_IFSC'" in str(e):
            messagebox.showerror("Error", "`My_IFSC` Column Doesn't Exist in Your Table")
            exit()
        elif "Unknown column 'My_Name'" in str(e):
            messagebox.showerror("Error", "`My_Name` Column Doesn't Exist in Your Table")
            exit()
        elif "Unknown column 'My_PIN'" in str(e):
            messagebox.showerror("Error", "`My_PIN` Column Doesn't Exist in Your Table")
            exit()
        elif "Unknown column 'My_Balance'" in str(e):
            messagebox.showerror("Error", "`My_Balance` Column Doesn't Exist in Your Table")
            exit()
        elif "Unknown column 'Phone_Number'" in str(e):
            messagebox.showerror("Error", "`Phone_Number` Column Doesn't Exist in Your Table")
            exit()
        elif "Unknown column 'Email'" in str(e):
            messagebox.showerror("Error", "`Email` Column Doesn't Exist in Your Table")
            exit()
# Request Records ###########################################

# Switch Windows ###########################################
def StartTK():
    global Tkt
    Tkt = Tk()

def Go_to_Deposit():
    Tkt.destroy()
    StartTK()
    Deposit()

def Go_to_Withdrawal():
    Tkt.destroy()
    StartTK()
    Withdrawal()

def Go_to_Pin_Change():
    Tkt.destroy()
    StartTK()
    Pin_Change()

def Go_to_Balance_Inquiry():
    Tkt.destroy()
    StartTK()
    Balance_Inquiry()

def Go_to_Home():
    Tkt.destroy()
    StartTK()
    Home()

def Go_To_Login():
    Tkt.destroy()
    StartTK()
    Login()
# Switch Windows ###########################################

# Processes ###########################################
def Deposit_Amt():
    DAmount = Creamt.get()
    Request_Records()
    if (len(DAmount) <= 0):
        messagebox.showwarning("Warning","Enter Any Amount")
        entry1.delete(0, 'end')
    elif (int(DAmount) % 100 != 0):
        messagebox.showwarning("Warning","Enter Amount in Multiple of 100")
        entry1.delete(0, 'end')
    else:
        Total = int(My_Balance) + int(DAmount)
        cursor = conn.cursor()
        cursor.execute("update atm set My_Balance=%s WHERE My_PIN='%s' " % (Total, My_PIN))
        conn.commit()
        Request_Records()
        entry1.delete(0, 'end')
        messagebox.showinfo("Balance", "Account Balance : ₹" + str(My_Balance))
        Go_To_Login()

def Debit():
    WAmount = Debamt.get()
    Request_Records()
    if (len(WAmount) <= 0):
        messagebox.showwarning("Warning", "Enter Any Amount")
        entry1.delete(0, 'end')
    elif (int(WAmount) % 100 != 0):
        messagebox.showwarning("Warning", "Enter Amount in Multiple of 100")
        entry1.delete(0, 'end')
    elif (int(WAmount) >= int(My_Balance)):
        messagebox.showwarning("Warning", "Insufficient Balance")
        entry1.delete(0, 'end')
    else:
        Bank_Charge = 10;
        Total = Bank_Charge + int(WAmount)
        Remaining = int(My_Balance) - Total
        cursor = conn.cursor()
        cursor.execute("update atm set My_Balance=%s WHERE My_PIN='%s' " % (Remaining, My_PIN))
        conn.commit()
        Request_Records()
        messagebox.showinfo("Sucess","Transaction Successful")
        entry1.delete(0, 'end')
        messagebox.showinfo("Balance", "Account Balance : ₹"+str(My_Balance))
        Go_To_Login()

def Update_PIN():
    A = OldPin.get()
    B = NewPin.get()
    C = CnfPin.get()

    if not A:
        messagebox.showwarning("Warning","Enter Old PIN")
    elif not B:
        messagebox.showwarning("Warning","Enter New PIN")
    elif not C:
        messagebox.showwarning("Warning","Enter Confirm New PIN")
    else:
        if len(A) > 0 and len(A) < 4:
            messagebox.showwarning("Warning","Enter 4-Digits Old PIN")
            entry1.delete(0, 'end')
        elif len(A) > 4:
            messagebox.showwarning("Warning","Incorrect Old PIN")
            entry1.delete(0, 'end')
        elif len(B) > 0 and len(B) < 4:
            messagebox.showwarning("Warning","Enter 4-Digits New PIN")
            entry2.delete(0, 'end')
        elif len(B) > 4:
            messagebox.showwarning("Warning","Enter 4-Digits New PIN")
            entry2.delete(0, 'end')
        elif len(C) > 0 and len(C) < 4:
            messagebox.showwarning("Warning","Enter 4-Digits Confirm New PIN")
            entry3.delete(0, 'end')
        elif len(C) > 4:
            messagebox.showwarning("Warning","Enter 4-Digits Confirm New PIN")
            entry3.delete(0, 'end')
        else:
            if int(A) != int(My_PIN):
                messagebox.showwarning("Warning","Incorrect Old PIN")
                entry1.delete(0, 'end')
            else:
                if int(B) != int(C):
                    messagebox.showwarning("Warning","Confirm PIN Does Not Match")
                    entry2.delete(0, 'end')
                    entry3.delete(0, 'end')
                elif int(B) == int(C):
                    Np = int(B)
                    cursor = conn.cursor()
                    cursor.execute("update atm set My_PIN=%s WHERE My_PIN='%s' " % (Np, My_PIN))
                    conn.commit()
                    messagebox.showinfo("Sucess","PIN Has Been Successfully Changed")
                    Go_To_Login()


def MatchPIN():
    PIN = pin.get()
    Request_Records()
    if (int(PIN) == int(My_PIN)):
        Go_to_Home()
    else:
        entry1.delete(0, 'end')
        messagebox.showwarning("Warning", "INCORRECT PIN")

def CheckCredentials():
    PIN = pin.get()
    if len(str(PIN)) != 0:
        chk = 0
        try:
            PIN = int(PIN)
            chk = 1
        except:
            entry1.delete(0, 'end')
            messagebox.showwarning("Warning", "INCORRECT PIN")

        if chk == 1:
            if len(str(PIN)) >= 0 and len(str(PIN)) < 4:
                entry1.delete(0, 'end')
                messagebox.showwarning("Warning", "ENTER 4-Digit PIN")
            elif len(str(PIN)) > 4:
                entry1.delete(0, 'end')
                messagebox.showwarning("Warning", "INCORRECT PIN")
            elif len(str(PIN)) == 4:
                MatchPIN()
            else:
                messagebox.showwarning("Error", "Something Went Wrong !")
    elif len(str(PIN)) == 0:
        messagebox.showwarning("Warning", "ENTER 4-Digit PIN")

# Processes ###########################################

# Window ###########################################
def Deposit():
    Request_Records()
    bg = PhotoImage(file="bg.png")
    bgimg = Label(Tkt, image=bg)
    bgimg.place(x=0, y=0)
    Tkt.title("ATM Management System")
    Tkt.iconbitmap('icon.ico')
    Tkt.geometry("600x400")
    lable1 = Label(Tkt, text="Money Deposit", borderwidth=8, relief="groove", bg='#EF7D00', fg='black',font=('Courier', 25, 'bold'))
    lable1.pack(pady=10)
    lable2 = Label(Tkt, text="Enter Amount", fg='black', font=('Courier', 15, 'bold'))
    lable2.pack(pady=10)
    global Creamt
    Creamt = StringVar()
    global entry1
    entry1 = Entry(Tkt, width=8, bg="#fbf8f7", fg="black", bd=5, justify='center', textvariable=Creamt,font=('Courier', 20, 'bold'))
    entry1.pack(pady=0)
    button1 = Button(Tkt, command=Deposit_Amt, width=20, text="Deposit", bg="black", bd=3, fg="white",font=('Courier', 15, 'bold'))
    button1.pack(pady=10)
    button2 = Button(Tkt, command=Go_to_Home, width=20, text="Back", bg="black", bd=3, fg="white",font=('Courier', 15, 'bold'))
    button2.pack(pady=10)
    Tkt.eval('tk::PlaceWindow . center')
    Tkt.state('zoomed')
    Tkt.resizable(False, False)
    Tkt.mainloop()

def Withdrawal():
    Request_Records()
    bg = PhotoImage(file="bg.png")
    bgimg = Label(Tkt, image=bg)
    bgimg.place(x=0, y=0)
    Tkt.title("ATM Management System")
    Tkt.iconbitmap('icon.ico')
    Tkt.geometry("600x400")
    lable1 = Label(Tkt, text="Money Withdrawal", borderwidth=8, relief="groove", bg='#EF7D00', fg='black',font=('Courier', 25, 'bold'))
    lable1.pack(pady=10)
    lable2 = Label(Tkt, text="Enter Amount", fg='black', font=('Courier', 15, 'bold'))
    lable2.pack(pady=10)
    global Debamt
    Debamt = StringVar()
    global entry1
    entry1 = Entry(Tkt, width=8, bg="#fbf8f7", fg="black", bd=5, justify='center', textvariable=Debamt,font=('Courier', 20, 'bold'))
    entry1.pack(pady=0)
    button1 = Button(Tkt, command=Debit, width=20, text="Withdrawal", bg="black", bd=3, fg="white",font=('Courier', 15, 'bold'))
    button1.pack(pady=10)
    button2 = Button(Tkt, command=Go_to_Home, width=20, text="Back", bg="black", bd=3, fg="white",font=('Courier', 15, 'bold'))
    button2.pack(pady=10)
    Tkt.eval('tk::PlaceWindow . center')
    Tkt.state('zoomed')
    Tkt.resizable(False, False)
    Tkt.mainloop()

def Pin_Change():
    Request_Records()
    bg = PhotoImage(file="bg.png")
    bgimg = Label(Tkt, image=bg)
    bgimg.place(x=0, y=0)
    Tkt.title("ATM Management System")
    Tkt.iconbitmap('icon.ico')
    Tkt.geometry("600x400")
    lable1 = Label(Tkt, text="PIN Change", borderwidth=8, relief="groove", bg='#EF7D00', fg='black',font=('Courier', 25, 'bold'))
    lable1.pack(pady=10)
    lable2 = Label(Tkt, text="Enter Old PIN ", fg='black', font=('Courier', 15, 'bold'))
    lable2.pack(pady=0)
    global OldPin
    OldPin = StringVar()
    global entry1
    entry1 = Entry(Tkt, width=4, bg="#fbf8f7", fg="black", bd=5, justify='center', textvariable=OldPin, show="*",font=('Courier', 20, 'bold'))
    entry1.pack(pady=20)
    lable3 = Label(Tkt, text="New PIN ", fg='black', font=('Courier', 15, 'bold'))
    lable3.pack(pady=0)
    global NewPin
    NewPin = StringVar()
    global entry2
    entry2 = Entry(Tkt, width=4, bg="#fbf8f7", fg="black", bd=5, justify='center', textvariable=NewPin, show="*",font=('Courier', 20, 'bold'))
    entry2.pack(pady=20)
    lable4 = Label(Tkt, text="Confirm New PIN ", fg='black', font=('Courier', 15, 'bold'))
    lable4.pack(pady=0)
    global CnfPin
    CnfPin = StringVar()
    global entry3
    entry3 = Entry(Tkt, width=4, bg="#fbf8f7", fg="black", bd=5, justify='center', textvariable=CnfPin, show="*",font=('Courier', 20, 'bold'))
    entry3.pack(pady=20)
    button1 = Button(Tkt, command=Update_PIN, width=20, text="Change", bg="black", bd=3, fg="white",font=('Courier', 15, 'bold'))
    button1.pack(pady=10)
    button2 = Button(Tkt, command=Go_to_Home, width=20, text="Back", bg="black", bd=3, fg="white",font=('Courier', 15, 'bold'))
    button2.pack(pady=10)
    Tkt.eval('tk::PlaceWindow . center')
    Tkt.state('zoomed')
    Tkt.resizable(False, False)
    Tkt.mainloop()

def Balance_Inquiry():
    Request_Records()
    bg = PhotoImage(file="bg.png")
    bgimg = Label(Tkt, image=bg)
    bgimg.place(x=0, y=0)
    Tkt.title("ATM Management System")
    Tkt.iconbitmap('icon.ico')
    Tkt.geometry("600x400")
    lable1 = Label(Tkt, text="Balance Inquiry", borderwidth=8, relief="groove", bg='#EF7D00', fg='black',font=('Courier', 25, 'bold'))
    lable1.pack(pady=10)
    lable2 = Label(Tkt, text="Account Holder Name : " + str(My_Name), fg='black', font=('Courier', 15, 'bold'))
    lable2.pack(pady=1)
    lable3 = Label(Tkt, text="Account Number : " + str(My_AC_No), fg='black', font=('Courier', 15, 'bold'))
    lable3.pack(pady=1)
    lable4 = Label(Tkt, text="Account IFSC : " + str(My_IFSC), fg='black', font=('Courier', 15, 'bold'))
    lable4.pack(pady=1)
    lable5 = Label(Tkt, text="Phone Number : " + str(Phone_Number), fg='black', font=('Courier', 15, 'bold'))
    lable5.pack(pady=1)
    lable6 = Label(Tkt, text="Email ID : " + str(Email), fg='black', font=('Courier', 15, 'bold'))
    lable6.pack(pady=1)
    lable7 = Label(Tkt, text="Balance : ₹" + str(My_Balance), fg='black', font=('Courier', 15, 'bold'))
    lable7.pack(pady=1)
    button1 = Button(Tkt, command=Go_to_Home, width=20, text="Back", bg="black", bd=3, fg="white",font=('Courier', 15, 'bold'))
    button1.pack(pady=10)
    Tkt.eval('tk::PlaceWindow . center')
    Tkt.state('zoomed')
    Tkt.resizable(False, False)
    Tkt.mainloop()

def Home():
    bg = PhotoImage(file="bg.png")
    bgimg = Label(Tkt, image=bg)
    bgimg.place(x=0, y=0)
    Tkt.title("ATM Management System")
    Tkt.iconbitmap('icon.ico')
    Tkt.geometry("600x400")
    lable1 = Label(Tkt, text="ATM Management System", borderwidth=8, relief="groove", bg='#EF7D00', fg='black',font=('Courier', 30, 'bold'))
    lable1.pack(pady=20)
    lable2 = Label(Tkt, text="Welcome " + My_Name, fg='black', font=('Courier', 25, 'bold'))
    lable2.pack(pady=1)
    button1 = Button(Tkt,command=Go_to_Balance_Inquiry, width=20, text="Balance Inquiry", bg="black", bd=3, fg="white",font=('Courier', 15, 'bold'))
    button1.pack(pady=10)
    button2 = Button(Tkt,command=Go_to_Pin_Change, width=20, text="PIN Change", bg="black", bd=3, fg="white",font=('Courier', 15, 'bold'))
    button2.pack(pady=10)
    button3 = Button(Tkt,command=Go_to_Withdrawal, width=20, text="Withdrawal", bg="black", bd=3, fg="white",font=('Courier', 15, 'bold'))
    button3.pack(pady=10)
    button4 = Button(Tkt,command=Go_to_Deposit, width=20, text="Deposit", bg="black", bd=3, fg="white", font=('Courier', 15, 'bold'))
    button4.pack(pady=10)
    Tkt.eval('tk::PlaceWindow . center')
    Tkt.state('zoomed')
    Tkt.resizable(False, False)
    Tkt.mainloop()

def Login():
    bg = PhotoImage(file="bg.png")
    bgimg = Label(Tkt, image=bg)
    bgimg.place(x=0, y=0)
    Tkt.title("ATM Management System")
    Tkt.iconbitmap('icon.ico')
    Tkt.geometry("600x300")
    lable1 = Label(Tkt, text="ATM Management System", borderwidth=8, relief="groove", bg='#EF7D00', fg='black',font=('Courier', 30, 'bold'))
    lable1.pack(pady=20)
    lable2 = Label(Tkt, text='Enter Your PIN', fg='black', font=('Courier', 15, 'bold'))
    lable2.pack(pady=1)
    global pin
    pin = StringVar()
    global entry1
    entry1 = Entry(Tkt, width=4, bg="#fbf8f7", fg="black", bd=5, justify='center', textvariable=pin, show="*",font=('Courier', 20, 'bold'))
    entry1.pack(pady=20)
    button1 = Button(Tkt, width=7, text="Submit", bg="black", bd=3, fg="white", command=CheckCredentials,font=('Courier', 15, 'bold'))
    button1.pack(pady=10)
    Tkt.eval('tk::PlaceWindow . center')
    Tkt.state('zoomed')
    Tkt.resizable(False, False)
    Tkt.mainloop()
# Window ###########################################

StartTK()
Login()
