import tkinter as tk
import subprocess

root = tk.Tk()
root.geometry('400x300')
root.resizable(width=False, height=False)
root.title('Color Detecting')

color1 = 'WHITE'
color2 = '#5385e4'
color3 = '#65e7ff'
color4 = 'BLACK'

main_frame = tk.Frame(root, bg=color1, pady=40)
main_frame.pack(fill=tk.BOTH, expand=True)
main_frame.columnconfigure(0, weight=1)
main_frame.rowconfigure(0, weight=1)
main_frame.rowconfigure(1, weight=1)

button1 = tk.Button(
    main_frame,
    background=color2,
    foreground=color4,
    highlightcolor='WHITE',
    width=20,
    height=2,
    border=0,
    cursor='hand1',
    text='Camera Color Detection',
    font=('Arial', 16, 'bold')
)
button1.grid(column=0, row=0)


button2 = tk.Button(
    main_frame,
    background=color2,
    foreground=color4,
    highlightcolor='WHITE',
    width=20,
    height=2,
    border=0,
    cursor='hand1',
    text='Picture Color Detection',
    font=('Arial', 16, 'bold')
)
button2.grid(column=0, row=1)
def bt1_enter(event):
    button1.config(
        highlightbackground=color3
    )
def bt1_leave(event):
    button1.config(
        highlightbackground=color3
    )
def bt2_enter(event):
    button2.config(
        highlightbackground=color3
    )
def bt2_leave(event):
    button2.config(
        highlightbackground=color3
    )

def run_camera():
    subprocess.run(["python", "cameracolordetect.py"])

def run_picture():
    subprocess.run(["python", "picturecolordetect.py"])

button1.config(command=run_camera)
button2.config(command=run_picture)

button1.bind('<Enter>',bt1_enter)
button1.bind('<Leave>',bt1_leave)

button2.bind('<Enter>',bt2_enter)
button2.bind('<Leave>',bt2_leave)

root.mainloop()
