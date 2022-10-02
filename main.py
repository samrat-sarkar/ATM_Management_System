import csv
import time
from tkinter import *
from tkinter import messagebox
from time import strftime

#Temp
My_PIN = None
My_Name = None
My_AC_No = None
My_IFSC = None
My_Balance = None
Phone_Number = None
Email = None
#Temp

#Request_Records###########################################
def Request_Records():
    with open("db.csv", newline='') as f:
        global My_PIN
        global My_Name
        global My_AC_No
        global My_IFSC
        global My_Balance
        global Phone_Number
        global Email
        ereader = csv.DictReader(f)
        for row in ereader:
           My_PIN=int(row['My_PIN'])
           My_Name = str(row['My_Name'])
           My_AC_No = int(row['My_AC_No'])
           My_IFSC = str(row['My_IFSC'])
           My_Balance = int(row['My_Balance'])
           Phone_Number = int(row['Phone_Number'])
           Email = str(row['Email'])
#Request_Records###########################################

#SESSION
User_Session=False
#SESSION
def StartTK():
    global Tkt
    Tkt = Tk()

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

def MatchPIN(PIN):
    Request_Records()
    if (int(PIN) == My_PIN):
        Go_to_Home()
    else:
        print(PIN," AND",My_PIN)
        entry1.delete(0, 'end')
        Msg0.set("INCORRECT PIN")
        print("Fail")


def CheckCredentials():
    PIN = pin.get()
    if len(PIN) >= 0 and len(PIN) < 4:
        entry1.delete(0, 'end')
        Msg0.set("INCORRECT PIN")
    elif len(PIN) > 4:
        entry1.delete(0, 'end')
        Msg0.set("INCORRECT PIN")
    elif len(PIN) == 4:
        MatchPIN(PIN)
    else:
        messagebox.showwarning("Error", "Something Went Wrong !")

def Update_PIN():
    A = OldPin.get()
    B = NewPin.get()
    C = CnfPin.get()

    if not A:
        Msg1.set("Enter Old PIN")
    elif not B:
        Msg1.set("Enter New PIN")
    elif not C:
        Msg1.set("Enter Confirm New PIN")
    else:
        if len(A)>0 and len(A)<4:
            Msg1.set("Enter 4 digits Old PIN")
            entry1.delete(0, 'end')
        elif len(A)>4:
            Msg1.set("Enter 4 digits Old PIN")
            entry1.delete(0, 'end')
        elif len(B)>0 and len(B)<4:
            Msg1.set("Enter 4 digits New PIN")
            entry2.delete(0, 'end')
        elif len(B)>4:
            Msg1.set("Enter 4 digits New PIN")
            entry2.delete(0, 'end')
        elif len(C)>0 and len(C)<4:
            Msg1.set("Enter 4 digits Confirm New PIN")
            entry3.delete(0, 'end')
        elif len(C)>4:
            Msg1.set("Enter 4 digits Confirm New PIN")
            entry3.delete(0, 'end')
        else:
            if int(A)!=My_PIN:
                Msg1.set("Incorrect Old PIN")
                entry1.delete(0, 'end')
            else:
                if int(B)!=int(C):
                    Msg1.set("Confirm PIN Not Match")
                    entry2.delete(0, 'end')
                    entry3.delete(0, 'end')
                elif int(B)==int(C):
                    print("Update Pin Here")



def Pin_Change():
    Request_Records()
    Tkt.configure(bg='black')
    Tkt.title("ATM Management System")
    Tkt.iconbitmap('icon.ico')
    Tkt.geometry("600x400")
    lable1 = Label(Tkt, text="PIN Change", bg='black', fg='#f00', font=('Courier', 25, 'bold', 'underline'))
    lable1.pack(pady=10)
    global Msg1
    Msg1 = StringVar()
    status = Label(Tkt, textvariable=Msg1, bg='black', fg='#f00', font=('Courier', 20, 'bold'))
    status.pack(pady=10)
    lable2 = Label(Tkt, text="Enter Old PIN ", bg='black', fg='#f00', font=('Courier', 15, 'bold'))
    lable2.pack(pady=0)
    global OldPin
    OldPin = StringVar()
    global entry1
    entry1 = Entry(Tkt, width=4, bg="#202124", fg="red", bd=5, justify='center', textvariable=OldPin, show="*",font=('Courier', 20, 'bold'))
    entry1.pack(pady=10)
    lable3 = Label(Tkt, text="New PIN ", bg='black', fg='#f00', font=('Courier', 15, 'bold'))
    lable3.pack(pady=0)
    global NewPin
    NewPin = StringVar()
    global entry2
    entry2 = Entry(Tkt, width=4, bg="#202124", fg="red", bd=5, justify='center', textvariable=NewPin,font=('Courier', 20, 'bold'))
    entry2.pack(pady=10)
    lable4 = Label(Tkt, text="Confirm New PIN ", bg='black', fg='#f00', font=('Courier', 15, 'bold'))
    lable4.pack(pady=0)
    global CnfPin
    CnfPin = StringVar()
    global entry3
    entry3 = Entry(Tkt, width=4, bg="#202124", fg="red", bd=5, justify='center', textvariable=CnfPin, show="*",font=('Courier', 20, 'bold'))
    entry3.pack(pady=10)
    button1 = Button(Tkt, command=Update_PIN, width=20, text="Change", bg="#484848", bd=3, fg="white",font=('Courier', 15, 'bold'))
    button1.pack(pady=10)
    button2 = Button(Tkt, command=Go_to_Home, width=20, text="Back", bg="#484848", bd=3, fg="white",font=('Courier', 15, 'bold'))
    button2.pack(pady=10)
    Tkt.eval('tk::PlaceWindow . center')
    Tkt.state('zoomed')
    Tkt.resizable(False, False)
    Tkt.mainloop()

