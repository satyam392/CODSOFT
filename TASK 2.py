import tkinter
from tkinter import *

root = Tk()
root.title("Simple Calculator")
root.geometry("700x800+100+200")  
root.resizable(False, False)
root.configure(bg="#17161b")

equation = ""

def show(value):
    global equation
    equation += value
    label_result.config(text=equation)

def clear():
    global equation
    equation = ""
    label_result.config(text=equation)

def calculate():
    global equation
    result = ""
    if equation != "":
        try:
            result = eval(equation)
        except:
            result = "!!ERROR!!"
            equation = ""
    label_result.config(text=result)


label_result = Label(root, width=25, height=2, text="", font=("arial", 40), fg="#ffcc00", bg="#8b0000")
label_result.pack(pady=30)  

Button(root, text="C", width=5, height=2, font=("arial", 35, "bold"), bd=2, fg="#fff", 
       bg="#ff4500", command=lambda: clear()).place(x=10, y=150)
Button(root, text="/", width=5, height=2, font=("arial", 35, "bold"), bd=2, fg="#fff",
        bg="#b22222", command=lambda: show("/")).place(x=150, y=150)
Button(root, text="%", width=5, height=2, font=("arial", 35, "bold"), bd=2, fg="#fff", 
       bg="#b22222", command=lambda: show("%")).place(x=290, y=150)
Button(root, text="*", width=5, height=2, font=("arial", 35, "bold"), bd=2, fg="#fff",
        bg="#b22222", command=lambda: show("*")).place(x=430, y=150)

Button(root, text="7", width=5, height=2, font=("arial", 35, "bold"), bd=2, fg="#fff", 
       bg="#ff6347", command=lambda: show("7")).place(x=10, y=250)
Button(root, text="8", width=5, height=2, font=("arial", 35, "bold"), bd=2, fg="#fff",
        bg="#ff6347", command=lambda: show("8")).place(x=150, y=250)
Button(root, text="9", width=5, height=2, font=("arial", 35, "bold"), bd=2, fg="#fff", 
       bg="#ff6347", command=lambda: show("9")).place(x=290, y=250)
Button(root, text="-", width=5, height=2, font=("arial", 35, "bold"), bd=2, fg="#fff", 
       bg="#b22222", command=lambda: show("-")).place(x=430, y=250)

Button(root, text="4", width=5, height=2, font=("arial", 35, "bold"), bd=2, fg="#fff", 
       bg="#ff6347", command=lambda: show("4")).place(x=10, y=350)
Button(root, text="5", width=5, height=2, font=("arial", 35, "bold"), bd=2, fg="#fff", 
       bg="#ff6347", command=lambda: show("5")).place(x=150, y=350)
Button(root, text="6", width=5, height=2, font=("arial", 35, "bold"), bd=2, fg="#fff", 
       bg="#ff6347", command=lambda: show("6")).place(x=290, y=350)
Button(root, text="+", width=5, height=2, font=("arial", 35, "bold"), bd=2, fg="#fff", 
       bg="#b22222", command=lambda: show("+")).place(x=430, y=350)

Button(root, text="1", width=5, height=2, font=("arial", 35, "bold"), bd=2, fg="#fff", 
       bg="#ff6347", command=lambda: show("1")).place(x=10, y=450)
Button(root, text="2", width=5, height=2, font=("arial", 35, "bold"), bd=2, fg="#fff",
        bg="#ff6347", command=lambda: show("2")).place(x=150, y=450)
Button(root, text="3", width=5, height=2, font=("arial", 35, "bold"), bd=2, fg="#fff",
        bg="#ff6347", command=lambda: show("3")).place(x=290, y=450)
Button(root, text="0", width=11, height=2, font=("arial", 35, "bold"), bd=2, fg="#fff", 
       bg="#ff6347", command=lambda: show("0")).place(x=10, y=550)

Button(root, text=".", width=5, height=2, font=("arial", 35, "bold"), bd=2, fg="#fff",
        bg="#ff6347", command=lambda: show(".")).place(x=290, y=550)
Button(root, text="=", width=5, height=3, font=("arial", 35, "bold"), bd=2, fg="#fff",
        bg="#ffcc00", command=lambda: calculate()).place(x=430, y=450)

root.mainloop()
