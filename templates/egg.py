from itertools import cycle
from random import randrange
from tkinter import Tk,Canvas,messagebox,font

canvas_height=400
canvas_width=800

win=Tk()
c=Canvas(win,width=canvas_width,height=canvas_height,background='deep sky blue')
c.create_rectangle(-5,canvas_height -100,canvas_width+5,canvas_height+5,fill='sea green',width='0')
c.create_oval(-80,-80,120,120,fill='orange',width=0)
c.pack()
color_cycle=cycle(['light blue','light pink','red','light green'])
egg_width=45
egg_height=55
egg_score=10
egg_speed=1000
interval=4000
difficulty_factor=100

catcher_color='dark blue'
catcher_width=100
catcher_height=100
catcher_start_x=canvas_width/2 - catcher_width/2
catcher_start_y=canvas_height-catcher_height-20
catcher_start_x2=catcher_start_x + catcher_width
catcher_start_y2=catcher_start_y+catcher_height
catcher=c.create_arc(catcher_start_x,catcher_start_y,catcher_start_x2,catcher_start_y2,start=200,extent=140,style='arc',outline=catcher_color,width=3)

score=0
score_text=c.create_text(10,10,anchor='nw', font=('Arial',18,'bold'),fill='darkblue',text='Score:'+ str(score))
live_remain=3
lives_text =c.create_text(canvas_width-10,10,anchor='ne', font=('Arial',18,'bold'),fill='darkblue',text='Lives:'+ str(live_remain))

eggs=[]
def create_eggs():
    x=randrange(10,740)
    y=40
    new_egg=c.create_oval(x,y,x+egg_width,y+egg_height,fill=next(color_cycle),width='0')
    eggs.append(new_egg)
    win.after(interval, create_eggs)
def move_eggs():
    for egg in eggs:
        (egg_x,egg_y,egg_x2,egg_y2)=c.coords(egg)
        c.move(egg,0,10)
        if egg_y2>canvas_height:
            egg_dropped(egg)
    win.after(egg_speed,move_eggs)        
def egg_dropped(egg):
    eggs.remove(egg)
    c.delete(egg)
    lose_life()
    if live_remain==0:
        messagebox.showinfo('Game over!','Final score:'+ str(score))
        win.destroy()
def lose_life():
    global live_remain
    live_remain -= 1
    c.itemconfigure(lives_text,text='Lives :'+str(live_remain))   

def catch_check():
    (catcher_x,catcher_y,catcher_x2,catcher_y2)=c.coords(catcher)
    for egg in eggs:
     (egg_x,egg_y,egg_x2,egg_y2)=c.coords(egg)
     if(catcher_x < egg_x and egg_x2< catcher_x2 and catcher_y2 -egg_y2<40):
        eggs.remove(egg)
        c.delete(egg)
        increase_score(egg_score)
    win.after(100,catch_check)
def increase_score(points):
    global score,egg_speed,interval
    score += points
    print("Executed" + str(score))
    egg_speed=int(egg_speed+difficulty_factor)
    interval=int(interval+difficulty_factor)
    c.itemconfigure(score_text,text='Score:' + str(score))
def move_left(event):
    global catcher
    (x1,y1,x2,y2)=c.coords(catcher)
    if(x1>0):
        c.move(catcher,-20,0)

def move_rigth(event):
    global catcher
    (x1,y1,x2,y2)=c.coords(catcher)
    if x2<canvas_width:
        c.move(catcher,20,0)

c.bind('<Left>',move_left)
c.bind('<Right>',move_rigth)
c.focus_set()

win.after(1000,create_eggs)
win.after(1000,move_eggs)
win.after(1000,catch_check)

win.mainloop()