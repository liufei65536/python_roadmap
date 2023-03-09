import time
import tkinter as tk


class Board:
    def __init__(self, size=3):
        self.board = [['-' for j in range(size)] for i in range(size)]
        self.size = size

    def __getitem__(self, key):
        return self.board[key]

    def __setitem__(self, key, value):
        pass

    def __str__(self):
        res = ""
        for row in self.board:
            temp_row = ""
            for col in row:
                temp_row = temp_row + col + '\t'
            res += str(temp_row) + "\n"
        return res

    def display(self):
        print(self)

    def can_set(self, row, col):
        return 0 <= row < self.size and \
               0 <= col < self.size and \
               self.board[row][col] == '-'

    def set_board(self, row, col, mark):
        if self.can_set(row, col):
            self.board[row][col] = mark
        else:
            print("Invalid input...,")

    def check_win(self):
        for row in self.board:
            if all(x == 'X' for x in row):
                return "Player X wins"
            elif all(x == 'O' for x in row):
                return "Player O wins"

        for col in range(self.size):
            if all(self.board[row][col] == 'X' for row in range(self.size)):
                return "Player X wins"
            elif all(self.board[row][col] == 'O' for row in range(self.size)):
                return "Player O wins"

        # Diagonal
        if all(self.board[i][i] == 'X' for i in range(self.size)) or all(
                self.board[i][self.size - 1 - i] == 'X' for i in range(self.size)):
            return "Player X wins"
        elif all(self.board[i][i] == 'O' for i in range(self.size)) or all(
                self.board[i][self.size - 1 - i] == 'O' for i in range(self.size)):
            return "Player O wins"

        if self.is_full():
            return "Tie"
        return None

    def is_full(self):
        return not any(self.board[i][j] == '-' for i in range(self.size) for j in range(self.size))

    def copy(self):
        new_board = Board(self.size)
        for i in range(self.size):
            for j in range(self.size):
                new_board.board[i][j] = self.board[i][j]
        return new_board



class AIPlayer:
    def __init__(self, player, mark):
        self.player = player
        self.mark = mark
        self.human_mark = 'O' if self.mark == 'X' else 'X'

    def get_best_move(self, board):
        best_score = -1000
        best_move = None

        for row in range(board.size):
            for col in range(board.size):
                if board.can_set(row, col):
                    board_copy = board.copy()
                    board_copy.set_board(row, col, self.mark)
                    score = self.minimax(board_copy, False, -1000, 1000)
                    if score > best_score:
                        best_score = score
                        best_move = (row, col)

        return best_move

    def minimax(self, board, is_maximizing, alpha, beta):
        result = board.check_win()
        if result == f"Player {self.human_mark} wins":
            return -1
        elif result == f"Player {self.mark} wins":
            return 1
        elif board.is_full():
            return 0

        # （AI回合）使AI分数最大
        if is_maximizing:
            best_score = -1000
            for row in range(board.size):
                for col in range(board.size):
                    if board.can_set(row, col):
                        board_copy = board.copy()
                        board_copy.set_board(row, col, 'O')
                        score = self.minimax(board_copy, False, alpha, beta)
                        best_score = max(best_score, score)
                        alpha = max(alpha, best_score)
                        if beta <= alpha:
                            break
            return best_score

        # （人类回合）使AI分数最少
        else:
            best_score = 1000
            for row in range(board.size):
                for col in range(board.size):
                    if board.can_set(row, col):
                        board_copy = board.copy()
                        board_copy.set_board(row, col, 'X')
                        score = self.minimax(board_copy, True, alpha, beta)
                        best_score = min(best_score, score)
                        beta = min(beta, best_score)
                        if beta <= alpha:
                            break
            return best_score


class TicTacToeGUI:
    def __init__(self, ai_mode=True, ai_first=False):
        self.root = tk.Tk()
        self.root.title("Tic Tac Toe")
        self.board = Board(3)
        # 创建9个按钮
        self.buttons = []
        for i in range(3):
            row = []
            for j in range(3):
                button = tk.Button(self.root, text="", font=("Helvetica", 24), width=5, height=2,
                                   command=lambda row=i, col=j: self.clicked(row, col))
                button.grid(row=i, column=j)
                row.append(button)
            self.buttons.append(row)

        self.ai_mode = ai_mode
        self.ai_first = ai_first
        self.player_marks = ['X', 'O']
        self.current_player = 0  # 0 or  1
        if self.ai_mode:
            if self.ai_first :
                self.ai_player = AIPlayer(0, self.player_marks[0])
                row, col = self.ai_player.get_best_move(self.board)
                self.board.set_board(row, col, self.ai_player.mark)
                self.buttons[row][col].config(text=self.ai_player.mark)
                self.current_player = (self.current_player + 1) % 2
            else:
                self.ai_player = AIPlayer(1, self.player_marks[1])

    def set_board(self, row, col, mark):
        self.buttons[row][col].config(text=mark)
        self.board.set_board(row, col, mark)

    def clicked(self, row, col):
        """
        当一个按钮被点击时，将其设置为当前玩家的标记，并切换到下一个玩家。
        如果下一个玩家是AI，则使用AI下棋
        """
        # 位置非空，此次点击无效，返回
        if self.board[row][col] != "-":
            return

        # ai 模式
        if self.ai_mode:
            self.set_board(row, col, self.player_marks[self.current_player])

            if not self.board.is_full() and self.board.check_win() is None:
                self.current_player = (self.current_player + 1) % 2  # 切到ai
                self.board.display()  # debug

                row, col = self.ai_player.get_best_move(self.board.copy())
                self.set_board(row, col, self.player_marks[self.current_player])

                self.current_player = (self.current_player + 1) % 2  # 切回人类
        # 双人模式
        else:
            self.set_board(row, col, self.player_marks[self.current_player])
            # 换下一个人
            self.current_player = (self.current_player + 1) % 2

        res = self.board.check_win()
        if res is not None:
            print(self.board)
            self.show_winner(res)

    def show_winner(self, winner):
        """
        显示获胜者或平局信息，并禁用所有按钮。
        """
        if winner == "Tie":
            message = "It's a tie!"
        else:
            message = f" {winner}!"
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
game = TicTacToeGUI(ai_mode=True, ai_first=True)
game.start()
