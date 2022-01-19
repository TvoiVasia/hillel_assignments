import tkinter as tk
import random
import time

window = tk.Tk()
window.title("Timer Calculator")
window.geometry("400x300+500+200")


label = tk.Label(
    text='''In this activity, you can measure just how long
it takes for you to react, and compare reaction times.

Please, press the button, when it is red!''',
    foreground="#3F3F3F",  # Set the text color to white
    background="#E0E0E0",  # Set the background color to black
    font=("Arial Black", 9),
    width=50,
    height=5,
)

colors = ["#FF0000", "#00FA9A", "#191970",
          "#FF69B4", "#FF8C00", "#6B8E23",
          "#FF00FF", "#4B0082", "#DEB887"]


frame = tk.Frame(
    height=20
)


start = 0

def timer_update():
    global start
    value = random.randint(0, len(colors)-1)
    button.config(
        bg=colors[value]
    )
    if button["bg"] == "#FF0000":
        start = time.time()
    elif button["bg"] != "#FF0000":
        pass
    window.after(300, timer_update)


false_click = 0

def clicks():
    global false_click
    if button["bg"] == "#FF0000":
        your_time = time.time() - start
        result.config(
            text=f"Your time: {your_time}",
         )
    else:
        false_click += 1
        incorrect.config(
            text=f"Incorrect click: {false_click}",
        )


button = tk.Button(
    text="Click me!",
    bg="blue",
    fg="white",
    width=20,
    height=3,
    command=clicks,
)


result = tk.Label(
    text="Your time: 0.0",
    foreground="red",  # Set the text color to white
    font=("Arial Black", 12),
)


frame_2 = tk.Frame(
    height=5
)


incorrect = tk.Label(
    text="Incorrect click: 0",
    foreground="red",  # Set the text color to white
    font=("Arial", 12),
)


for c in window.children:
    print(c)
    window.children[c].pack()

window.update()

window.after(300, timer_update)

window.mainloop()

