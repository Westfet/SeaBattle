from random import randint
from Board import Board
from Ship import Ship
from User import User
from AI import AI
from BoardWrongShipException import BoardWrongShipException


def greet():
    print("-------------------")
    print(" Приветствуем вас  ")
    print("      в игре       ")
    print("    морской бой    ")
    print("-------------------")
    print(" формат ввода: x y ")
    print(" x - номер строки  ")
    print(" y - номер столбца ")


class GameProcess:
    def __init__(self, size=6):
        self.size = size
        player = self.random_board()
        computer = self.random_board()
        computer.hidden = True
        self.ai = AI(computer, player)
        self.user = User(player, computer)

    def try_board(self):
        lens = [3, 2, 2, 1, 1, 1, 1]
        board = Board(size=self.size)
        attempts = 0
        for l in lens:
            while True:
                attempts += 1
                if attempts > 2000:
                    return None
                this_x = randint(0, self.size)
                this_y = randint(0, self.size)
                ship = Ship(l, randint(0, 1), this_y, this_x)
                try:
                    board.add_ship(ship)
                    break
                except BoardWrongShipException:
                    pass
        board.begin()
        return board

    def random_board(self):
        board = None
        while board is None:
            board = self.try_board()
        return board

    def loop(self):
        num = 0
        while True:
            print("-" * 20)
            print("Доска пользователя:")
            print(self.user.board)
            print("-" * 20)
            print("Доска компьютера:")
            print(self.ai.board)
            if num % 2 == 0:
                print("-" * 20)
                print("Ходит пользователь!")
                repeat = self.user.move()
            else:
                print("-" * 20)
                print("Ходит компьютер!")
                repeat = self.ai.move()
            if repeat:
                num -= 1

            if self.ai.board.amount == 7:
                print("-" * 20)
                print("Пользователь выиграл!")
                break

            if self.user.board.amount == 7:
                print("-" * 20)
                print("Компьютер выиграл!")
                break
            num += 1

    def start(self):
        greet()
        self.loop()
