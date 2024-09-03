# The Laundry Collector Game program

from tkinter import *
import random

# make window
window = Tk()
window.title('The Laundry Collector Game')

# create a canvas to put objects on the screen
canvas = Canvas(window, width=400, height=400, bg='white')
canvas.pack()

# set up welcome screen with title and directions
title = canvas.create_text(200, 200, text='The Laundry Collector', fill='black', font=('Helvetica', 20))
directions = canvas.create_text(200, 300, text='Collect the dirty laundry and avoid the clean laundry.', fill='black', font=('Helvetica', 10))

# # set up score display using label widget
# score = 0
# score_display = Label(window, text="Score: " + str(score))
# score_display.pack()

# # set up level display using label widget
# level = 1
# level_display = Label(window, text="Level: " + str(level))
# level_display.pack()

# # create an image object using the gif file
# basket_image = PhotoImage(file="Untitled design (1).gif")
# # use the image to create a character at position 200, 200
# mybasket = canvas.create_image(200, 360, image=basket_image)

# # variables and lists needed for managing laundry
# laundry_list = []  # list containing all laundry created, empty at start
# dirty_laundry = []  # list containing all dirty laundry created, empty at start
# laundry_speed = 2  # initial speed of falling laundry
# laundry_type_list = ['shirt', 'dirty_shirt', 'jacket', 'dirty_jacket', 'sock', 'dirty_sock', 'dirty_pants', 'pants', 'dirty_sock1']

# def random_laundry_generator():
#     random_file = random.randint(1, 8)
#     if random_file == 1:
#         return "dirty_pants.gif"
#     elif random_file == 2:
#         return "dirty_shirt.gif"
#     elif random_file == 3:
#         return "dirty_socks.gif"
#     elif random_file == 4:
#         return "dirty_jacket.gif"
#     elif random_file == 5:
#         return "dirty_sock1.gif"
#     elif random_file == 6:
#         return "jacket.gif"
#     elif random_file == 7:
#         return "pants.gif"
#     elif random_file == 8:
#         return "shirt.gif"

# def make_laundry():
#     xposition = random.randint(1, 400)
#     laundry_image = PhotoImage(file=random_laundry_generator())
#     laundry = canvas.create_image(xposition, 0, image=laundry_image)
#     laundry_list.append(laundry)
#     window.after(1000, make_laundry)

# make_laundry()

window.mainloop()