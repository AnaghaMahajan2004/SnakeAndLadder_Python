from tkinter import*
from PIL import Image, ImageTk
import random

root = Tk()
root.title("ROCK PAPER SCISSORS")
root.configure(bg="black")
root.geometry("1300x600")

rock_img1 = ImageTk.PhotoImage(Image.open("rock.jpg"))
paper_img1 = ImageTk.PhotoImage(Image.open("paper.jpg"))
scissor_img1 = ImageTk.PhotoImage(Image.open("scissor.jpg"))

rock_img2 = ImageTk.PhotoImage(Image.open("rock.jpg"))
paper_img2 = ImageTk.PhotoImage(Image.open("paper.jpg"))
scissor_img2 = ImageTk.PhotoImage(Image.open("scissor.jpg"))

lab_ply = Label(root, image=scissor_img1)
lab_comp = Label(root, image=scissor_img2)
lab_comp.place(x=0, y=70)
lab_ply.place(x=1040,y=70)

comp_score = Label(root, text=0, font=("cambria",60,"bold"), fg="red", width=5, height=2)
ply_score = Label(root, text=0, font=("cambria",60,"bold"), fg="red", width=5, height=2)
comp_score.place(x=270, y=150)
ply_score.place(x=790, y=150)

ply_ind = Label(root,font=("cambria",40,"bold"), text="PLAYER", bg="orange", fg="blue", height=1, width=15)
comp_ind = Label(root,font=("cambria",40,"bold"), text="COMPUTER", bg="orange", fg="blue", height=1, width=15)

comp_ind.place(x=0, y=0)
ply_ind.place(x=825, y=0)

def msg(m):
  final_message['text'] = m

def comp():
  comp_final = int(comp_score["text"])  
  comp_final += 1
  comp_score["text"] = str(comp_final)

def ply():
  ply_final = int(ply_score["text"])  
  ply_final += 1
  ply_score["text"] = str(ply_final)

def check_winner(p,c):
  if p==c:
    msg("It's a TIE")
  elif p=="rock":
    if c=="paper":
      msg("COMPUTER wins")
      comp()
    else:
      msg("PLAYER wins")
      ply()
  elif p=="paper":
    if c=="scissor":
      msg("COMPUTER wins")
      comp()
    else:
      msg("PLAYER wins")
      ply()
  elif p=="scissor":
    if c=="rock":
      msg("COMPUTER wins")
      comp()
    else:
      msg("PLAYER wins")
      ply()
  else:
    pass

to_select = ["rock", "paper"," scissor"]

def upd_choice(c):
  comp_ch = to_select[random.randint(0,2)]
  if comp_ch == "rock":
    lab_comp.configure(image=rock_img2)
  elif comp_ch == "paper":
    lab_comp.configure(image=paper_img2)
  else:
    lab_comp.configure(image=scissor_img2)
  if c == "rock":
    lab_ply.configure(image=rock_img1)
  elif c == "paper":
    lab_ply.configure(image=paper_img1)
  else:
    lab_ply.configure(image=scissor_img1)
  
  check_winner(c, comp_ch)


final_message = Label(root, font=("cambria",30,"bold"), bg="red", fg="white")
final_message.place(x=500, y=525)

rock_but = Button(root, width=10, height=1, text="ROCK", font=("algerian",30,"bold"), bg="yellow", fg="red", command=lambda:upd_choice("rock"))

paper_but = Button(root, width=10, height=1, text="PAPER", font=("algerian",30,"bold"), bg="yellow", fg="red", command=lambda:upd_choice("paper"))

scissors_but = Button(root, width=10, height=1, text="SCISSORS", font=("algerian",30,"bold"), bg="yellow", fg="red", command=lambda:upd_choice("scissor"))

# rock_but.grid(row=2, column=1, sticky='nsew')
# paper_but.grid(row=2, column=2, sticky='nsew')
# scissors_but.grid(row=2, column=3, sticky='nsew')
rock_but.place(x=231,y=420)
paper_but.place(x=513, y=420)
scissors_but.place(x=795,y=420)


root.mainloop()








