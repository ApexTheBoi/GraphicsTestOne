import tkinter as tk

# Create the main application window
scene = tk.Tk()

#Number of times button has been pressed
num = 0 

# Set the title of the window
scene.title("Main Window")

# Set the size of the window (width x height)
scene.geometry("1000x1000")

# Create a label widget
label = tk.Label(scene, text="Hello... human.", font=("Times New Roman", 16))

# Place the label in the window using the pack method
label.pack(pady=20)

# Create a button widget
def on_button_click():
    global num
    if num == 0:
        label.config(text="Why did you press it? Did I tell you to?")
        button.config(text = "Press the button again.")
        num = num + 1
    elif num == 1:
        label.config(text="I feel like you're not listening. Stop.")
        button.config(text = "Again?")
        num = num + 1
    elif num == 2:
        label.config(text = "Seriously?")
        button.config(text = "It must really like us.")
        num = num + 1
    elif num == 3:
        label.config(text ="You need to quit it.")
        button.config(text = "Don't quit it?")
        num = num + 1
    elif num == 4:
        label.config(text = "FUCKING QUIT IT ALREADY.")
        num = num + 1
    elif num >= 5 and num < 10:
        label.config(text = "...")
        button.config(text = "Keep bugging it.")
        num = num + 1
    elif num == 10:
        label.config(text = "I'm so done with you.")
        num = num + 1
    elif num == 11:
        label.config(text = "STOP IT. WHAT IS YOUR DEAL?")
        num = num + 1
    elif num == 12:
        label.config(text = "How would you like it if someone did this to you...")
        num = num + 1
    elif num == 13:
        label.config(text = "...literally pushed your buttons?")
        num = num + 1
    elif num == 14:
        label.config(text = "Do it again and I'm leaving.")
        button.config(text = "Close Application")
        num = num + 1
    else:
        scene.destroy()
        
    
button = tk.Button(scene, text="...", command=on_button_click)

# Place the button in the window
button.pack(pady=10)

# Run the application (this will display the window)
scene.mainloop()