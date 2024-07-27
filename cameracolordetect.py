import cv2
import pandas as pd

cap = cv2.VideoCapture(0)
b = g = r = 0
def drawCircle(img, x, y):
    cv2.circle(img, (x, y), 5, (255, 238, 156), -1)

index = ["color", "color_name", "hex", "R", "G", "B"]
csv = pd.read_csv("colors.csv", names=index, header=None)
csv.head()
def getBGR(x, y):
    global b, g, r
    b, g, r = img[y, x]
    b, g, r = int(b), int(g), int(r)
    return b, g, r

def checkColor(b, g, r):
    minimum = 1000
    for i in range(len(csv)):
        d = abs(b - int(csv.loc[i, "B"])) + abs(g - int(csv.loc[i, "G"])) + abs(r - int(csv.loc[i, "R"])) # maximum = 255 + 255 + 255 = 765 (d = ||b-B|| + ||g-G|| + ||r-R||)
        if (d <= minimum):
            minimum = d
            colorname = csv.loc[i, "color_name"]
    return colorname
def putText(img, x, y):
    cv2.rectangle(img, (x - 150, y - 220), (x + 300, y - 170), (b,g,r), -1)
    text = checkColor(b, g, r) + " | R=" + str(r) + " G=" + str(g) + " B=" + str(b)
    cv2.putText(img, text, (x - 140, y - 190), cv2.FONT_HERSHEY_COMPLEX, 0.6, (255, 255, 255), 1)
    if r + g + b >= 600:
        cv2.putText(img, text, (x - 140, y - 190), cv2.FONT_HERSHEY_COMPLEX, 0.6, (0,0,0), 1)

while True:
    ret, img = cap.read()
    img = cv2.flip(img, 1)
    x, y = int(img.shape[1]/2), int(img.shape[0]/2)
    # print(x, y)
    getBGR(x, y)
    checkColor(b, g, r)
    drawCircle(img, x, y)
    putText(img, x, y)
    cv2.imshow('Camera Color Detector', img)
    if cv2.waitKey(20) & 0xFF == 27:
        break
