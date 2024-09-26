import tkinter as tk
import random

class Rpsgame:
    def _init_(self, master):
        self.master = master
        master.title("Rock Paper Scissors Game")

        self.user_score = 0
        self.computer_score = 0

        self.result_var = tk.StringVar()
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.master, text="Choose Rock, Paper or Scissors:", font=('Arial', 16)).pack(pady=10)

        choices = ["Rock", "Paper", "Scissors"]
        for choice in choices:
            button = tk.Button(self.master, text=choice, font=('Arial', 14), bg="#4CAF50", fg="white",
                               command=lambda c=choice: self.play_game(c))
            button.pack(pady=5, padx=20, fill=tk.X)

        # Score display
        self.score_label = tk.Label(self.master, text="Score: You 0 - Computer 0", font=('Arial', 16))
        self.score_label.pack(pady=20)

        # Label to display result
        self.result_label = tk.Label(self.master, textvariable=self.result_var, font=('Arial', 16))
        self.result_label.pack(pady=20)

    def play_game(self, user_choice):
        self.user_choice = user_choice
        self.computer_choice = random.choice(["Rock", "Paper", "Scissors"])
        self.determine_winner()

    def determine_winner(self):
        if self.user_choice == self.computer_choice:
            result = "It's a tie!"
        elif (self.user_choice == "Rock" and self.computer_choice == "Scissors") or \
             (self.user_choice == "Paper" and self.computer_choice == "Rock") or \
             (self.user_choice == "Scissors" and self.computer_choice == "Paper"):
            result = "You win!"
            self.user_score += 1
        else:
            result = "You lose!"
            self.computer_score += 1

        self.result_var.set(f"You chose: {self.user_choice}\nComputer chose: {self.computer_choice}\n{result}")
        self.score_label.config(text=f"Score: You {self.user_score} - Computer {self.computer_score}")

if _name_ == "_main_":
    root = tk.Tk()
    root.configure(bg="#f0f0f0")
    game = Rpsgame(root)
    root.mainloop()