def Balance_Inquiry():
    Request_Records()
    Tkt.configure(bg='black')
    Tkt.title("ATM Management System")
    Tkt.iconbitmap('icon.ico')
    Tkt.geometry("600x400")
    lable1 = Label(Tkt, text="Balance Inquiry", bg='black', fg='#f00', font=('Courier', 25, 'bold', 'underline'))
    lable1.pack(pady=10)
    lable2 = Label(Tkt, text="Account Holder Name : " + str(My_Name), bg='black', fg='#f00', font=('Courier', 15, 'bold'))
    lable2.pack(pady=1)
    lable3 = Label(Tkt, text="Account Number : " + str(My_AC_No), bg='black', fg='#f00', font=('Courier', 15, 'bold'))
    lable3.pack(pady=1)
    lable4 = Label(Tkt, text="Account IFSC : " + str(My_IFSC), bg='black', fg='#f00', font=('Courier', 15, 'bold'))
    lable4.pack(pady=1)
    lable5 = Label(Tkt, text="Phone Number : " + str(Phone_Number), bg='black', fg='#f00', font=('Courier', 15, 'bold'))
    lable5.pack(pady=1)
    lable6 = Label(Tkt, text="Email ID : " + str(Email), bg='black', fg='#f00', font=('Courier', 15, 'bold'))
    lable6.pack(pady=1)
    lable7 = Label(Tkt, text="Balance Number : ₹" + str(My_Balance), bg='black', fg='#f00', font=('Courier', 15, 'bold'))
    lable7.pack(pady=1)
    button1 = Button(Tkt, command=Go_to_Home, width=20, text="Back", bg="#484848", bd=3, fg="white", font=('Courier', 15, 'bold'))
    button1.pack(pady=10)
    Tkt.eval('tk::PlaceWindow . center')
    Tkt.state('zoomed')
    Tkt.resizable(False, False)
    Tkt.mainloop()


def Home():
    Tkt.configure(bg='black')
    Tkt.title("ATM Management System")
    Tkt.iconbitmap('icon.ico')
    Tkt.geometry("600x400")
    lable1 = Label(Tkt, text="ATM Management System", borderwidth=8, relief="groove", bg='black', fg='#f00',font=('Courier', 30, 'bold'))
    lable1.pack(pady=20)
    lable2 = Label(Tkt, text="Welcome "+My_Name, bg='black', fg='#f00', font=('Courier', 20, 'bold'))
    lable2.pack(pady=1)
    button1 = Button(Tkt, command=Go_to_Balance_Inquiry, width=20, text="Balance Inquiry", bg="#484848", bd=3, fg="white",font=('Courier', 15, 'bold'))
    button1.pack(pady=10)
    button2 = Button(Tkt, command=Go_to_Pin_Change, width=20, text="Pin Change", bg="#484848", bd=3, fg="white", font=('Courier', 15, 'bold'))
    button2.pack(pady=10)
    button3 = Button(Tkt, width=20, text="Withdrawal", bg="#484848", bd=3, fg="white", font=('Courier', 15, 'bold'))
    button3.pack(pady=10)
    button4 = Button(Tkt, width=20, text="Deposit", bg="#484848", bd=3, fg="white", font=('Courier', 15, 'bold'))
    button4.pack(pady=10)
    Tkt.eval('tk::PlaceWindow . center')
    Tkt.state('zoomed')
    Tkt.resizable(False, False)
    Tkt.mainloop()


def Login():
    Tkt.configure(bg='black')
    Tkt.title("ATM Management System")
    Tkt.iconbitmap('icon.ico')
    Tkt.geometry("600x300")
    lable1 = Label(Tkt, text="ATM Management System", borderwidth=8, relief="groove", bg='black', fg='#f00',font=('Courier', 30, 'bold'))
    lable1.pack(pady=20)
    global Msg0
    Msg0 = StringVar()
    Msg0.set("Enter Your PIN")
    lable2 = Label(Tkt, textvariable=Msg0, bg='black', fg='#f00', font=('Courier', 15, 'bold'))
    lable2.pack(pady=1)
    global pin
    pin = StringVar()
    global entry1
    entry1 = Entry(Tkt, width=4, bg="#202124", fg="red", bd=5, justify='center', textvariable=pin, show="*",font=('Courier', 20, 'bold'))
    entry1.pack(pady=20)
    button1 = Button(Tkt, width=7, text="Submit", bg="#484848", bd=3, fg="white", command=CheckCredentials,font=('Courier', 15, 'bold'))
    button1.pack(pady=10)
    Tkt.eval('tk::PlaceWindow . center')
    Tkt.state('zoomed')
    Tkt.resizable(False, False)
    Tkt.mainloop()

StartTK()
Login()



