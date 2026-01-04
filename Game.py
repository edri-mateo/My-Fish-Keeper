import tkinter as tk  # tkinter is a standard GUI library for Python, tk is an alias for tkinter

# CONSTANTS
HEIGHT = 700
WIDTH = 700

TANK_X1 = 50         # top-left x coordinate
TANK_Y1 = 150        # top-left T coordinate
TANK_X2 = WIDTH-50   # bottom-right x coordinate
TANK_Y2 = 320        # bottom-right y coordinate

BASE_X1 = TANK_X1
BASE_Y1 = TANK_Y2+10 # 10 is the width of the outline stroke
BASE_X2 = TANK_X2
BASE_Y2 = TANK_Y2+100

# create a window
window = tk.Tk()
window.title("•.˚○•°  Home Fishie Home  ∘˙○˚.•")
window.geometry(str(WIDTH) + "x" + str(HEIGHT))


# PHOTOS
BACKGROUND_IMG = tk.PhotoImage(file="/Users/edriellemateo/Documents/VSCODE/Projects/Home Fishie Home/images/background.PNG") # Tkinter only takes in gif, pgm, or ppm (sometimes png) otherwise you need to install Python and Pillow
TANK_IMG = tk.PhotoImage(file="/Users/edriellemateo/Documents/VSCODE/Projects/Home Fishie Home/images/tank.PNG")
DIRT_IMG = tk.PhotoImage(file="/Users/edriellemateo/Documents/VSCODE/Projects/Home Fishie Home/images/dirt.PNG")
DEAD_IMG = tk.PhotoImage(file="/Users/edriellemateo/Documents/VSCODE/Projects/Home Fishie Home/images/dead.PNG")

DECOR1_IMG = tk.PhotoImage(file="/Users/edriellemateo/Documents/VSCODE/Projects/Home Fishie Home/images/decor1.PNG")
DECOR2_IMG = tk.PhotoImage(file="/Users/edriellemateo/Documents/VSCODE/Projects/Home Fishie Home/images/decor2.PNG")
DECOR3_IMG = tk.PhotoImage(file="/Users/edriellemateo/Documents/VSCODE/Projects/Home Fishie Home/images/decor3.PNG")
DECOR4_IMG = tk.PhotoImage(file="/Users/edriellemateo/Documents/VSCODE/Projects/Home Fishie Home/images/decor4.PNG")
DECOR5_IMG = tk.PhotoImage(file="/Users/edriellemateo/Documents/VSCODE/Projects/Home Fishie Home/images/decor5.PNG")
DECOR6_IMG = tk.PhotoImage(file="/Users/edriellemateo/Documents/VSCODE/Projects/Home Fishie Home/images/decor6.PNG")
DECOR7_IMG = tk.PhotoImage(file="/Users/edriellemateo/Documents/VSCODE/Projects/Home Fishie Home/images/decor7.PNG")
DECOR8_IMG = tk.PhotoImage(file="/Users/edriellemateo/Documents/VSCODE/Projects/Home Fishie Home/images/decor8.PNG")
DECOR9_IMG = tk.PhotoImage(file="/Users/edriellemateo/Documents/VSCODE/Projects/Home Fishie Home/images/decor9.PNG")
DECOR10_IMG = tk.PhotoImage(file="/Users/edriellemateo/Documents/VSCODE/Projects/Home Fishie Home/images/decor10.PNG")
DECOR11_IMG = tk.PhotoImage(file="/Users/edriellemateo/Documents/VSCODE/Projects/Home Fishie Home/images/decor11.PNG")
DECOR12_IMG = tk.PhotoImage(file="/Users/edriellemateo/Documents/VSCODE/Projects/Home Fishie Home/images/decor12.PNG")

