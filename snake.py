
from tkinter import*
from PIL import Image, ImageTk
import random

def start_game():
  global im, b1, b2
  # Buttons for players
  b1.place(x=650,y=150)

  b2.place(x=825,y=150)

  #exit button
  b=Button(root,text="EXIT",height=2,width=16,fg="black",bg="gray",font=("jokerman",20,"bold"),activebackground="red",command=root.destroy)
  b.place(x=650,y=20)

  #dice image to show
  im=Image.open("D:/Game/DiceFull.jpg")
  im=im.resize((200,200))
  im=ImageTk.PhotoImage(im)
  b=Button(root,image=im,height=200,width=200)
  b.place(x=700,y=350)

def reset_coins():
  global player_1 , player_2, pos1, pos2
  player_1.place(x=0,y=570)
  player_2.place(x=50,y=570)
  pos1=0
  pos2=0

def load_dice_images():
  global Dice
  names=["Dice1.png","Dice2.png","Dice3.png","Dice4.png","Dice5.png","Dice6.png"]
  for nam in names:
    im=Image.open("D:/Game/" + nam)
    im=im.resize((200,200))
    im=ImageTk.PhotoImage(im)
    Dice.append(im)

def check_ladder(Turn):
  global pos1, pos2, Ladder
  f=0  # No ladder
  if Turn==1:
    if pos1 in Ladder:
      pos1 = Ladder[pos1]
      f=1
  else:
    if pos2 in Ladder:
      pos2 = Ladder[pos2]   
      f=1
  return f 

def check_snake(Turn):
  global pos1, pos2
  if Turn==1:
    if pos1 in Snake:
      pos1 = Snake[pos1]
  else:
    if pos2 in Snake:
      pos2 = Snake[pos2]

def roll_dice():
  global Dice, turn, pos1, pos2, b1, b2
  r = random.randint(1, 6)
  b3=Button(root,image=Dice[r-1],height=200,width=200)
  b3.place(x=700,y=350)
  
  Lad=0
  if turn == 1:
    if (pos1+r)<=100:
      pos1=pos1+r
    Lad = check_ladder(turn)
    check_snake(turn)
    move_coin(turn, pos1)
    if r!=6 and Lad!=1:
      turn = 2
      b1.configure(state='disabled')
      b2.configure(state='normal')
  else:
    if (pos2+r)<=100:
      pos2=pos2+r
    Lad = check_ladder(turn)
    check_snake(turn)
    move_coin(turn, pos2)
    if r!=6 and Lad!=1:
      turn = 1
      b2.configure(state='disabled')
      b1.configure(state='normal')

  is_winner()

def is_winner():
  global pos1, pos2
  if pos1==100:
    msg = "Player 1 is the WINNER!!"
    Lab = Label(root, text=msg, height=2, width=20, bg="red", font=('Cursive', 30, 'bold'))
    Lab.place(x=300,y=300)
    reset_coins()
  elif pos2==100:
    msg = "Player 2 is the WINNER!!"
    Lab = Label(root, text=msg, height=2, width=20, bg="red", font=('Cursive', 30, 'bold'))
    Lab.place(x=300,y=300)
    reset_coins()

def move_coin(Turn, r):
  global player_1, player_2, Index
  if Turn == 1:
    player_1.place(x=Index[r][0], y=Index[r][1])
  else:
    player_2.place(x=Index[r][0], y=Index[r][1])


def get_Index():
  global player_1, player_2, Index
  Num=[100,99,98,97,96,95,94,93,92,91,81,82,83,84,85,86,87,88,89,90,80,79,78,77,76,75,74,73,72,71,61,62,63,64,65,66,67,68,69,70,60,59,58,57,56,55,54,53,52,51,41,42,43,44,45,46,47,48,49,50,40,39,38,37,36,35,34,33,32,31,21,22,23,24,25,26,27,28,29,30,20,19,18,17,16,15,14,13,12,11,1,2,3,4,5,6,7,8,9,10]
  row=20
  i=0
  for x in range(1,11):
    col=14
    for y in range(1,11):
      Index[Num[i]] = (col,row)
      col=col+57
      i=i+1
    row=row+57
  print(Index)

# To store Dice images
Dice = []

# To store x and y coordinates of given number
Index = {}

#Initial positions of players
pos1=None
pos2=None

# Ladder bottom to top
Ladder = {8:31, 7:14, 15:26, 2:38, 21:42, 28:84, 36:44, 51:67, 71:91, 78:98, 87:94}

# Snakes head to tail
Snake = {99:80, 95:75, 92:88, 89:68, 74:54, 64:60, 62:19, 46:25, 49:11, 16:6}

root = Tk()
root.config(bg="green")
root.geometry("1000x600")
root.title("SNAKE AND LADDER GAME")
#root.resizable(width=True, height=True)

f1 = Frame(root, width=1200, height=800, relief='raised', bg="green")
f1.place(x=0, y=0)

# Set Board
img = Image.open("D:/Game/snake_ and_ ladder_ board.png")
resized_img = img.resize((560, 560),)
img1 = ImageTk.PhotoImage(resized_img)
Lab = Label(f1, image=img1)
Lab.place(x=0, y=0)

# Player 1 button
ply1_img = Image.open("D:\Game\ply1.jpg")
img_1res = ply1_img.resize((150,150))
img_1 = ImageTk.PhotoImage(img_1res)
b1 = Button(root, image=img_1, command=roll_dice)

# Player 2 button
ply2_img = Image.open("D:\Game\ply2.jpg")
img_2res = ply2_img.resize((150,150))
img_2 = ImageTk.PhotoImage(img_2res)
b2 = Button(root, image=img_2, command=roll_dice)

# Player 1 coin
player_1=Canvas(root,width=20,height=20, bg="blue")
player_1.create_oval(3,3,20,20,fill="blue")

# Player 2 coin
player_2=Canvas(root,width=20,height=20, bg="red")
player_2.create_oval(3,3,20,20,fill="red")

# Whose turn first
turn = 1

# Load dice images
load_dice_images()

#K Keep coins at initial position
reset_coins()

#Get index of each number
get_Index()

# Setting all buttons
start_game()

root.mainloop()