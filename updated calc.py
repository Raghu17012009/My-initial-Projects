import tkinter
import keyboard
import math
#buttons
button_values = [
    ["%", "AC", "C","⌫"], 
    ["¹/ₓ","X²","√",  "÷",],
    ["7", "8", "9", "×"], 
    ["4", "5", "6", "-"],
    ["1", "2", "3", "+"],
    ["+/-","0",".", "="]
]

Spl_symblos=["¹/ₓ","√","X²",]
right_symbols = ["÷", "×", "-", "+", "="]
top_symbols = ["AC", "+/-", "%",".","C"]
backspace_symbol = ["⌫"]
cancel_symbol = ["C"]

#rows and coloums
row_count=len(button_values)
column_count=len(button_values[0])

#colours
colour_light_gray="#D4D4D2"
colour_black="#1C1C1C"
colour_dark_gray="#505050"
colour_orange="#FF9500"
colour_white="white"
colour_red="#FF3B30"

window=tkinter.Tk()

window.title("Calculator")
window.resizable(False,False)

frame=tkinter.Frame(window)


def clear_all():
    global count,A,operator,B
    A=0
    operator=None
    B=None
    count=0

def validate_length(P):
    Max=9
    return len(P) <= Max

def enter(event):
    operator = "="
    button_clicked(operator)

def key_press(event):
    global operator
    key = event.char

    if key in ["+","-","/","*",None]:
        op=key
        
        if op=="*":
            op="×"
        elif op==None:
            op="="

        a=(entry.get())
        a=a[0:len(a)]
        button_clicked(op)
        entry.delete(0,tkinter.END)


label=tkinter.Label( frame ,text="0",font=("Ariel",30),background=colour_black,foreground=colour_white,
                    anchor="e",width=column_count)

label.grid(row=0,column=0,columnspan=column_count,sticky="we")

entry=tkinter.Entry(frame,font=("Ariel",35),background="#1C1C1C",foreground="white",justify="right",bd=5,width=column_count,
                    validate="key",validatecommand=(window.register(validate_length),"%P"))

entry.grid(row=1,column=0,columnspan=column_count,sticky="we")


entry.bind("<Return>", enter)


entry.bind('+',key_press)
entry.bind('/',key_press)
entry.bind('*',key_press)
entry.bind('-',key_press)






def call():
    for row in range(row_count):
        for column in range(column_count):
                value = button_values[row][column]
                button=tkinter.Button(frame,text=value,font=("Ariel",30),width=column_count-1,height=1,
                                    command=lambda value=value: button_clicked(value))
                
                if value in top_symbols:
                    button.config(background=colour_light_gray,foreground=colour_black,bd=5)
                elif value in Spl_symblos:
                    button.config(background=colour_black,foreground=colour_white,bd=5)
                elif value in right_symbols:
                    button.config(background=colour_orange,foreground=colour_white,bd=5)
                elif value in backspace_symbol:
                    button.config(background=colour_white,foreground=colour_red,bd=5)
                else:
                    button.config(background=colour_dark_gray,foreground=colour_white,bd=5)

                button.grid(row=row+2,column=column)

call()


frame.pack()

#A+B A-B A/B A*B
A=0
operator=None
B=None
a=None
count = 0

def remove_zero_decimal(num):
    n=str(num)
    i=0
    a=""
    if len(n)>9:
        for i in range(0,9):
            a += n[i]
    else:
        for i in range(0,len(n)):
            a += n[i]


    n = float (a)
    if n%1 == 0:
            n = int(n)
    return str(n)

def ans(ans):
    global A,operator,B
    label["text"]=A+operator+B+"="
    entry.delete(0,tkinter.END)
    entry.insert(0,ans)

def ans1(ans):
    global A,operator,a
    
    if operator=="X²":
        label["text"]="("+remove_zero_decimal(A)+")²"
    elif operator=="¹/ₓ":
        label["text"]="¹/"+remove_zero_decimal(A)
    else:
        label["text"]=operator+remove_zero_decimal(A)
    entry.delete(0,tkinter.END)
    entry.insert(0,a)

def ans2(ans,op):
    global a,A
    if op=="%":
        label["text"]=remove_zero_decimal(A)+op
    else:
        label["text"]=op+"("+remove_zero_decimal(A)+")"
    entry.delete(0,tkinter.END)
    entry.insert(0,a)

