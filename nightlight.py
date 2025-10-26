import subprocess
from tkinter import *


# Functions 
def set_temp():
    # Set color temperature to set amount of kelvin

    value = str(slider.get())

    subprocess.run(["redshift", "-x"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)  
    subprocess.run(["redshift", "-O", value], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

def reset():
    # Set color temperature to the normal amount
    subprocess.run(["redshift", "-x"], stdout=subprocess.DEVNULL)   

# Making The Window
window = Tk()
window.title("Night Light")
window.geometry("300x250")
window.configure(bg='white')


Label(window, text="Color temperature (K)", bg="white").pack(pady=10)


slider = Scale(window, from_=4000, to=1000, orient=HORIZONTAL, length=250)
slider.set(4000)
slider.pack(pady=10)


# Making and Packing The buttons
btn_on = Button(window, text="Turn on", command=set_temp, bg='green', width=15) 
btn_off = Button(window, text="Turn off", command=reset, bg='red', width=15) 

btn_on.pack(pady=10)
btn_off.pack(pady=10)

# Looping the window

window.mainloop()