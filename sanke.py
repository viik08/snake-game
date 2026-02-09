import tkinter # for the interface  and the graphics
import random  # for random food placement


ROWS = 25 # no. of rows
COLMS = 25 # no. of columbs
TILE_SIZE = 25 # no. of pixels in the single tile

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
snake_body = [] # snake tiles

velocity_x = 0
velocity_y = 0

game_over = False
score = 0

def change_direction(e): # e = event
    #print(e)
    #print(e.keysym)
    if(game_over):
        return
    
    global velocity_x, velocity_y
    if (e.keysym == "Up" and velocity_y !=1):
        velocity_x = 0
        velocity_y = -1
    elif (e.keysym == "Down" and velocity_y !=-1):
        velocity_x = 0
        velocity_y = 1
    elif (e.keysym == "Left" and velocity_x !=1):
        velocity_x = -1
        velocity_y = 0
    elif (e.keysym == "Right" and velocity_x !=-1):
        velocity_x = 1
        velocity_y = 0
    elif (e.keysym == "w" and velocity_y !=1):
        velocity_x = 0
        velocity_y = -1
    elif (e.keysym == "s" and velocity_y !=-1):
        velocity_x = 0
        velocity_y = 1
    elif (e.keysym == "a" and velocity_x !=1):
        velocity_x = -1
        velocity_y = 0
    elif (e.keysym == "d" and velocity_x !=-1):
        velocity_x = 1
        velocity_y = 0


def move_snake():
    global snake,snake_body ,food, game_over,score
    if game_over:
        return
    
    if(snake.x < 0 or snake.x >=WINDOW_WIDTH or snake.y < 0 or snake.y >= WINDOW_HEIGHT):
        game_over = True
        return
    for part in snake_body:
        if(snake.x == part.x and snake.y == part.y):
            game_over = True
            return
    
    
    #collision with the tiles
    if(snake.x == food.x and snake.y == food.y):
        snake_body.append(tile(food.x,food.y))
        
        #adding the food
        food.x = random.randint(0, COLMS-1) * TILE_SIZE
        food.y = random.randint(0, ROWS-1) * TILE_SIZE
        #score updates when food waten
        score += 1
    #updating the snake body after the movement
    for i in range(len(snake_body)-1,-1,-1):
        part = snake_body[i]
        
        if (i == 0):
            part.x= snake.x
            part.y = snake.y
        else:
            prev_part = snake_body[i-1]
            part.x = prev_part.x
            part.y = prev_part.y
            
    snake.x += velocity_x * TILE_SIZE
    snake.y += velocity_y * TILE_SIZE


def draw():
    global snake , snake_body, food, game_over,score
    move_snake()
    
    canvas.delete("all") # clear the canvas before redrawing everything
    
    #draw the food
    canvas.create_oval(food.x, food.y, food.x + TILE_SIZE, food.y + TILE_SIZE, fill="red")
    
    #draw the snake
    canvas.create_rectangle(snake.x, snake.y, snake.x + TILE_SIZE, snake.y + TILE_SIZE, fill="green")
    
    
    for tile in snake_body:
        canvas.create_rectangle(tile.x, tile.y, tile.x + TILE_SIZE, tile.y + TILE_SIZE, fill="green")
    
    if(game_over):
        canvas.create_text(WINDOW_WIDTH/2, WINDOW_HEIGHT/2, text=f"Game Over \n Score: {score}", fill="white", font=("Arial", 24))
    else:
        canvas.create_text(30, 20, text=f"Score: {score}", fill="white", font=("Arial", 12))
    window.after(120, draw) #  100ms meaning 10 frames / sec (increase the value slow the game )

draw()

window.bind("<KeyRelease>",change_direction) # for changing  the direction

window.mainloop()
