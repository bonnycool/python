import breezypythongui as bpg
from breezypythongui import EasyFrame  # Correct import
import random

class GuessingGame(EasyFrame):
    def __init__(self):
        # Initialize the frame
        super().__init__(title="Number Guessing Game", width=300, height=150)

        # Generate a random number between 1 and 100
        self.target_number = random.randint(1, 100)

        # User input field
        self.addLabel("Enter your guess:", row=0, column=0)
        self.guessField = self.addIntegerField(0, row=0, column=1)

        # Guess button
        self.addButton("Guess", self.guess_number, row=1, column=0, columnspan=2)

        # Output label to display feedback
        self.outputLabel = self.addLabel("", row=2, column=0, columnspan=2)

    def guess_number(self):
        # Get the user's guess
        guess = self.guessField.getNumber()

        # Check the guess and provide feedback
        if guess < self.target_number:
            self.outputLabel["text"] = "Too low! Try again."
        elif guess > self.target_number:
            self.outputLabel["text"] = "Too high! Try again."
        else:
            self.outputLabel["text"] = "Correct! You guessed it!"

# Create and start the UI
if __name__ == "__main__":
    app = GuessingGame()
    app.mainloop()  # Start the event loop
