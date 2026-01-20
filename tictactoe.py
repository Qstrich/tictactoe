import tkinter as tk
from tkinter import messagebox

# setup the window
window = tk.Tk()
window.title("Tic-Tac-Toe")
window.geometry("400x470")

# global variables
turn = "X"
game_over = False
board = [""] * 9
buttons = []

def click(index):
    global turn, game_over
    
    if board[index] == "" and not game_over:
        board[index] = turn
        
        # update the button
        if turn == "X":
            buttons[index].config(text="X", fg="blue")
        else:
            buttons[index].config(text="O", fg="red")
            
        check_winner()
        
        if not game_over:
            # swap turns
            if turn == "X":
                turn = "O"
            else:
                turn = "X"
            status_label.config(text=f"Player {turn}'s Turn")

def check_winner():
    global game_over
    
    # rows, cols, diagonals
    wins = [
        (0,1,2), (3,4,5), (6,7,8),
        (0,3,6), (1,4,7), (2,5,8),
        (0,4,8), (2,4,6)
    ]
    
    for a,b,c in wins:
        if board[a] == board[b] == board[c] and board[a] != "":
            # we have a winner
            buttons[a].config(bg="lightgreen")
            buttons[b].config(bg="lightgreen")
            buttons[c].config(bg="lightgreen")
            
            status_label.config(text=f"Player {turn} Wins!")
            messagebox.showinfo("Game Over", f"Player {turn} Wins!")
            game_over = True
            return

    # check for draw
    if "" not in board:
        status_label.config(text="Draw!")
        messagebox.showinfo("Game Over", "It's a Draw!")
        game_over = True

def reset_game():
    global turn, game_over, board
    turn = "X"
    game_over = False
    board = [""] * 9
    status_label.config(text="Player X's Turn")
    
    for btn in buttons:
        btn.config(text="", bg="SystemButtonFace")

# ui setup
status_label = tk.Label(window, text="Player X's Turn", font=("Arial", 14), pady=10)
status_label.pack()

frame = tk.Frame(window)
frame.pack(expand=True)

# make the buttons
for i in range(9):
    btn = tk.Button(frame, text="", font=("Arial", 24, "bold"), width=4, height=2,
                    command=lambda i=i: click(i))
    # simple math for the grid
    r = i // 3
    c = i % 3
    btn.grid(row=r, column=c, padx=5, pady=5)
    buttons.append(btn)

restart_btn = tk.Button(window, text="Play Again", font=("Arial", 12), command=reset_game)
restart_btn.pack(pady=15)

window.mainloop()
