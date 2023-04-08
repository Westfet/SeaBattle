from BoardExceptions import BoardException


class BoardUsedException(BoardException):

    def __str__(self):
        return "Вы уже стреляли в эту клетку"
