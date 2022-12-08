#3. Создайте программу для игры в ""Крестики-нолики"".
from tkinter import*
import random

def fill(i):
    global table
    global flag
    if flag:
        table[i] = "X"
        buttons[i].config(text='X')
    else:
        table[i] = "O"
        buttons[i].config(text='O')
    if win_game(table):
        lbl.configure(text='Game end')
    else:
      flag = not flag  

def win_game(array): #победные варианты
    if (array[0] == array[1] == array[2] or
     array[3] == array[4] == array[5] or
     array[6] == array[7] == array[8] or
     array[0] == array[3] == array[6] or
     array[1] == array[4] == array[7] or
     array[2] == array[5] == array[8] or
     array[0] == array[4] == array[8] or
     array[2] == array[4] == array[6]) :
        return True
    else:
        return False    

win = Tk()
win.title("Game")
lbl = Label(win, text="game start")
lbl.grid(column=1, row=4)

buttons = [Button(width=5, height=4, command=lambda x=i: fill(x)) for i in range(9)]
row = 1
col = 0
for i in range(9):
    buttons[i].grid(row =row, column =col)
    col += 1
    if col == 3:
        row += 1
        col =0
table = [int(i) for i in range(9)]      #исходная таблица игры
flag = random.randint(0,1)


win.mainloop()