from Dot import Dot
from BoardWrongShipException import BoardWrongShipException
from BoardUsedException import BoardUsedException
from BoardOutException import BoardOutException


class Board:

    def __init__(self, size, hidden=0):
        self.size = size
        self.hidden = hidden
        self.amount = 0
        # equal self.field = [["0"] * size] * size
        self.field = [["0"] * size for _ in range(size)]
        # задействованные точки
        self.busy = []
        # список кораблей
        self.ships = []

    def __str__(self):
        result = "  | 1 | 2 | 3 | 4 | 5 | 6 |"
        # с помощью enumerate в i записывается № элемента, а в j - сам элемент
        for i, j in enumerate(self.field):
            result += f"\n{i + 1} | " + " | ".join(j) + " |"
        if self.hidden:
            result = result.replace("■", "O")
        return result

    def out(self, d):
        return not ((0 <= d.x < self.size) and (0 <= d.y < self.size))

    def around(self, ship, verb=False):
        near = [
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1), (0, 0), (0, 1),
            (1, -1), (1, 0), (1, 1)
        ]
        for d in ship.dots:
            for dx, dy in near:
                this = Dot(d.x + dx, d.y + dy)
                if not (self.out(this)) and this not in self.busy:
                    if verb:
                        self.field[this.x][this.y] = "."
                    self.busy.append(this)

    def add_ship(self, ship):
        for i in ship.dots:
            if self.out(i) or i in self.busy:
                raise BoardWrongShipException()
        for i in ship.dots:
            self.field[i.x][i.y] = "■"
            self.busy.append(i)
        self.ships.append(ship)
        self.around(ship)

    def shot(self, d):
        if self.out(d):
            raise BoardOutException()
        if d in self.busy:
            raise BoardUsedException()
        self.busy.append(d)
        for ship in self.ships:
            if d in ship.dots:
                ship.lives -= 1
                self.field[d.x][d.y] = "X"
                if ship.lives == 0:
                    self.amount += 1
                    self.around(ship, verb=True)
                    print("Корабль уничтожен!")
                    return False
                else:
                    print("Корабль ранен!")
                    return True
        self.field[d.x][d.y] = "."
        print("Мимо!")
        return False

    def begin(self):
        self.busy = []