FISH1_IMG = tk.PhotoImage(file="/Users/edriellemateo/Documents/VSCODE/Projects/Home Fishie Home/images/fish1.PNG")
FISH2_IMG = tk.PhotoImage(file="/Users/edriellemateo/Documents/VSCODE/Projects/Home Fishie Home/images/fish2.PNG")
FISH3_IMG = tk.PhotoImage(file="/Users/edriellemateo/Documents/VSCODE/Projects/Home Fishie Home/images/fish3.PNG")
FISH4_IMG = tk.PhotoImage(file="/Users/edriellemateo/Documents/VSCODE/Projects/Home Fishie Home/images/fish4.PNG")
FISH5_IMG = tk.PhotoImage(file="/Users/edriellemateo/Documents/VSCODE/Projects/Home Fishie Home/images/fish5.PNG")
FISH6_IMG = tk.PhotoImage(file="/Users/edriellemateo/Documents/VSCODE/Projects/Home Fishie Home/images/fish6.PNG")
FISH7_IMG = tk.PhotoImage(file="/Users/edriellemateo/Documents/VSCODE/Projects/Home Fishie Home/images/fish7.PNG")
FISH8_IMG = tk.PhotoImage(file="/Users/edriellemateo/Documents/VSCODE/Projects/Home Fishie Home/images/fish8.PNG")
FISH9_IMG = tk.PhotoImage(file="/Users/edriellemateo/Documents/VSCODE/Projects/Home Fishie Home/images/fish9.PNG")
FISH10_IMG = tk.PhotoImage(file="/Users/edriellemateo/Documents/VSCODE/Projects/Home Fishie Home/images/fish10.PNG")
FISH11_IMG = tk.PhotoImage(file="/Users/edriellemateo/Documents/VSCODE/Projects/Home Fishie Home/images/fish11.PNG")

BUTTONCART_IMG = tk.PhotoImage(file="/Users/edriellemateo/Documents/VSCODE/Projects/Home Fishie Home/images/buttoncart.PNG")
BUTTONCLEAN_IMG = tk.PhotoImage(file="/Users/edriellemateo/Documents/VSCODE/Projects/Home Fishie Home/images/buttonclean.PNG")
BUTTONDECOR_IMG = tk.PhotoImage(file="/Users/edriellemateo/Documents/VSCODE/Projects/Home Fishie Home/images/buttondecor.PNG")
BUTTONFEED_IMG = tk.PhotoImage(file="/Users/edriellemateo/Documents/VSCODE/Projects/Home Fishie Home/images/buttonfeed.PNG")
BUTTONFISH_IMG = tk.PhotoImage(file="/Users/edriellemateo/Documents/VSCODE/Projects/Home Fishie Home/images/buttonfish.PNG")
BUTTONMUSIC_IMG = tk.PhotoImage(file="/Users/edriellemateo/Documents/VSCODE/Projects/Home Fishie Home/images/buttonmusic.PNG")
BUTTONSHOP_IMG = tk.PhotoImage(file="/Users/edriellemateo/Documents/VSCODE/Projects/Home Fishie Home/images/buttonshop.PNG")
BUTTONTRASH_IMG = tk.PhotoImage(file="/Users/edriellemateo/Documents/VSCODE/Projects/Home Fishie Home/images/buttontrash.PNG")

# create a canvas
canvas = tk.Canvas(window, height=HEIGHT, width=WIDTH)
canvas.create_image(0, 80, image=BACKGROUND_IMG, anchor="nw") # anchor="nw" means the image's top-left corner will be at (0,0)
menu_bar = tk.Frame(window, bg="beige", height=100, width=WIDTH).place(x=0, y=0) # .place() adds your widget to the window without taking up space (overalps instead of padding)
canvas.create_image(7, 35, image=TANK_IMG, anchor="nw")
canvas.create_image(310, 300, image=FISH1_IMG, anchor="nw") #80x--
canvas.create_image(200, 450, image=DECOR1_IMG, anchor="nw") #100x--



# draw shapes
#tank = canvas.create_rectangle([TANK_X1, TANK_Y1], [TANK_X2, TANK_Y2], outline="skyblue4", width=10, fill="lightblue")
#base = canvas.create_rectangle([BASE_X1, BASE_Y1], [BASE_X2, BASE_Y2], outline="burlywood3", width=10, fill="burlywood1") 

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

# shop button
button_shop = tk.Label(window, image=BUTTONSHOP_IMG, bg="beige")
button_shop.place(x=15, y=11)
# decorate tank button
button_decorate = tk.Label(window, image=BUTTONDECOR_IMG, bg="beige")
button_decorate.place(x=30+100, y=12)
# feed button
button_feed = tk.Label(window, image=BUTTONFEED_IMG, bg="beige")
button_feed.place(x=145+100, y=11)
# clean tank button
button_clean = tk.Label(window, image=BUTTONCLEAN_IMG, bg="beige")
button_clean.place(x=255+100, y=16)
# fish button
button_fish = tk.Label(window, image=BUTTONFISH_IMG, bg="beige")
button_fish.place(x=370+100, y=14)
# trash button
button_trash = tk.Label(window, image=BUTTONTRASH_IMG, bg="beige")
button_trash.place(x=480+100, y=14)
# music button
button_music = tk.Label(window, image=BUTTONMUSIC_IMG, bg="#f6d29b")
button_music.place(x=455+112, y=622)


canvas.pack() # add the canvas to the window
window.mainloop() # run the application