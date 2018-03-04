# This is a game which generats and makes you solve a maze
# Designed in and for linux but there is a high chance it works with other os too
# Created using Python 3.6 and Neovim as my editor

# Modules
import turtle
import math

# Screen setup
main_screen = turtle.Screen()
main_screen.bgcolor("#000000")
main_screen.title("Maze Game")
main_screen.setup(700, 700)
main_screen.bgpic("images/background.gif")

# Register shapes
turtle.register_shape("images/person_right.gif")
turtle.register_shape("images/person_left.gif")
turtle.register_shape("images/trasure.gif")
turtle.register_shape("images/wall.gif")

# Pen
class Pen(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("#ffffff")
        self.penup()
        self.speed(0)

# Player
class Player(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("images/person_right.gif")
        self.color("#2874a6")
        self.penup()
        self.speed(0)
        self.gold = 0
        
    def go_up(self):
        move_to_x = player.xcor()
        move_to_y = player.ycor() + 24

        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)
            
    def go_down(self):
        move_to_x = player.xcor()
        move_to_y = player.ycor() - 24

        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)

    def go_left(self):
        move_to_x = player.xcor() - 24
        move_to_y = player.ycor()

        self.shape("images/person_left.gif")

        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)

    def go_right(self):
        move_to_x = player.xcor() + 24
        move_to_y = player.ycor()

        self.shape("images/person_right.gif")

        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)

    def is_collision(self, other):
        a = self.xcor()-other.xcor()
        b = self.ycor()-other.ycor()
        distance = math.sqrt((a ** 2) + (b ** 2))

        if distance < 5:
            return True
        else:
            return False

class Treasure(turtle.Turtle):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.shape("images/trasure.gif")
        self.color("#d4ac0d")
        self.penup()
        self.speed(0)
        self.gold = 100
        self.goto(x, y)

    def destroy(self):
        self.goto(2000, 2000)
        self.hideturtle()

# Levels list
levels = [""]

# First level
level_1 = [
"XXXXXXXXXXXXXXXXXXXXXXXXX",
"XXXX XXXXXX       XXXX XX",
"XXX   XXXX       XXXX   X",
"XX  P  XX       XXXXX T X",
"XXX     X    XXXXXXX    X",
"XXX         XXXXXXX     X",
"XXXX    X    XXXXX     XX",
"XXX    XX     XXX    XXXX",
"XX    XXX    XXX      XXX",
"X     XXXX    XXXXX     X",
"XX    XXXXX   XXXXXX    X",
"XXX  XXXX     XXX      XX",
"X   XXXXXX   XXXX    XXXX",
"X    XXXXXXXXXXXXXX   XXX",
"XX      XXXXXXXXXXXX   XX",
"XXX       XX   XXXXXX   X",
"XXXX            XXXXX   X",
"XXXXXXXXXXXX     XXX    X",
"XXXXXXXXXXXXX    XXX    X",
"XXX       XXX    XXX    X",
"X                XXX    X",
"XXXX       XXXXXXXX     X",
"XXXXXX   XXXXXXXX      XX",
"XX          XXX       XXX",
"X   XXXXXX          XXXXX",
"XXXXXXXXXXXXXXXXXXXXXXXXX",
]

# Trasure list
treasures = []

# Add maze to list
levels.append(level_1)

# Level Setup Function
def setup_maze(level):
    for y in range (len(level)):
        for x in range(len(level[y])):
            character = level[y][x]
            screen_x = -288 + (x * 24)
            screen_y = 288 - (y * 24)
            
            if character == "X":
                pen.goto(screen_x, screen_y)
                pen.shape("images/wall.gif")
                pen.stamp()
                walls.append((screen_x, screen_y))
        
            if character == "P":
                player.goto(screen_x, screen_y)

            if character == "T":
                treasures.append(Treasure(screen_x, screen_y))
# Class instance
pen = Pen()
player = Player()

# Wall coordinate list
walls = []

# Level setup
setup_maze(levels[1])

# Keyboard Bindings
turtle.listen()
turtle.onkey(player.go_left, "Left")
turtle.onkey(player.go_right, "Right")
turtle.onkey(player.go_up, "Up")
turtle.onkey(player.go_down, "Down")

# Turn off screen updates
main_screen.tracer(0)

# Main game loop
while True:
    for treasure in treasures:
        if player.is_collision(treasure):
            player.gold += treasure.gold
            print("Player Gold: {}".format(player.gold))
            treasure.destroy()
            treasures.remove(treasure)

    main_screen.update()

















