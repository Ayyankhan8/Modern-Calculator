from customtkinter import *
from tkinter import *
from tkinter import END
from tkinter import messagebox
def answer():
    expressionfield = input_value.get()
    try:
        result = eval(expressionfield)
        ans = round(result,1)
        input_value.delete(0,END)
        input_value.insert(0,ans)
    
    except SyntaxError:
        messagebox.showerror('Error','INVALID EXPRESSION')
    except ZeroDivisionError:
        messagebox.showerror('error','Number cannot divided by zero')    

def ButtonClick(number):
    global operator
    operator = operator + str(number)
    input_value.set(operator)
    
def ButtonClear():
    global operator
    operator =" "
    input_value.set("")

def ButtonEqual():
    global operator
    result = str(eval(operator))
    input_value.set(result)
    operator = ""

main = Tk()
main.title("Calculator")

operator = ""
input_value = StringVar()
display_text = Entry(main,font=("arial",20,"bold"),textvariable=input_value,bd=30,insertwidth=4,
                     bg="powder blue",justify=RIGHT)
display_text.grid(columnspan=4)

# row : button 7,8,9,+

btn_7 = Button(main,padx=16,bd=8,fg="black",font=("arial",20,"bold"),text="7",command=lambda: ButtonClick(7))
btn_7.grid(row=1,column=0)

btn_8 = Button(main,padx=16,bd=8,fg="black",font=("arial",20,"bold"),text="8",command=lambda: ButtonClick(8))
btn_8.grid(row=1,column= 1)

btn_9 = Button(main,padx=16,bd=8,fg="black",font=("arial",20,"bold"),text="9",command=lambda: ButtonClick(9))
btn_9.grid(row=1,column=2)

btn_add = Button(main,padx=16,bd=8,fg="black",font=("arial",20,"bold"),text="+",command=lambda: ButtonClick("+"))
btn_add.grid(row=1,column=3)

# row : button 4,5,6,-

btn_4 = Button(main,padx=16,bd=8,fg="black",font=("arial",20,"bold"),text="4",command=lambda: ButtonClick(4))
btn_4.grid(row=2,column=0)

btn_5 = Button(main,padx=16,bd=8,fg="black",font=("arial",20,"bold"),text="5",command=lambda: ButtonClick(5))
btn_5.grid(row=2,column= 1)

btn_6 = Button(main,padx=16,bd=8,fg="black",font=("arial",20,"bold"),text="6",command=lambda: ButtonClick(6))
btn_6.grid(row=2,column=2)

btn_minus = Button(main,padx=16,bd=8,fg="black",font=("arial",20,"bold"),text="-",command=lambda: ButtonClick("-"))
btn_minus.grid(row=2,column=3)

# row : button 1,2,4,*

btn_1 = Button(main,padx=16,bd=8,fg="black",font=("arial",20,"bold"),text="1",command=lambda: ButtonClick(1))
btn_1.grid(row=3,column=0)

btn_2 = Button(main,padx=16,bd=8,fg="black",font=("arial",20,"bold"),text="2",command=lambda: ButtonClick(2))
btn_2.grid(row=3,column= 1)

btn_3 = Button(main,padx=16,bd=8,fg="black",font=("arial",20,"bold"),text="3",command=lambda: ButtonClick(3))
btn_3.grid(row=3,column=2)

btn_mul = Button(main,padx=16,bd=8,fg="black",font=("arial",20,"bold"),text="*",command=lambda: ButtonClick("*"))
btn_mul.grid(row=3,column=3)

# row : button 0,c,=,/
btn_0 = Button(main,padx=16,bd=8,fg="black",font=("arial",20,"bold"),text="0",command=lambda: ButtonClick(0))
btn_0.grid(row=4,column=0)

btn_clear = Button(main,padx=16,bd=8,fg="black",font=("arial",20,"bold"),text="C",command=ButtonClear)
btn_clear.grid(row=4,column= 1)

btn_equal = Button(main,padx=16,bd=8,fg="black",font=("arial",20,"bold"),text="=",command=ButtonEqual)
btn_equal.grid(row=4,column=2)

btn_div = Button(main,padx=16,bd=8,fg="black",font=("arial",20,"bold"),text="/",command=lambda: ButtonClick("/"))
btn_div.grid(row=4,column=3)


main.mainloop()
