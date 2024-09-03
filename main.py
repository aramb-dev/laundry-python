# The Laundry Collector Game program

from tkinter import *
import random

# make window
window = Tk()
window.title('The Laundry Collector Game')

# create a canvas to put objects on the screen
canvas = Canvas(window, width = 400, height = 400, bg = 'white')
canvas.pack()

# set up welcome screen with title and directions
title = canvas.create_text(200, 200, text ='The Laundry Collector', fill ='black', font = ('Helvetica', 20))
directions = canvas.create_text(200, 300, text = 'Collect the dirty laundry and avoid the clean laundry.', fill = 'black', font = ('Helvetica', 10))

# set up score display using label widget
score = 0
score_display = Label(window, text= "Score: " + str(score))
score_display.pack()

# set up level display using label widget
level = 1
level_display = Label(window, text="Level: " + str(level))
level_display.pack()

# create an image object using the gif file
basket_image = PhotoImage(file="Untitled design (1).gif")
# use the image to create a character at position 200, 200
mybasket = canvas.create_image(200, 360, image = basket_image)

# variables and lists needed for managing laundry
laundry_list = []  # list containing all laundry created, empty at start
dirty_laundry = []  # list containing all dirty laundry created, empty at start
laundry_speed = 2  # initial speed of falling laundry
laundry_type_list = ['shirt', 'dirty_shirt', 'jacket', 'dirty_jacket', 'sock', 'dirty_sock', 'dirty_pants', 'pants', 'dirty_sock1']

# Import the random module
import random

def random_laundry_generator():
    random_file = random.randint(1, 8)
    if random_file == 1 :
        laundry = canvas.create_image(image="dirty_pants.gif")  # Corrected file path
    elif random_file == 2 :
        laundry = canvas.create_image(image="dirty_shirt.gif")  # Corrected file path
    elif random_file == 3 :
        laundry = canvas.create_image(image="dirty_socks.gif")  # Corrected file path
    elif random_file == 4 :
        laundry = canvas.create_image(image="dirty_jacket.gif")  # Corrected file path
    elif random_file == 5 :
        laundry = canvas.create_image(image="dirty_sock1.gif")  # Corrected file path
    elif random_file == 6 :
        laundry = canvas.create_image(image="jacket.gif")  # Corrected file path
    elif random_file == 7 :
        laundry = canvas.create_image(image="pants.gif")  # Corrected file path
    elif random_file == 8 :
        laundry = canvas.create_image(image="shirt.gif")  # Corrected file path
    return laundry

# function to make laundry at random places
def make_laundry():
    xposition = random.randint(1, 400)
    laundry_type = random.choice(laundry_type_list)
    laundry = canvas.create_image(xposition, 0, xposition+30, 30, image=random_laundry_generator())
    laundry_list.append(laundry)
    if "dirty" in laundry_type:
        dirty_laundry.append(laundry)  # Append to dirty laundry list if dirty
    window.after(1000, make_laundry)  # Schedule the next laundry creation

def move_laundry():
    for laundry in laundry_list:
        coords = canvas.coords(laundry)
        new_coords = (coords[0], coords[1] + laundry_speed)
        canvas.coords(laundry, *new_coords)  # Update the laundry position
        if coords[1] > 400:
            xposition = random.randint(1,400)
            canvas.coords(laundry, xposition, 0, xposition+30, 30)  # Reset laundry position

    window.after(50, move_laundry)  # Schedule the next laundry movement

# Start the game loop
window.after(1000, make_laundry())
window.mainloop()