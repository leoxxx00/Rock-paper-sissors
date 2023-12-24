from tkinter import *
from tkinter import ttk
from random import *

root = Tk()
root.title("Rock Paper Scissors")
root.geometry("500x1000")
root.config(bg="white")

rock = PhotoImage(file='rock.png')
paper = PhotoImage(file='paper.png')
scissors = PhotoImage(file='siccior.png')

image_list = [rock, paper, scissors]

pick_number = randint(0,2)

image_label = Label(root,image=image_list[pick_number],bd=0)
image_label.pack(pady=20)

def spin():
    pick_number = randint(0,2)
    image_label.config(image=image_list[pick_number])

    if user_choice.get()=="Rock":
        user_choice_value=0
    elif user_choice.get()=="Paper":
        user_choice_value=1
    elif user_choice.get() == "Scissors":
        user_choice_value = 2

    if user_choice_value == 0:
        if pick_number==0:
            win_lose_label.config(text='ITS A TIE ..........SPINNNNNN')
        elif pick_number == 1:
            win_lose_label.config(text='You loose... paper cover rock ...!!!')
        elif pick_number == 2:
            win_lose_label.config(text='Rock smash sissor YOU WINNNNNN !!!')

    if user_choice_value == 1:
        if pick_number==1:
            win_lose_label.config(text='ITS A TIE ..........SPINNNNNN')
        elif pick_number == 0:
            win_lose_label.config(text='You win... paper cover rock...!!!')
        elif pick_number == 2:
            win_lose_label.config(text='Sissor cuts paper ! YOU LOOSEEEE')

    if user_choice_value == 2:
        if pick_number==2:
            win_lose_label.config(text='ITS A TIE ..........SPINNNNNN')
        elif pick_number == 0:
            win_lose_label.config(text='You loose... rock smash sissor...!!!')
        elif pick_number == 1:
            win_lose_label.config(text=' sissor cut paper YOU WINNNNNN !!!')

user_choice = ttk.Combobox(root,value=("Rock","Paper","Sissors"))
user_choice.current(0)
user_choice.pack(pady=20)

spin_button = Button(root,text="SPIN!!!",command=spin)
spin_button.pack(pady=10)

win_lose_label = Label(root,text="",font=("Helvetica",18),bg="white")
win_lose_label.pack(pady=50)

root.mainloop()
