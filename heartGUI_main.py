import tkinter as tk
from tkinter import ttk  # Importing ttk for themed widgets
from PIL import Image, ImageTk

def button_pressed(event):
    event.widget.config(relief="sunken")

def button_released(event):
    event.widget.config(relief="raised")

def call_file():
    # Define the function for the "Disease Detection" button
    pass  # Placeholder for the function call

root = tk.Tk()
root.configure(background="white")  # Changing background color
w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))
root.title("Cardiovascular Disease Prediction")

# Adding image "log.jpg" on the right side
image3 = Image.open('log.jpg')
image3 = image3.resize((int(w/2), h), Image.LANCZOS)

background_image2 = ImageTk.PhotoImage(image3)
background_label2 = tk.Label(root, image=background_image2, bg="white")  # Set the same background color as the root window
background_label2.image = background_image2
background_label2.place(x=int(w/2), y=0)

# Adding text "Cardiovascular Disease Prediction" above the buttons on the left side
label_header = tk.Label(root, text="CARDIOVASCULAR DISEASE TRIAGE", font=("Helvetica", 30, 'bold'),
                        background="white", fg="black", width=40, height=1)  # Changing text color to black
label_header.place(x=150, y=20)

# Additional text
additional_text = """
Cardiovascular disease (CVD) triage refers to the process of evaluating and prioritizing patients who present with symptoms or risk factors related to cardiovascular diseases. 

Triage is a common practice in healthcare, particularly in emergency situations, where patients are assessed to determine the urgency of their condition and to ensure that those with the most critical needs receive immediate attention.
"""

label_additional_text = tk.Label(root, text=additional_text, font=("Helvetica", 14, "italic"),
                                 background="white", fg="black", wraplength=500, justify='center')
label_additional_text.place(x=50, y=150)

def reg():
    from subprocess import call
    call(["python", "heart_registration.py"])

def log():
    from subprocess import call
    call(["python", "heart_login.py"])

def window():
    root.destroy()

button1 = tk.Button(root, text="Login", command=log, width=14, height=1, font=('Helvetica', 20, ' bold '), bg="green", fg="white")
button1.place(x=20, y=500)
button1.bind("<ButtonPress>", button_pressed)
button1.bind("<ButtonRelease>", button_released)

button2 = tk.Button(root, text="Register", command=reg, width=14, height=1, font=('Helvetica', 20, ' bold '), bg="green", fg="white")
button2.place(x=300, y=500)
button2.bind("<ButtonPress>", button_pressed)
button2.bind("<ButtonRelease>", button_released)

button3 = tk.Button(root, text="Exit", command=window, width=14, height=1, font=('Helvetica', 20, ' bold '), bg="red", fg="white")
button3.place(x=150, y=580)
button3.bind("<ButtonPress>", button_pressed)
button3.bind("<ButtonRelease>", button_released)

# Disease Detection button with glass texture effect
style = ttk.Style()
style.theme_use("clam")  # Use the 'clam' theme
style.configure("Glass.TButton", background="#a0a0a0", bordercolor="#a0a0a0", lightcolor="#a0a0a0", darkcolor="#a0a0a0", relief="flat", font=("Helvetica", 18,'bold'))

root.mainloop()