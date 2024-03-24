import cv2
import tkinter as tk
from game import gameStart
from training import trainStart

root = tk.Tk()

def play_game():
    print("Starting game...")
    root.destroy()
    gameStart()

def start_training():
    print("Starting training...")
    root.destroy()
    trainStart()

def quit_game():
    root.destroy()

def initMenu():
    root.title("Signquest")
    root.geometry("400x400")
    title_label = tk.Label(root, text="Signquest", font=("Arial", 28, "bold"), fg="#333", pady=20)
    title_label.pack()
    button_style = {"font": ("Arial", 16), "fg": "black", "padx": 20, "pady": 10, "bd": 0}
    play_button = tk.Button(root, text="Play Game", command=play_game, **button_style)
    play_button.pack()
    training_button = tk.Button(root, text="Training", command=start_training, **button_style)
    training_button.pack()
    quit_button = tk.Button(root, text="Quit", command=quit_game, bg="#f44336", **button_style)
    quit_button.pack(pady=20)
    root.mainloop()

def main():
     initMenu()

if __name__ == "__main__":
         main()