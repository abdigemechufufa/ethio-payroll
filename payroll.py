from tkinter import *
from tkinter import messagebox

def pention_one(basicSalary):
    return round(bSdata.get() * 0.07)

def pention_two(basicSalary):
    return round(bSdata.get() * 0.11) 

def tax(basicSalary):
    if bSdata.get() >= 0 and bSdata.get() <= 600:
        return 0
    elif bSdata.get() >= 601 and bSdata.get() <= 1650:
        return round(bSdata.get() * 0.1 - 60)
    elif bSdata.get() >= 1651 and bSdata.get() <= 3200:
        return round(bSdata.get() * 0.15 - 142.5)
    elif bSdata.get() >= 3201 and bSdata.get() <= 5250:
        return round(bSdata.get() * 0.20 - 302.5)
    elif bSdata.get() >= 5251 and bSdata.get() <= 7800:
        return round(bSdata.get() * 0.25 - 565)
    elif bSdata.get() >= 7801 and bSdata.get() <= 10900:
        return round(bSdata.get() * 0.3 - 955)
    elif bSdata.get() > 10901:
        return round(bSdata.get() * 0.35 - 1500)

def Calculate():
    employeeName = eN.get()
    basicSalary = bS.get()
    allowance = aL.get()
    overTime = oT.get()
    otherDeduction = oD.get()

    p1 = pention_one(basicSalary)
    p2 = pention_two(basicSalary)
    incomeTax = tax(basicSalary)

    grossSalary = bSdata.get() + aLdata.get() + oTdata.get()
    deductables = incomeTax + p1 + p2 + oDdata.get()
    totalDeduction = bSdata.get() - deductables
    netSalary = bSdata.get()  - deductables

    result = Toplevel(root)
    result.geometry("275x270")
    result.title("Result")
    result.resizable(False, False)

    Label(result, text = "Employee Name").place(x=10, y=10)
    Label(result, text = "Gross Salary").place(x=10, y=40)
    Label(result, text = "Income Tax").place(x=10, y=70)
    Label(result, text = "Pension 7%").place(x=10, y=100)
    Label(result, text = "Pension 11%").place(x=10, y=130)
    Label(result, text = "Total Deduction").place(x=10, y=160)
    Label(result, text = "Net Salary").place(x=10, y=190)

    Label(result, text = eNdata.get()).place(x=140, y=10)
    Label(result, text = str(grossSalary)+" Birr").place(x=140, y=40)
    Label(result, text = str(incomeTax)+" Birr").place(x=140, y=70)
    Label(result, text = str(p1)+" Birr").place(x=140, y=100)
    Label(result, text = str(p2)+" Birr").place(x=140, y=130)
    Label(result, text = str(totalDeduction)+" Birr").place(x=140, y=160)
    Label(result, text = str(netSalary)+" Birr").place(x=140, y=190)

    Button (result, text="Ok", command=lambda: result.destroy(), height = 2, width= 35).place(x=10, y=220)

def Scale():
    scale = Toplevel(root)
    scale.geometry("300x250")
    scale.title("Scale For Tax")
    scale.resizable(False, False)
    
    Label(scale, text = "If Salary").place(x=10, y=10)
    Label(scale, text = "0 -> 600").place(x=10, y=40)
    Label(scale, text = "601 -> 1650").place(x=10, y=70)
    Label(scale, text = "1651 -> 3200").place(x=10, y=100)
    Label(scale, text = "3201 -> 5250").place(x=10, y=130)
    Label(scale, text = "5251 -> 7800").place(x=10, y=160)
    Label(scale, text = "7801 -> 10900").place(x=10, y=190)
    Label(scale, text = "> 10901").place(x=10, y=220)

    Label(scale, text = "Tax").place(x=140, y=10)
    Label(scale, text = "0").place(x=140, y=40)
    Label(scale, text = "Basic Salary * 10% - 60").place(x=140, y=70)
    Label(scale, text = "Basic Salary * 15% - 142.5").place(x=140, y=100)
    Label(scale, text = "Basic Salary * 20% - 302.50").place(x=140, y=130)
    Label(scale, text = "Basic Salary * 25% - 565").place(x=140, y=160)
    Label(scale, text = "Basic Salary * 30% - 955").place(x=140, y=190)
    Label(scale, text = "Basic Salary * 35% - 1500").place(x=140, y=220)

def About():
    messagebox.showinfo("About","This Program Work For Ethiopia")

def Devs():
    messagebox.showinfo("Developer","Developed By Abdi Gemechu\nSource Code : https://github.com/abdigemechufufa/ethio-payroll")

root = Tk()
root.title("Payroll System")
root.resizable(False, False)
root.geometry("275x260")

global eN
global bS
global aL
global oT
global oD

eNdata = StringVar()
bSdata = IntVar()
aLdata = IntVar()
oTdata = IntVar()
oDdata = IntVar()

Label(root, text="Employee Name").place(x=10, y=10)
Label(root, text="Basic Salary").place(x=10, y=40)
Label(root, text="Allowance").place(x=10, y=70)
Label(root, text="Overtime").place(x=10, y=100)
Label(root, text="Other Deduction").place(x=10, y=130)

eN = Entry(root, textvariable=eNdata)
eN.place(x=140, y=10)

bS = Entry(root, textvariable=bSdata)
bS.place(x=140, y=40)

aL = Entry(root, textvariable=aLdata)
aL.place(x=140, y=70)

oT = Entry(root, textvariable=oTdata)
oT.place(x=140, y=100)

oD = Entry(root, textvariable=oDdata)
oD.place(x=140, y=130)

Button (root, text="Calculate", command=Calculate, height = 2, width= 35).place(x=10, y=160)
Button (root, text="Scale", command=Scale, height = 2, width= 10).place(x=10, y=210)
Button (root, text="About", command=About, height = 2, width= 10).place(x=98, y=210)
Button (root, text="Devs", command=Devs, height = 2, width= 10).place(x=185, y=210)

root.mainloop()