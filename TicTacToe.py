import tkinter as tk
import tkinter.messagebox as messagebox
import json
import os


class TicTacToe:
    def __init__(self, agent="ValueIteration"):
        self.window = tk.Tk()
        self.window.title("Tic Tac Toe")
        self.current_player = "X"  # default human player if going first
        self.computer_symbol = "O"  # default computer player if going first
        self.board = (0,) * 9
        self.buttons = [None] * 9
        self.is_vs_computer = False  # flag to check if playing against the computer
        self.agent = agent
        self.policy = {}
        if self.agent == "ValueIteration":
            path = str(os.getcwd())+"/"+"OptimalPolicy/valueIteration.json"
        elif self.agent == "PolicyIteration":
            path = str(os.getcwd())+"/"+"OptimalPolicy/policyIteration.json"

        with open(path, 'r') as json_file:
            self.policy = json.load(json_file)  # open json file as dictionary

        # Calculate the window position to center it on the screen
        screen_width = self.window.winfo_width()
        screen_height = self.window.winfo_height()
        window_width = 380  # adjustable
        window_height = 420  # adjustable
        x_axis = (screen_width - window_width) // 2
        y_axis = (screen_height - window_height) // 2
        self.window.geometry(f"{window_width}x{window_height}+{x_axis}{y_axis}")

        player_choice = tk.StringVar()
        player_choice.set("X")
        player_label = tk.Label(self.window, text="Choose your symbol:")
        player_label.grid(row=3, columnspan=3)
        x_radio = tk.Radiobutton(self.window, text="X", variable=player_choice, value="X")
        o_radio = tk.Radiobutton(self.window, text="O", variable=player_choice, value="O")
        x_radio.grid(row=4, column=0)
        o_radio.grid(row=4, column=2)

        # Checkbox for playing against the computer
        vs_computer_checkbox = tk.Checkbutton(self.window, text="Play vs Computer",
                                              command=self.toggle_vs_computer)
        vs_computer_checkbox.grid(row=5, columnspan=3)

        start_button = tk.Button(self.window, text="Start Game",
                                 command=lambda: self.start_game(player_choice.get()))
        start_button.grid(row=6, columnspan=3)

    def toggle_vs_computer(self):
        self.is_vs_computer = not self.is_vs_computer

    def start_game(self, player_choice):
        self.computer_symbol = "O" \
            if player_choice == "X" else "X"  # set computer symbol opposite to player
        for i in range(9):
            row, column = i // 3, i % 3
            button = tk.Button(self.window, text="", width=10, height=5,
                               command=lambda idx=i: self.make_move(idx))
            button.grid(row=row, column=column)
            self.buttons[i] = button

        if self.computer_symbol == "X" and self.is_vs_computer:
            # computer starts the game if playing against the computer and computer is X
            self.make_computer_move()

    def make_move(self, idx):
        if self.board[idx] == 0:
            self.board = self.board[:idx] + (1 if self.current_player == "X" else 2,) + self.board[idx + 1:]
            self.buttons[idx]['text'] = self.current_player
            if self.check_win() or self.check_tie():
                self.end_game()
            else:
                self.current_player = "O" if self.current_player == "X" else "X"
                if self.is_vs_computer and self.current_player == self.computer_symbol:
                    # computer's turn when playing against the computer
                    self.make_computer_move()

    def make_computer_move(self):
        state = self.board  # get current state of the board
        if self.computer_symbol == "O":  # invert X and O if computer is O
            state = tuple(3-x if x != 0 else 0 for x in state)
        self.make_move(self.policy[str(state)])

    def check_win(self):  # all possible win combinations
        win_combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7),
                            (2, 5, 8), (0, 4, 8), (2, 4, 6)]
        for combo in win_combinations:
            a, b, c = combo
            if self.board[a] == self.board[b] == self.board[c] and self.board[a] != 0:
                messagebox.showinfo("Game Over", f"Player {self.current_player} wins!")
                return True
        return False

    def check_tie(self):
        if 0 not in self.board:
            messagebox.showinfo("Game Over", "It's a tie!")
            return True
        return False

    def end_game(self):
        for button in self.buttons:
            button.config(state=tk.DISABLED)

        restart_button = tk.Button(self.window, text="Restart Game", command=self.restart_game)
        restart_button.grid(row=7, columnspan=3)

    def restart_game(self):
        self.window.destroy()
        self.__init__()
        self.start_game("X")

    def start(self):
        self.window.mainloop()


if __name__ == "__main__":
    game = TicTacToe("PolicyIteration")
    game.start()
