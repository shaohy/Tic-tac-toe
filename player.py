import random


class Player:
    def __init__(self, colour):
        """
        两种颜色 CIRCLE CROSS
        :param colour:
        """
        self.colour = colour

    def next_move(self, board):
        """
        用input获取坐标x, y
        :param board: 输入一个棋盘
        :return: 要落子的坐标 int index
        """
        move = None
        available_moves = board.available_moves()
        while move is None:
            prompt = input("Enter a coordinate: ")
            if len(prompt) != 3:
                continue
            x, y = int(prompt[0]), int(prompt[2])
            move = self._parse_coordinates(x, y)
            if (x, y) not in available_moves:
                move = None
                continue
        return move

    def get_colour(self):
        """
        :return: 玩家的颜色
        """
        return self.colour

    def __str__(self):
        return "Player"

    def __repr__(self):
        return self.__str__()

    @staticmethod
    def _parse_coordinates(x, y):
        """
        Parses (x, y) coordinates into board coordinates.
        :return: int index
        """
        return (int(y) - 1) * 3 + int(x) - 1


class AIPlayer(Player):
    def next_move(self, board):
        """
        修改让电脑自己决定落子位置
        :param board:
        :return:
        """
        x, y = random.choice(board.available_moves())
        return self._parse_coordinates(x, y)

    def __str__(self):
        return "AIPlayer"
