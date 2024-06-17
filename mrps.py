import tkinter as tk
from tkinter import messagebox
import random

# Function to determine the winner
def determine_winner(user_choice):
    choices = ['Rock', 'Paper', 'Scissors']
    computer_choice = random.choice(choices)
    result = ""

    if user_choice == computer_choice:
        result = "It's a tie!"
    elif (user_choice == 'Rock' and computer_choice == 'Scissors') or \
         (user_choice == 'Paper' and computer_choice == 'Rock') or \
         (user_choice == 'Scissors' and computer_choice == 'Paper'):
        result = "You win!"
    else:
        result = "You lose!"

    result_label.config(text=f"Computer chose: {computer_choice}\n{result}")
    update_images(user_choice, computer_choice)

# Function to handle button clicks
def on_button_click(choice):
    determine_winner(choice)

# Function to update images based on choices
def update_images(user_choice, computer_choice):
    user_img_label.config(image=images[user_choice])
    computer_img_label.config(image=images[computer_choice])

# Create the main window
root = tk.Tk()
root.title("Rock Paper Scissors")
root.geometry("600x500")
root.config(bg="lightblue")

# Load images
rock_img = tk.PhotoImage(file="rock png.png")
paper_img = tk.PhotoImage(file="paper png.png")
scissors_img = tk.PhotoImage(file="scissor png.png")
images = {'Rock': rock_img, 'Paper': paper_img, 'Scissors': scissors_img}

# Title label
title_label = tk.Label(root, text="Rock Paper Scissors", font=("Arial", 24, 'bold'), bg="lightblue")
title_label.pack(pady=20)

# Result label
result_label = tk.Label(root, text="", font=("Arial", 18), bg="lightblue")
result_label.pack(pady=20)

# Frame for images
image_frame = tk.Frame(root, bg="lightblue")
image_frame.pack(pady=20)

user_img_label = tk.Label(image_frame, bg="lightblue")
user_img_label.grid(row=0, column=0, padx=20)

computer_img_label = tk.Label(image_frame, bg="lightblue")
computer_img_label.grid(row=0, column=1, padx=20)

# Buttons for Rock, Paper, Scissors
button_frame = tk.Frame(root, bg="lightblue")
button_frame.pack(pady=20)

rock_button = tk.Button(button_frame, text="Rock", font=("Arial", 16), width=10, command=lambda: on_button_click("Rock"))
rock_button.grid(row=0, column=0, padx=10)

paper_button = tk.Button(button_frame, text="Paper", font=("Arial", 16), width=10, command=lambda: on_button_click("Paper"))
paper_button.grid(row=0, column=1, padx=10)

scissors_button = tk.Button(button_frame, text="Scissors", font=("Arial", 16), width=10, command=lambda: on_button_click("Scissors"))
scissors_button.grid(row=0, column=2, padx=10)

# Run the main loop
root.mainloop()
