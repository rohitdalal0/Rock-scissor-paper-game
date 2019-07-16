import random
import turtle



# This is turtle
def _win_():
  color = ["#"+''.join([random.choice('0123456789ABCDEF') for j in range(6)]) for i in range(1)]

  baby = turtle.Turtle()
  baby.speed(20)
  baby.color(color)
  baby.pensize(5)

  # creating Y
  baby.penup()
  baby.left(180)
  baby.forward(200)
  baby.pendown()
  baby.right(110)
  baby.forward(50)
  baby.left(45)
  baby.forward(50)
  baby.backward(50)
  baby.right(45)
  baby.forward(50)
  baby.penup()
  baby.right(45)
  baby.forward(10)
  baby.right(120)
  baby.forward(60)
  baby.pendown()

  # creating O
  baby.circle(30)
  # creating U
  baby.left(90)
  baby.penup()
  baby.forward(70)
  baby.pendown()
  baby.left(90)
  baby.forward(50)
  baby.right(180)
  baby.forward(70)
  baby.left(30)
  baby.forward(10)
  baby.left(60)
  baby.forward(30)
  baby.left(40)
  baby.forward(10)
  baby.left(50)
  baby.forward(70)

  # turtle going over U
  baby.penup()
  baby.forward(30)
  baby.pendown()

  baby.right(90)
  baby.penup()
  baby.forward(60)

  # Going to create
  baby.right(90)
  baby.forward(100)
  baby.left(90)
  baby.pendown()
  # creating W
  baby.left(90)
  baby.forward(100)
  baby.right(180)
  baby.forward(100)
  baby.left(120)
  baby.forward(50)
  baby.right(50)
  baby.forward(50)
  baby.left(110)
  baby.forward(100)

  baby.penup()

  # this is ' I ' and direction change
  baby.right(90)
  baby.forward(20)
  baby.right(90)
  baby.pendown()
  baby.forward(100)
  baby.penup()

  # direction change
  baby.left(90)
  baby.forward(20)
  baby.left(90)
  baby.pendown()


  # making N
  baby.forward(100)
  baby.right(140)
  baby.forward(100)
  baby.left(130)
  baby.forward(150)

# This is end of making " You win "




things_name=['rock', 'paper', 'scissor']

# computer will auto select here
computer=random.choice(things_name)
print('<<-- rock, paper, scissor -->>')

# Here, I'm getting data form user

human=input("Enter Name :: ")

# scores
human_score=0
computer_score=0

# This is function for calling
def game_start():
  if human==computer:
    print("Tie ------------------------------>>>>>>")
    print("|Computer Score :"+ str(int(computer_score)) +"||Human Score :" +str(int(human_score)))

  elif human=='rock':
    if computer=='paper':
      print('You lose')
    else:
      human_score + 1
      _win_()
    
  if human=='paper':
    if computer=='scissor':
      print('You lose')
      computer_score + 1
    else:
      human_score+1
      _win_()

  if human=='scissor':
    if computer=='paper':
      human_score + 1
      _win_()
    else:
      print('You lose')
      computer_score + 1

game_start()
print('<<<<<<-----We are working On it-------please, Callback by yourself----->>>>>>')


