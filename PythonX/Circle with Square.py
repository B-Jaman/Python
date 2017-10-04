
import turtle

my_game=turtle.Turtle()

def game(length,angle):
    my_game.forward(length)
    my_game.right(angle)
    my_game.forward(length)
    my_game.right(angle)
    my_game.forward(length)
    my_game.right(angle)
    my_game.forward(length)
   
for i in range(50):
    game(100,90)
    my_game.right(105)

