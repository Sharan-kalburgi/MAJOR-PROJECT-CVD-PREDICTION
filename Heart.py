import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk, ImageDraw
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from keras.models import Sequential
from keras.layers import Dense, Dropout
import random

# Load dataset
dataset = pd.read_csv('new.csv')

# GUI setup
root = tk.Tk()
root.title("CARDIO VASCULAR DISEASE TRIAGE")

# Set window size
w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))

# Set background color to Prussian Blue
root.configure(bg="#CDE9FC")

instruction_label = tk.Label(root, font=('Helvetica', 14, 'bold'), fg="black", bg="#CDE9FC")
instruction_label.place(x=8, y=250)

# Heading
lbl = tk.Label(root, text="CARDIO VASCULAR DISEASE TRIAGE", font=('Helvetica', 35, 'bold'), bg="#CDE9FC", fg="black")
lbl.place(x=238, y=40)

def display_fun_fact():
    fact = random.choice(fun_facts)
    instruction_label.config(text=fact)

# Function to update fun fact every 30 seconds
def update_fun_fact():
    display_fun_fact()
    root.after(3000, update_fun_fact)  # Schedule the update after 30 seconds

# Fun Facts about Heart Disease
fun_facts = [
    "Did you know that heart disease is the leading cause of death worldwide?",
    "Exercise can significantly reduce the risk of heart disease.",
    "High blood pressure is a major risk factor for heart disease.",
    "Eating a healthy diet can help prevent heart disease.",
    "Stress can contribute to the development of heart disease.",
    "Did you know that heart disease can affect people of all ages?",
    "Regular check-ups and screenings are essential for detecting heart disease early.",
    "Smoking is a leading cause of heart disease.",
    "Lack of sleep can increase the risk of heart disease.",
    "Laughing can improve blood flow and reduce the risk of heart disease.",
    "Heart disease can be genetic, so knowing your family history is important.",
    "Maintaining a healthy weight can lower the risk of heart disease."
]


# Fun Fact Label
fun_fact_label = tk.Label(root, text="DID YOU KNOW..!?", font=('Helvetica', 20,"bold"), wraplength=500,justify="left",bg="#CDE9FC", fg="black")
center_x = (w - 300) // 2
center_y = (h - 300) // 2
fun_fact_label.place(x=8, y=200)

# Start updating fun facts
update_fun_fact()

# Function to display confusion matrix
def display_confusion_matrix(cm, title):
    plt.figure(figsize=(8, 6))
    sns.heatmap(cm, annot=True, cmap='Greens', fmt='g')
    plt.xlabel('Predicted labels')
    plt.ylabel('True labels')
    plt.title(title)
    plt.show()

# Function to display classification report
def display_classification_report(report):
    print("Classification Report:\n", report)

# Function to display accuracy
def display_accuracy(accuracy):
    print("Accuracy: {:.2f}%".format(accuracy * 100))

# ANN Model Training and Evaluation
def ANN_algo():
    # Data preprocessing
    le = LabelEncoder()
    data = dataset.dropna()
    data['target'] = le.fit_transform(data['target'])
    data['thal'] = le.fit_transform(data['thal'])
    data['cp'] = le.fit_transform(data['cp'])
    x = data.drop(['target'], axis=1)
    y = data['target']
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=0)
    sc = StandardScaler()
    X_train = sc.fit_transform(x_train)
    X_test = sc.transform(x_test)

    # Train ANN model
    classifier = Sequential()
    classifier.add(Dense(activation="relu", input_dim=13, units=8, kernel_initializer="uniform"))
    classifier.add(Dense(activation="relu", units=14, kernel_initializer="uniform"))
    classifier.add(Dense(activation="sigmoid", units=1, kernel_initializer="uniform"))
    classifier.add(Dropout(0.2))
    classifier.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    classifier.fit(X_train, y_train, batch_size=8, epochs=100)
    y_pred = classifier.predict(X_test)
    y_pred = (y_pred > 0.5)

    # Evaluate ANN model
    accuracy = accuracy_score(y_test, y_pred)
    classification_report = classification_report(y_test, y_pred)
    confusion_matrix = confusion_matrix(y_test, y_pred)

    # Display results
    display_classification_report(classification_report)
    display_confusion_matrix(confusion_matrix, title='ANN Confusion Matrix')
    display_accuracy(accuracy)

def call_file():
    import Check_Heart
    Check_Heart.Train()

# Function to close the window
def window():
    root.destroy()

# Disease Detection instruction text
# instruction_label = tk.Label(root, text="Press the Detection button to check for abnormalities", font=('Helvetica', 18, 'bold'), bg="#CDE9FC", fg="black")
# instruction_label.place(x=5, y=250)

# Disease Detection button with glass texture effect
style = ttk.Style()
style.theme_use("clam")  # Use the 'clam' theme
style.configure("Glass.TButton", background="#4CAF50", bordercolor="#a0a0a0", font=("Helvetica", 20))
button4 = ttk.Button(root, text="Disease Detection", command=call_file, width=20, style="Glass.TButton")
button4.place(x=20, y=350)

# Exit button with glass texture effect
exit = ttk.Button(root, text="Exit", command=window, width=20, style="Glass.TButton")
exit.place(x=20, y=450)

# Load and display image on the right-hand side
image = Image.open("31.jpg")
image.thumbnail((400, 400))  # Increase the size of the image

# Create a circular mask
mask = Image.new("L", image.size, 0)
draw = ImageDraw.Draw(mask)
draw.ellipse((0, 0) + image.size, fill=255)

# Apply the circular mask to the original image
circular_image = Image.new("RGBA", image.size, (0, 0, 0, 0))
circular_image.paste(image, (0, 0), mask)

# Convert the circular image to a Tkinter-compatible format
photo = ImageTk.PhotoImage(circular_image)

# Create a canvas and display the circular image
canvas = tk.Canvas(root, width=400, height=400, bg="#CDE9FC", bd=0, highlightthickness=0)
canvas.create_image(200, 200, image=photo)
canvas.place(x=w - 450, y=h // 2 - 200)

root.mainloop()