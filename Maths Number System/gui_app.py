import tkinter as tk
from tkinter.ttk import *
from tkinter import*
from tkinter import ttk
root = tk.Tk()
root.title("Linear Equation")
root.geometry("1920x1080")
root['bg']='lightyellow'
#lbl3 = tk.Label(root,text="""
#This program is to Find a two digit number whose difference between the digits 
#is known and also the sum of original number added with two digit number after 
#interchanging the digits
#""").grid(column = 1, row = 0)
def getTextInput():
    text_input_1=textExample.get()
    text_input_2=textExample_2.get()
    a=int(text_input_1)
    
    b1=int(text_input_2)
    b=(a-b1*11)/22
    result1=(b+b1)*10+b
    lbl= tk.Label(root,font=('Consolas',13,'bold'),text=round(result1),bg='lightyellow').grid(column = 1, row = 6)
    
    result2=(b*10)+b+b1
    lbl2 = tk.Label(root,font=('Consolas',13,'bold'),text=round(result2),bg='lightyellow').grid(column = 1, row = 7)
#Label4
lbl4 = tk.Label(root,text="Sum of the two digits numbers: ",
                bg='lightyellow',font=('Consolas',13,'bold')).grid(column = 0, row = 0)
#TxtBox1
textExample=ttk.Entry(root,font=('Consolas',13,'bold'))
textExample.grid(column = 1, row = 0)

#Label5
lbl5 = tk.Label(root,text="Difference between the digit of two digit number",bg='lightyellow',font=('Consolas',13,'bold'))
lbl5.grid(column = 0, row = 1)
#TxtBox2
textExample_2=ttk.Entry(root,font=('Consolas',13,'bold'))
textExample_2.grid(column = 1, row = 1)

#Button
btnRead1=ttk.Button(root,text="Calculate numbers-->",command=getTextInput,width=20).grid(column = 1, row = 5,sticky = E)



root.mainloop()
