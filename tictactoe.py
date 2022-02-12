from tkinter import *
import tkinter.messagebox
tk = Tk()
tk.title("Tic Tac Toe")

playera = StringVar()
playerb = StringVar()
p1 = StringVar()
p2 = StringVar()

player1_name = Entry(tk, textvariable=p1, bd=5)
player1_name.grid(row=1, column=1, columnspan=8)
player2_name = Entry(tk, textvariable=p2, bd=5)
player2_name.grid(row=2, column=1, columnspan=8)

bclick = True
flag = 0

def disableButton():
    button1.configure(state=DISABLED)
    button2.configure(state=DISABLED)
    button3.configure(state=DISABLED)
    button4.configure(state=DISABLED)
    button5.configure(state=DISABLED)
    button6.configure(state=DISABLED)
    button7.configure(state=DISABLED)
    button8.configure(state=DISABLED)
    button9.configure(state=DISABLED)

def btnClick(button):
    global bclick, flag, playera, playerb, p1, p2
    if(button['text']==" " and bclick == True):
        button['text'] = "Fighter"
        bclick = False
        playera = p1.get() + "Wins!"
        playerb = p2.get() + "Wins!"
        checkWin()
        flag += 1

    elif(button['text']==" " and bclick == False):
        button['text'] = "Warrior"
        bclick = True
        checkWin()
        flag += 1  

    else:
        tkinter.messagebox.showinfo("Tic-Tac-Toe","This button is already clicked!")

def checkWin():
    if(button1['text']=="Fighter" and button2['text']=="Fighter" and button3['text']=="Fighter" or
       button4['text']=="Fighter" and button5['text']=="Fighter" and button6['text']=="Fighter" or
       button7['text']=="Fighter" and button8['text']=="Fighter" and button9['text']=="Fighter" or
       button1['text']=="Fighter" and button4['text']=="Fighter" and button7['text']=="Fighter" or
       button2['text']=="Fighter" and button5['text']=="Fighter" and button8['text']=="Fighter" or
       button3['text']=="Fighter" and button6['text']=="Fighter" and button9['text']=="Fighter" or
       button1['text']=="Fighter" and button5['text']=="Fighter" and button9['text']=="Fighter" or
       button3['text']=="Fighter" and button5['text']=="Fighter" and button7['text']=="Fighter"):
        tkinter.messagebox.showinfo("Tic-Tac-Toe,playera") 
        disableButton()

    elif(button1['text']=="Warrior" and button2['text']=="Fighter" and button3['text']=="Warrior" or
       button4['text']=="Warrior" and button5['text']=="Warrior" and button6['text']=="Warrior" or
       button7['text']=="Warrior" and button8['text']=="Warrior" and button9['text']=="Warrior" or
       button1['text']=="Warrior" and button4['text']=="Warrior" and button7['text']=="Warrior" or
       button2['text']=="Warrior" and button5['text']=="Warrior" and button8['text']=="Warrior" or
       button3['text']=="Warrior" and button6['text']=="Warrior" and button9['text']=="Warrior" or
       button1['text']=="Warrior" and button5['text']=="Warrior" and button9['text']=="Warrior" or
       button3['text']=="Warrior" and button5['text']=="Warrior" and button7['text']=="Warrior"):
        tkinter.messagebox.showinfo("Tic-Tac-Toe,playerb") 
        disableButton()

    elif(flag == 8):
        tkinter.messagebox.showinfo("Tic-Tac-Toe","Its a tie")
        disableButton()

        

       


    
    
    
    
    
    
    
    






buttons = StringVar()

label = Label( tk, text="Player 1:", font='Times 28 bold italic', bg='black', fg='red', height=1, width=8)
label.grid(row=1, column=0)


label = Label( tk, text="Player 2:", font='Times 28 bold italic', bg='black', fg='red', height=1, width=8)
label.grid(row=2, column=0)

button1 = Button(tk, text=" ", font='Times 30 bold', bg='violet', fg='white', height=4, width=8, command=lambda: btnClick(button1))
button1.grid(row=3, column=0)

button2 = Button(tk, text=' ', font='Times 30 bold', bg='indigo', fg='white', height=4, width=8, command=lambda: btnClick(button2))
button2.grid(row=3, column=1)

button3 = Button(tk, text=' ',font='Times 30 bold', bg='blue', fg='white', height=4, width=8, command=lambda: btnClick(button3))
button3.grid(row=3, column=2)

button4 = Button(tk, text=' ', font='Times 30 bold', bg='green', fg='white', height=4, width=8, command=lambda: btnClick(button4))
button4.grid(row=4, column=0)

button5 = Button(tk, text=' ', font='Times 30 bold', bg='yellow', fg='white', height=4, width=8, command=lambda: btnClick(button5))
button5.grid(row=4, column=1)

button6 = Button(tk, text=' ', font='Times 30 bold', bg='orange', fg='white', height=4, width=8, command=lambda: btnClick(button6))
button6.grid(row=4, column=2)

button7 = Button(tk, text=' ', font='Times 30 bold', bg='red', fg='white', height=4, width=8, command=lambda: btnClick(button7))
button7.grid(row=5, column=0)

button8 = Button(tk, text=' ', font='Times 30 bold', bg='pink', fg='white', height=4, width=8, command=lambda: btnClick(button8))
button8.grid(row=5, column=1)

button9 = Button(tk, text=' ', font='Times 30 bold', bg='lime', fg='white', height=4, width=8, command=lambda: btnClick(button9))
button9.grid(row=5, column=2)

tk.mainloop()
