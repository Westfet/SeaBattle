from Dot import Dot


class Ship(Dot):

    # direction = 0 - корабль горизонтальный, 1 - вертикальный
    def __init__(self, length, direction, x, y):
        super().__init__(x, y)
        self.length = length
        self.direction = direction
        self.lives = length

    # property потому что не просто метод, а метод-свойство
    @property
    def dots(self):
        ship_dots = []
        for i in range(self.length):
            this_x = self.x
            this_y = self.y
            if not self.direction:
                this_x += i
            else:
                this_y += i
            ship_dots.append(Dot(this_x, this_y))
        return ship_dots

