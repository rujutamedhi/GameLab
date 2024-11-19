import turtle as t
import random as rd
import time as ti
import requests
t.bgcolor('yellow')
caterpillar=t.Turtle()
caterpillar.shape('square')
caterpillar.speed(0)
caterpillar.penup()
caterpillar.hideturtle()
leaf=t.Turtle()
leaf_shape=((0,0),(14,2),(18,6),(20,20),(6,18),(2,14))
t.register_shape('leaf',leaf_shape)
leaf.shape('leaf')
leaf.color('green')
leaf.penup()
leaf.speed()
leaf.hideturtle()

text_turtle=False
text_turtle=t.Turtle()
text_turtle.write('Press space to start',align='center',font=('Arial',18,'bold'))
text_turtle.hideturtle()
score_turtle=t.Turtle()
score_turtle.hideturtle()
score_turtle.speed(0)

ti.sleep(3)

def outside_window():
    left_wall=-t.window_width()/2
    right_wall=t.window_width()/2
    top_wall=t.window_height()/2
    bottom_wall=-t.window_height()/2
    (x,y)=caterpillar.pos()
    outside= x<left_wall or x>right_wall or y< bottom_wall or y>top_wall
    return outside
def place_leaf():
    leaf.hideturtle()
    leaf.setx(rd.randint(-200,200))
    leaf.sety(rd.randint(-200,200))
    leaf.showturtle()
def game_over():
    caterpillar.color('yellow')
    leaf.color('yellow')
    t.penup()
    t.hideturtle()
    t.write('GAME OVER',align='center',font=('Ariel',30,'bold'))

def display_score(current_score):
    score_turtle.clear()
    score_turtle.penup()
    x=(t.window_width()/2) - 50
    y=(t.window_height()/2) - 50
    score_turtle.setpos(x,y)
    score_turtle.write('Score:',str(current_score),font=('Ariel',20),align='right')
    score_turtle.write(str(current_score),font=('Ariel',20),align='left')
game_started=0
def submit_final_score( username,final_score):
    # Define the URL of the Flask application route
    url = 'http://localhost:5000/submit_snake_score'  # Adjust the URL as needed

    # Create a dictionary containing the data to send
    data = {
        'name':username,
        'score': final_score
        
    }
    print("score",final_score)
    response = requests.post(url, json=data)

    # Check the response status
    if response.status_code == 200:
        print("Score submitted successfully.")
    else:
        print("Failed to submit score. Error:", response.text)
def start_game():
    global game_started
    if game_started:
        return
    game_started =True
    score=0
    text_turtle.clear()
    caterpillar_speed=2
    caterpillar_length=3
    caterpillar.shapesize(1,caterpillar_length,1)
    caterpillar.showturtle()
    display_score(score)
    place_leaf()
    while True:
        caterpillar.forward(caterpillar_speed)
        if caterpillar.distance(leaf)<20:
            place_leaf()
            caterpillar_length=caterpillar_length+1
            caterpillar.shapesize(1,caterpillar_length,1)
            caterpillar_speed=caterpillar_speed+1
            score=score+10
            display_score(score)
        if outside_window():
            submit_final_score("rutu",score)
            game_over()
            break
def move_up():
    if caterpillar.heading()==0 or caterpillar.heading()==180:
     caterpillar.setheading(90)
def move_down():
    if caterpillar.heading()==0 or caterpillar.heading()==180:
     caterpillar.setheading(270)
def move_left():
    if caterpillar.heading()==90 or caterpillar.heading()==270:
     caterpillar.setheading(180)
def move_right():
    if caterpillar.heading()==90 or caterpillar.heading()==270:
     caterpillar.setheading(0)


t.onkey(start_game,'space')
t.onkey(move_up,'Up')
t.onkey(move_down,'Down')
t.onkey(move_left,'Left')
t.onkey(move_right,'Right')
t.listen()
t.mainloop()
