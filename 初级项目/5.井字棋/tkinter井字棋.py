import tkinter as tk

class TicTacToeGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Tic Tac Toe")

        # 创建9个按钮
        self.buttons = []
        for i in range(3):
            row = []
            for j in range(3):
                button = tk.Button(self.root, text="", font=("Helvetica", 24), width=5, height=2, command=lambda row=i, col=j: self.clicked(row, col))
                button.grid(row=i, column=j)
                row.append(button)
            self.buttons.append(row)

        self.current_player = "X"
        self.board = [
            ["-", "-", "-"],
            ["-", "-", "-"],
            ["-", "-", "-"]
        ]

    def clicked(self, row, col):
        """
        当一个按钮被点击时，将其设置为当前玩家的标记，并切换到下一个玩家。
        """
        if self.board[row][col] == "-":
            self.buttons[row][col].config(text=self.current_player)
            self.board[row][col] = self.current_player
            if self.current_player == "X":
                self.current_player = "O"
            else:
                self.current_player = "X"
            self.check_game_over()

    def check_game_over(self):
        """
        检查游戏是否已结束
        """
        for i in range(3):
            # 检查行
            if self.board[i][0] != "-" and self.board[i][0] == self.board[i][1] and self.board[i][1] == self.board[i][2]:
                self.show_winner(self.board[i][0])
                return
            # 检查列
            if self.board[0][i] != "-" and self.board[0][i] == self.board[1][i] and self.board[1][i] == self.board[2][i]:
                self.show_winner(self.board[0][i])
                return
        # 检查对角线
        if self.board[0][0] != "-" and self.board[0][0] == self.board[1][1] and self.board[1][1] == self.board[2][2]:
            self.show_winner(self.board[0][0])
            return
        if self.board[0][2] != "-" and self.board[0][2] == self.board[1][1] and self.board[1][1] == self.board[2][0]:
            self.show_winner(self.board[0][2])
            return
        # 检查是否有空格
        for row in self.board:
            for cell in row:
                if cell == "-":
                    return
        # 如果没有空格，平局
        self.show_winner("Tie")

    def show_winner(self, winner):
        """
        显示获胜者或平局信息，并禁用所有按钮。
        """
        if winner == "Tie":
            message = "It's a tie!"
        else:
            message = f"Player {winner} wins!"
        for row in self.buttons:
            for button in row:
                button.config(state="disabled")
        self.root.title(message)

    def start(self):
        """
        开始游戏。
        """
        self.root.mainloop()

# 运行游戏
game = TicTacToeGUI()
game.start()
