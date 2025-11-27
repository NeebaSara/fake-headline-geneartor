import random
import tkinter as tk
from tkinter import messagebox, ttk

subjects = ["Jimin", "Mark", "Matthew", "Johnny", "Philip"]
actions = ["laughs", "declares", "walks", "runs", "complaints", "went"]
places_or_things = ["at the joke", "a holiday on Monday", "near water", "away from others", "and goes on a trip"]

def main():
    root = tk.Tk()
    root.title("Fake News Headline Generator")
    root.geometry("600x180")
    root.resizable(False, False)

    headline_var = tk.StringVar()

    def generate_headline():
        subject = random.choice(subjects)
        action = random.choice(actions)
        place = random.choice(places_or_things)
        headline_var.set(f"BREAKING NEWS: {subject} {action} {place}")

    def on_quit():
        if messagebox.askyesno("Quit", "Do you really want to quit?"):
            root.destroy()

    headline_label = ttk.Label(root, textvariable=headline_var, wraplength=560, font=("Copperplate Gothic Bold", 14)) #the font and the sizes
    headline_label.pack(pady=(18,10), padx=20)

    btn_frame = ttk.Frame(root)
    btn_frame.pack()

    ttk.Button(btn_frame, text="New Headline", command=generate_headline).grid(row=0, column=0, padx=10)
    ttk.Button(btn_frame, text="Quit", command=on_quit).grid(row=0, column=1, padx=10)

    root.protocol("WM_DELETE_WINDOW", on_quit)  # ask confirmation on window close
    generate_headline()  # show one on start
    root.mainloop()

if __name__ == "__main__":
    main()

#FIN~~~~~