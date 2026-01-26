import tkinter # for the interface  and the graphics
import random  # for random food placement


ROWS = 25 # no. of rows
COLMS = 25 # no. of columbs
TILE_SIZE = 25 # no. of pixelks in the single tile

#  the game window size
WINDOW_WIDTH = COLMS * TILE_SIZE
WINDOW_HEIGHT = ROWS * TILE_SIZE

class tile :
    def __init__(self, x, y):
        self.x = x
        self.y = y

#game window 
window = tkinter.Tk() # this is going to open up a window 
window.title("sanke game")
window.resizable(False, False) # to disable the resizing of the window

canvas = tkinter.Canvas(window, bg = 'black', width = WINDOW_WIDTH, height = WINDOW_HEIGHT, borderwidth= 0, highlightthickness=0) # creating a canvas for the game

canvas.pack()

window.update()

# make the window appear in the center of the screen
window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

#formula for centering the window
window_x = int((screen_width/2) - (window_width/2))
window_y = int((screen_height/2) - (window_height/2))

window.geometry(f"{window_width}x{window_height}+{window_x}+{window_y}")


#the game :
snake = tile(5*TILE_SIZE, 5*TILE_SIZE) # tile for sanke's head
food =  tile(15*TILE_SIZE, 15*TILE_SIZE) # tile for food
def draw():
    global snake
    #draw the snake
    canvas.create_rectangle(snake.x, snake.y, snake.x + TILE_SIZE, snake.y + TILE_SIZE, fill="green")
    
    #draw the food
    canvas.create_oval(food.x, food.y, food.x + TILE_SIZE, food.y + TILE_SIZE, fill="red")
    
    
    window.after(100, draw) #  100ms meaning 10 frames / sec

draw()








window.mainloop()



