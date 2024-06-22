from tkinter import * 
from PIL import Image, ImageTk
import subprocess

def launch_game1():
    subprocess.Popen(["python", "snake.py"])

def launch_game2():
    subprocess.Popen(["python", "game.py"])

root = Tk()
root.title("Gaming Platform")
root.config(bg="black")
root.geometry("1300x600")

bg_image = Image.open("D:\Game\Game Zone.jpg")
bg_image = bg_image.resize((root.winfo_screenwidth(), root.winfo_screenheight()))
background = ImageTk.PhotoImage(bg_image)
background_label = Label(root, image=background)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

snake_img = Image.open("D:\Game\snakelogo.jpg")
snake_res = snake_img.resize((250,250))
snake = ImageTk.PhotoImage(snake_res)
button_game1 = Button(root, image=snake, command=launch_game1)
button_game1.place(x=40, y=320)

rock_img = Image.open("D:\Game\\rocklogo.png")
rock_res = rock_img.resize((250,250))
rock = ImageTk.PhotoImage(rock_res)
button_game2 = Button(root, image=rock, command=launch_game2)
button_game2.place(x=1003, y=320)

root.mainloop()