def button_clicked(value):
    global count,Spl_symblos,right_symbols,top_symbol,A,operator,B,backspace_symbol,a

    if value in right_symbols:
        if value == "=":
            if A is not None and operator is not None:
                        a=entry.get()
                        a=a[1:]
                        label["text"]=a
                        B=label["text"]
                        print(B)
                        numA = float(A)
                        numB = float(B)


                        if operator == "+":
                            result=float(remove_zero_decimal(numA+numB))
                            if result>100000000:
                                label["text"]="Error"
                            else:
                                a=remove_zero_decimal(numA+numB)
                                ans(a)
                        elif operator == "-":
                            result=float(remove_zero_decimal(numA-numB))
                            if result<-100000000:
                                label["text"]="Error"
                            else:
                                a=remove_zero_decimal(numA-numB)
                                ans(a)
                        elif operator == "÷":
                            if numB == 0:
                                label["text"]="Error"
                            else:
                                a=remove_zero_decimal(numA/numB)
                                ans(a)
                        elif operator == "×":
                            result=float(remove_zero_decimal(numA*numB))

                            if result>100000000:
                                label["text"]="Error"
                            else:
                                a=remove_zero_decimal(numA*numB)
                                ans(a)                          
                            remove_zero_decimal(numA*numB)
                        
                        clear_all()
        
        elif value in "+-×÷":
            a=""
            if operator is None:
                a=entry.get()
                label["text"]=a
                print(label["text"])   
                A=label["text"]
                B=0
            count=0
            entry.delete(0,tkinter.END)
            operator = value
            entry.insert(0,operator)
            
    
    elif value in backspace_symbol:
        if value == "⌫":
            a=entry.get()
            a=a[:-1]
            entry.delete(0,tkinter.END)
            entry.insert(0,a)
            label["text"]=(label["text"])[:-1]
            if label["text"]=="":
                label["text"]="0"

    
    elif value in cancel_symbol:
        if value == "C":
            label["text"]="0"
            count=0

   #"¹/ₓ","√","X²" 
    elif value in Spl_symblos:
            label["text"]=entry.get()
            if value == "√":
                operator=value
                A=float(label["text"])
                result=(math.sqrt(A))
                a=remove_zero_decimal(result)
                ans1(a)
            elif value == "X²":
                operator=value
                A=float(label["text"])
                result=(math.pow(A,2))
                a=remove_zero_decimal(result)
                ans1(a)
            elif value == "¹/ₓ":
                operator=value
                A=float(label["text"])
                if A == 0:
                    label["text"]="Error"
                else:
                    result=(1/A)
                    a=remove_zero_decimal(result)
                    ans1(a)
    
    elif value in top_symbols:
        label["text"]=entry.get()
        if value =="AC":
            entry.delete(0,tkinter.END)
            clear_all()
            label["text"]="0"
        elif value =="+/-":
            operator=value
            A=label["text"]
            result = float(label["text"]) * -1
            a=remove_zero_decimal(result)
            ans2(a,operator)
        elif value == "%":
            operator=value
            A=label["text"]
            result = float(label["text"]) / 100
            a=remove_zero_decimal(result)
            ans2(a,operator)
        elif value == ".":
            if value not in label["text"]:
                label["text"] += value
                entry.insert(tkinter.END,value)
    
    
    else:
        
        if value in "0123456789":
            ap=entry.get()
            a=""
            for i in ap:
                if i not in right_symbols:
                    a+=i
            label["text"]=a
            count+=1
            if count<9:
                if label["text"]== "0":
                    label["text"] = value
                    entry.insert(tkinter.END, value)
                else:
                    label["text"] += value
                    entry.insert(tkinter.END, value)

#to centre the window
window.update()
window.update_idletasks()   #update window with the new dimensions

window_width=window.winfo_width()
window_height= window.winfo_height()
screen_width= window.winfo_screenwidth()
screen_height=window.winfo_screenheight()

window_x=int((screen_width/2)-(window_width/2))
window_y=int((screen_height/2)-(window_height/2))

#format "(w)x(h)+(x)+(y)"
window.geometry(f"{window_width}x{window_height}+{window_x}+{window_y}")

window.mainloop()