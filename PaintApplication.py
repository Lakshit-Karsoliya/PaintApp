import PIL
import tkinter
from PIL import Image,ImageDraw,ImageTk
from tkinter.messagebox import *
from tkinter.colorchooser import askcolor
from tkinter import *

root=Tk()

#variables
canvas_height=700
canvas_width=700
canvas_color='#ffffff'
pen_color='#000000'
x,y=0,0
pointer_size=1
var=0

root.title('PaintApp')
root.minsize(width=700,height=700)
root.resizable(0,0)

canvas=Canvas(root,height=canvas_height,width=canvas_width,bg=canvas_color)
canvas.pack()

#creating a blank image
image1=PIL.Image.new(mode="RGB",size=(canvas_height,canvas_width),color=canvas_color)

def saveImage():
	global var
	filename='PaintAppCanvas'+str(var)+'.png'
	image1.save(filename)
	showinfo(title='Info',message='canvas saved')
	var+=1

def initiallyxy(event):
	global x,y
	x,y=event.x,event.y
def allcords(event):
	global x,y
	global pointer_size
	pointer_size=scale.get()
	canvas.create_line(x,y,event.x,event.y,width=pointer_size,fill=pen_color,smooth=TRUE,capstyle=ROUND)
	#drawing parallel to canvas in image
	draw=ImageDraw.Draw(image1)
	draw.line([(x,y),(event.x,event.y)],width=pointer_size,fill=pen_color,joint='curve')
	x,y=event.x,event.y

root.bind("<Button-1>",initiallyxy)
root.bind("<B1-Motion>",allcords)

def clear():
	canvas.delete("all")
	draw=ImageDraw.Draw(image1)
	draw.rectangle([0,0,canvas_height,canvas_width],fill='white')
def eraser():
	global pen_color
	pen_color="white"
def clrbox():
	top=Toplevel()
	top.title('ColorBox')
	top.resizable(0,0)
	#we cannot pass direct argument se i use lambda
	#color-Buttons
	black=Button(top,text="black",command=lambda:Color('black',top),bg='black',fg='white',width=6)
	black.grid(row=0,column=0)
	blue=Button(top,text="blue",command=lambda:Color('blue',top),bg='blue',fg='white',width=6)
	blue.grid(row=1,column=0)
	red=Button(top,text="Red",command=lambda:Color('red',top),bg='red',fg='white',width=6)
	red.grid(row=2,column=0)
	green=Button(top,text="Green",command=lambda:Color('green',top),bg='green',fg='white',width=6)
	green.grid(row=0,column=1)
	yellow=Button(top,text="Yellow",command=lambda:Color('yellow',top),bg='yellow',fg='black',width=6)
	yellow.grid(row=1,column=1)
	brown=Button(top,text="Brown",command=lambda:Color('brown',top),bg='brown',fg='white',width=6)
	brown.grid(row=2,column=1)
	
	top.mainloop()

def Color(color,top):
	global pen_color
	pen_color=color
	top.destroy()

def chooseColor():
	global pen_color
	pen_color=askcolor()[1]

def about():
	showinfo(title='About',message='This is a simple Paint App \nHaving some functionality like \nClear: To clear screen\nErase: To use eraser tool\nColor: Having 6 Color options\nColorBox:To create Custom color \nSlider: To control pointer size\nSave: To save canvas\n\nDeveloped By: Lakshit Karsoliya\n\nIf you found any bug here is my github\nhttps://github.com/Lakshit-Karsoliya\n')

scale=Scale(root,label="pointer size",from_=1,to=10,orient=HORIZONTAL,length=500,showvalue=0)
scale.pack()

	
menubar=Menu(root,bg='lightblue',fg='black',activebackground='lightblue',activeforeground='black',relief=FLAT,activeborder=0)

menubar.add_command(label="Clear",command=clear)

menubar.add_command(label="Eraser",command=eraser)

menubar.add_command(label="Color",command=clrbox)

menubar.add_command(label="ColorBox",command=chooseColor)

menubar.add_command(label="Save",command=saveImage)

menubar.add_command(label="About",command=about)

menubar.add_command(label="Quit",command=quit)

root.config(menu=menubar)	

root.mainloop()