from BoardExceptions import BoardException


class BoardOutException(BoardException):
    def __str__(self):
        return "Выбранная точка находится за границами доски"

