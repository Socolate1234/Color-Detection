

import cv2
import pandas as pd

import tkinter as tk
from tkinter import filedialog
def open_image():

    filepath = filedialog.askopenfilename(
        initialdir="This PC",
        title="Select an image",
        filetypes=(
            ("Image files", "*.png *.gif *.jpg *.jpeg *.pgm *.ppm *.xbm"),
            ("All files", "*.*")
        )
    )
    return filepath

photo = open_image()
img = cv2.imread(photo)

# declaring global variables (are used later on)
clicked = False
r = g = b = x_pos = y_pos = 0

# Reading csv file with pandas and giving names to each column
index = ["color", "color_name", "hex", "R", "G", "B"]
csv = pd.read_csv('colors.csv', names=index, header=None)
csv.head()
def checkColor(R, G, B):
    minimum = 10000
    for i in range(len(csv)):
        d = abs(R - int(csv.loc[i, "R"])) + abs(G - int(csv.loc[i, "G"])) + abs(B - int(csv.loc[i, "B"]))
        if d <= minimum:
            minimum = d
            cname = csv.loc[i, "color_name"]
    return cname

# function to get x,y coordinates of mouse double click
def draw_function(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        global b, g, r, x_pos, y_pos, clicked
        clicked = True
        x_pos = x
        y_pos = y
        b, g, r = img[y, x]
        b = int(b)
        g = int(g)
        r = int(r)
cv2.namedWindow('image')
cv2.setMouseCallback('image', draw_function)

while True:

    cv2.imshow("image", img)
    if clicked:
        cv2.rectangle(img, (20, 20), (750, 60), (b, g, r), -1)
        text = checkColor(r, g, b) + ' R=' + str(r) + ' G=' + str(g) + ' B=' + str(b)
        cv2.putText(img, text, (50, 50), 2, 0.8, (255, 255, 255), 1, cv2.FONT_HERSHEY_COMPLEX)
        if r + g + b >= 600:
            cv2.putText(img, text, (50, 50), 2, 0.8, (0, 0, 0), 1, cv2.FONT_HERSHEY_COMPLEX)
        clicked = False
# Press Esc key to exist
    if cv2.waitKey(20) & 0xFF == 27:
        break

cv2.destroyAllWindows()
