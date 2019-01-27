"""
SIMPLE KEYBOARD AND MOUSE-CLICK EVENTLOGGER
By Adam Stebbing
1/26/2019
"""
import tkinter as tkr

log = [] # Instantiate event log
master = tkr.Tk() # Instantiate GUI

"""Functions"""
# Add Keyboard events to log
def char(event):
    print("Pressed", repr(event.char))
    key = event.char
    log.append(key)
    print(log)

# Add Click events to log
def click(event):
    frame.focus_set() # Ensure frame is focused on click
    print("Clicked at", event.x, event.y)
    button = event.x, event.y
    log.append(button)
    print(log)

"""Frame"""
frame = tkr.Frame(master, height=500, width=500) # Create GUI
frame.bind("<Key>", char)
frame.bind("<Button-1>", click)
frame.bind("<Button-2>", click)
frame.bind("<Button-3>", click)
frame.pack()

"""Activate"""
master.mainloop()
