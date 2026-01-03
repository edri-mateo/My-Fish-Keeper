import tkinter as tk  # tkinter is a standard GUI library for Python, tk is an alias for tkinter

# create a window
window = tk.Tk()
window.title("•.˚○•°  Home Fishie Home  ∘˙○˚.•")
window.geometry("500x500")

# CONSTANTS
HEIGHT = 500
WIDTH = 500

TANK_X1 = 50         # top-left x coordinate
TANK_Y1 = 150        # top-left T coordinate
TANK_X2 = WIDTH-50   # bottom-right x coordinate
TANK_Y2 = 320        # bottom-right y coordinate

BASE_X1 = TANK_X1
BASE_Y1 = TANK_Y2+10 # 10 is the width of the outline stroke
BASE_X2 = TANK_X2
BASE_Y2 = TANK_Y2+100

# PHOTOS
BACKGROUND_IMG = tk.PhotoImage(file="/Users/edriellemateo/Documents/VSCODE/Projects/Home Fishie Home/background_room_test.gif") # Tkinter only takes in gif, pgm, or ppm (sometimes png) otherwise you need to install Python and Pillow
#FISH_IMG = tk.PhotoImage(file="path_to_fish_image.gif")


# create a canvas
canvas = tk.Canvas(window, height=HEIGHT, width=WIDTH)
canvas.create_image(0, 0, image=BACKGROUND_IMG, anchor="nw") # anchor="nw" means the image's top-left corner will be at (0,0)
menu_bar = tk.Frame(window, bg="lightblue", height=70, width=WIDTH).place(x=0, y=0) # .place() adds your widget to the window without taking up space (overalps instead of padding)

# draw shapes
tank = canvas.create_rectangle([TANK_X1, TANK_Y1], [TANK_X2, TANK_Y2], outline="skyblue4", width=10, fill="lightblue")
base = canvas.create_rectangle([BASE_X1, BASE_Y1], [BASE_X2, BASE_Y2], outline="burlywood3", width=10, fill="burlywood1") 

# BUTTON HANDLERS
# def feed_fish():
# def clean_tank():
# def decorate_tank():
# def play_with_fish():

# FUNCTIONS
# def update_happiness():
# def update_hunger():
# def update_cleanliness():
# def check_num_fish(): -> minimum of 1 fish
# def check_money(): -> minimum of 0 money
# def if_dead(): -> fish dies if hunger = 0 or cleanliness = 0
# def save_game():
# def load_game():

# MENU
# fish profile
# file to load game
# button to save game
# settings (music on/off)
# help/instructions
# shopping 
    # decorations
    # food
    # other fish 
    # sell fish for money -> must have at least 1 fish


bubble_style = { # we will add this styling to all buttons using (**, which unpacks the array and integrates it into the line of code where we make our button) 
    "font": ("Bubblegum", 15, "bold"),
    "fg": "#5A7CB6",        # text colour
    "highlightbackground": "#385281",  # border color (macOS)
    "highlightthickness": 2,
    "padx": 14,
    "pady": 8,
    "cursor": "hand"
}


# ---- BUTTONS ----
# feed button
feed_button = tk.Button(window, text="Feed \nFish", **bubble_style).place(x=40, y=10)  # .place() allows precise placement using x and y coordinates
# clean tank button
clean_tank = tk.Button(window, text="Clean \nTank", **bubble_style).place(x=140, y=10) 
# decorate tank button
decorate_button = tk.Button(window, text="Decorate \nTank", **bubble_style).place(x=245, y=10) 
# play with fish button
play_button = tk.Button(window, text="Play \nwith Fish", **bubble_style).place(x=370, y=10) 


canvas.pack() # add the canvas to the window
window.mainloop() # run the application
