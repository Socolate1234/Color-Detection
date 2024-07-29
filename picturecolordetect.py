
import cv2
import pandas as pd
import tkinter as tk
from tkinter import filedialog

def select_image():
    file_path = filedialog.askopenfilename(
        initialdir="This PC",
        title="Choose an image",
        filetypes=(
            ("Image files", "*.png *.gif *.jpg *.jpeg *.pgm *.ppm *.xbm"),
            ("All files", "*.*")
        )
    )
    return file_path

selected_image = select_image()
image = cv2.imread(selected_image)

mouse_clicked = False
red = green = blue = x_coord = y_coord = 0

color_columns = ["color", "color_name", "hex", "R", "G", "B"]
color_data = pd.read_csv('colors.csv', names=color_columns, header=None)

def identify_color(red, green, blue):
    color_diffs = color_data.apply(lambda row: abs(red - row["R"]) + abs(green - row["G"]) + abs(blue - row["B"]),axis=1)
    closest_color_idx = color_diffs.idxmin()
    return color_data.loc[closest_color_idx, "color_name"]

def handle_mouse_event(event, x, y, flags, param):
    global blue, green, red, x_coord, y_coord, mouse_clicked
    if event == cv2.EVENT_LBUTTONDBLCLK:
        mouse_clicked = True
        x_coord, y_coord = x, y
        blue, green, red = map(int, image[y, x])

cv2.namedWindow('image')
cv2.setMouseCallback('image', handle_mouse_event)

while True:
    cv2.imshow("image", image)
    if mouse_clicked:
        cv2.rectangle(image, (20, 20), (750, 60), (blue, green, red), -1)
        color_text = identify_color(red, green, blue) + ' R=' + str(red) + ' G=' + str(green) + ' B=' + str(blue)
        text_color = (0, 0, 0) if red + green + blue >= 600 else (255, 255, 255)
        cv2.putText(image, color_text, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.8, text_color, 1)
        mouse_clicked = False
    if cv2.waitKey(20) & 0xFF == 27:
        break

cv2.destroyAllWindows()
