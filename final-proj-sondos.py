import turtle
import random
from pygame import mixer

screen_x = 1366
screen_y = 766
screen = turtle.setup(screen_x, screen_y) #this is the screen.

screen=turtle.Screen()
screen.bgpic("sea.gif")
screen.update()

turtle.tracer(1,1)

mixer.init()

score = 0
score1 = 0

#making the bag.
bags = turtle.Turtle()
bags.penup()

turtle.register_shape("bag.gif")
bags.shape("bag.gif")

#making the player.
player = turtle.Turtle() 
player.pu()
turtle.register_shape("net.gif")
player.shape("net.gif")
######################
player2 = turtle.Turtle() 
player2.pu()
turtle.register_shape("net.gif")
player2.shape("net.gif")


#making the sea turtles.
sea_turtle = turtle.Turtle()
sea_turtle.penup()
sea_turtle.shape("turtle")
sea_turtle_pos = []
sea_turtle_pos.append(sea_turtle.pos())
#print(sea_turtle_pos)
turtle.register_shape("sea-turtle.gif")
sea_turtle.shape("sea-turtle.gif")
 
def rand():
    max_x = 683
    min_x = -683 #min and max edge of the screen.
    return random.randint(min_x,max_x) #random number for bags



bags1 = bags.clone()
bags2 = bags.clone()
bags3 = bags.clone()
sea_turtle.goto(rand(),-300)
sea1 = sea_turtle.clone()
sea2 = sea_turtle.clone()
sea3 = sea_turtle.clone()
sea4 = sea_turtle.clone()
sea5 = sea_turtle.clone()
sea6 = sea_turtle.clone()
sea7 = sea_turtle.clone()
sea8 = sea_turtle.clone()
sea_list = [ sea_turtle, sea1 , sea2, sea3 ,sea4 , sea5 ,sea6, sea7, sea8]
turtle_num = 9

sea1.goto(rand() , -300)
sea2.goto(rand() , -300)
sea3.goto(rand() , -300)
sea4.goto(rand() , -300)
sea5.goto(rand() , -300)
sea6.goto(rand() , -300)
sea7.goto(rand() , -300)
sea8.goto(rand() , -300)
bags1.goto(rand(), -380)
bags2.goto(rand(), -380)
bags3.goto(rand(), -380)
bags.goto(rand() , -380)

bag_list = [bags, bags1, bags2, bags3]
MAX_Y = 380
y_pos = bags.ycor() #gets the y position

#new_y = y_pos - 1 #set it equals to y_pos - 1 to make the droping affect
def game():
    global score,turtle_num, score1
    
    for i in bag_list:
        y_pos = i.pos()[1]
        if y_pos <= -MAX_Y:
            i.ht()
            i.goto(rand() , 394)
        else:
            x,y = i.pos()
            i.goto(x , y -  20)
            i.st()

    #getting the x and y of the turtles
        x_p,y_p = player.pos()
        x_p2,y_p2 = player2.pos()
        #print(x_p2,y_p2)
        x_b,y_b = i.pos()
        if abs(x_p - x_b) < 50 and abs(y_p - y_b) < 50 : #makes the bag disapear if they touch the net
            i.ht()
            i.goto(x_b , -MAX_Y)
            score+=1
            turtle.clear()
            turtle.write(score, font=("Arial", 20))
            mixer.music.load('win_sound.mp3')
            mixer.music.play()
        if abs(x_p2 - x_b) < 50 and abs(y_p2 - y_b) < 50:
            i.ht()
            i.goto(x_b , -MAX_Y)
            score1 +=1
            mixer.music.load('win_sound.mp3')
            mixer.music.play()
        for c in sea_list:
            x_t,y_t = c.pos()

            if (abs(x_b - x_t) < 50) and (abs(y_b - y_t) < 50):   #make the turtle disapear if the bag
                c.ht()                                            #touches it
                turtle_num -= 1
                sea_list.remove(c)
                mixer.music.load("oof.mp3")
                mixer.music.play()
    #print(turtle_num)
    if turtle_num == 1:
        c.speed(1)
        c.goto(rand() , -300)

    if turtle_num == 0:
        quit()


    turtle.clear()
    turtle.write(score, font=("Arial", 20))
    sc.undo()
    sc.write(score1, font=("Arial", 20))

    
    turtle.ontimer(game, 10)    
##############################################################   
def move_left(): #move left function.
    x = player.xcor()
    x = x - 20
    if x < -683: #the player can't go out of the screen.
        x = -683
    player.setx(x) #set the new x

def move_right(): #move right function.   
    x = player.xcor()
    x = x + 20
    if x > 683: #the player can't go out of the screen.
        x = 683
    player.setx(x) #set the new x
def move_up (): # move up function
    y = player.ycor()
    y = y + 20
    if y > 0: # the player can't go up more than 0.
        y = 0
    player.sety(y) #set the new y.
def move_down (): #move up function
    y = player.ycor()
    y = y - 20
    if y <  -200: #the player can't be less then -200
        y = -200
    player.sety(y)
##################################################################
def move_left2(): #move left function.
    x = player2.xcor()
    x = x - 20
    if x < -683: #the player can't go out of the screen.
        x = -683
    player2.setx(x) #set the new x

def move_right2(): #move right function.   
    x = player2.xcor()
    x = x + 20
    if x > 683: #the player can't go out of the screen.
        x = 683
    player2.setx(x) #set the new x
def move_up2 (): # move up function
    y = player2.ycor()
    y = y + 20
    if y > 0: # the player can't go up more than 0.
        y = 0
    player2.sety(y) #set the new y.
def move_down2 (): #move up function
    y = player2.ycor()
    y = y - 20
    if y <  -200: #the player can't be less then -200
        y = -200
    player2.sety(y)

turtle.listen()
turtle.onkey(move_left, 'Left')   #make the turtle move left.
turtle.onkey(move_right, 'Right') #make the turtle move right.
turtle.onkey(move_up, 'Up')       #make the turtle nove up.
turtle.onkey(move_down, 'Down')   #make the turtle go down.
############################################
turtle.listen()
turtle.onkey(move_left2, 'a')   #make the turtle move left.
turtle.onkey(move_right2, 'd') #make the turtle move right.
turtle.onkey(move_up2, 'w')       #make the turtle nove up.
turtle.onkey(move_down2, 's')   #make the turtle go down.






sc = turtle.Turtle()
sc.speed(0)
sc.penup()
sc.goto(-600,300)
sc.ht()
turtle.penup()
turtle.goto(600,300)
sc.write(score1, font=("Arial", 20))
turtle.write(score, font=("Arial", 20))
turtle.ht()
game()
