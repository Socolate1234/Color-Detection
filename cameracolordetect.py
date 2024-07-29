import cv2
import pandas as pd


camera = cv2.VideoCapture(0)
blue = green = red = 0

def draw_marker(image, x, y):
    cv2.circle(image, (x, y), 5, (255, 238, 156), -1)

# Load color data from CSV
column_names = ["color", "color_name", "hex", "R", "G", "B"]
color_data = pd.read_csv("colors.csv", names=column_names, header=None)

def extract_color(x, y):
    global blue, green, red
    blue, green, red = frame[y, x]
    blue, green, red = int(blue), int(green), int(red)
    return blue, green, red
S
def find_color_name(blue, green, red):
    color_diffs = color_data.apply(lambda row: abs(red - row["R"]) + abs(green - row["G"]) + abs(blue - row["B"]),axis=1)
    closest_color_idx = color_diffs.idxmin()
    return color_data.loc[closest_color_idx, "color_name"]


def annotate_image(image, x, y):
    cv2.rectangle(image, (x - 150, y - 220), (x + 300, y - 170), (blue, green, red), -1)
    color_name = find_color_name(blue, green, red)
    text = f"{color_name} | R={red} G={green} B={blue}"
    text_color = (255, 255, 255) if blue + green + red < 600 else (0, 0, 0)
    cv2.putText(image, text, (x - 140, y - 190), cv2.FONT_HERSHEY_SIMPLEX, 0.6, text_color, 1)

while True:
    ret, frame = camera.read()
    if not ret:
        break
    frame = cv2.flip(frame, 1)
    center_x, center_y = int(frame.shape[1] / 2), int(frame.shape[0] / 2)

    extract_color(center_x, center_y)
    find_color_name(blue, green, red)
    draw_marker(frame, center_x, center_y)
    annotate_image(frame, center_x, center_y)

    cv2.imshow('Camera Color Detector', frame)
    if cv2.waitKey(20) & 0xFF == 27:  # Press 'ESC' to exit
        break

camera.release()
cv2.destroyAllWindows()
