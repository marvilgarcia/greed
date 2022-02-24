import os
import random
from tkinter.tix import MAX

from game.casting.actor import Actor
from game.casting.artifact import Artifact
from game.casting.cast import Cast

from game.directing.director import Director

from game.services.keyboard_service import KeyboardService
from game.services.video_service import VideoService

from game.shared.color import Color
from game.shared.point import Point


FRAME_RATE = 12
MAX_X = 900
MAX_Y = 600
CELL_SIZE = 15
FONT_SIZE = 15
COLS = 60
ROWS = 40
CAPTION = "Greed"
DATA_PATH = os.path.dirname(os.path.abspath(__file__)) + "/data/messages.txt"
WHITE = Color(255, 255, 255)
DEFAULT_ARTIFACTS = 40 # number of characters on the screen


def main():
    
    # create the cast
    cast = Cast()
    
    # create the banner
    banner = Actor()
    banner.set_text("")
    banner.set_font_size(FONT_SIZE)
    banner.set_color(WHITE)
    banner.set_position(Point(CELL_SIZE, 0))
    cast.add_actor("banners", banner)
    
    # create the robot
    x = int(MAX_X / 2 )
    y = int(MAX_X / -50)
    position = Point(x, y)

    robot = Actor()
    robot.set_text("#")
    robot.set_font_size(FONT_SIZE)
    robot.set_color(WHITE)
    robot.set_position(position)
    cast.add_actor("robots", robot)
    
    # create the artifacts
    #with open(DATA_PATH) as file:
        #data = file.read()
        #messages = data.splitlines()

    seq = [42,111] # gets the ascii characters for * and o
    for n in range(DEFAULT_ARTIFACTS):
        #text = chr(random.randint(33, 126)) # getting the ascii characters to put on the screen.
        text = chr(random.choice(seq))
        #message = messages[n] 

        # need to change to make it so the characters will be at the top. 
        x = random.randint(1, COLS - 1) 
        y = 2 # will make the gems and rocks start from the bottom. 
        position = Point(x, y)
        position = position.scale(CELL_SIZE) # scales the pixel to the appropriate size.

        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        color = Color(r, g, b)
        
        # creating the velocity
        x_v = 0
        y_v = random.randrange(1,10)
        velocity = Point(x_v, y_v)

        artifact = Artifact()
        artifact.set_text(text)
        artifact.set_font_size(FONT_SIZE)
        artifact.set_color(color)
        artifact.set_position(position)
        # changes the velocity
        artifact._velocity = velocity # changes to 0,2
        artifact.move_next(MAX_X, MAX_Y) #makes the velocity work or switches it on. Move next from actor class
        #artifact.set_message(message)
        cast.add_actor("artifacts", artifact)
    
    # start the game
    keyboard_service = KeyboardService(CELL_SIZE)
    video_service = VideoService(CAPTION, MAX_X, MAX_Y, CELL_SIZE, FRAME_RATE)
    director = Director(keyboard_service, video_service)
    director.start_game(cast)


if __name__ == "__main__":
    main()
