from settings import EMPTY


class Board:
    def __init__(self):
        """
        EMPTY 代表没有棋子
        """
        self.pieces = [EMPTY for _ in range(9)]

    def __str__(self):
        """
        O | X | O
        X | O | X
        O | O | X
        :return: string
        """
        return "{}\n{}\n{}".format(" | ".join(self.pieces[:3]),
                                   " | ".join(self.pieces[3:6]),
                                   " | ".join(self.pieces[6:]))

    def __repr__(self):
        return self.__str__()

    def set_piece(self, i, colour):
        """
        :param i:
        :param colour:
        :return: 把对应坐标设成指定颜色
        """
        self.pieces[i] = colour

    def available_moves(self):
        """
        [(0, 2), (1, 1), (x, y)]
        :return: 返回可以走的位置
        """
        output = []
        for y in range(3):
            for x in range(3):
                if self.pieces[y * 3 + x] == EMPTY:
                    output.append((x + 1, y + 1))
        return output

    def is_win_for(self, colour):
        """
        检查当前棋盘玩家是否胜出
        :return: bool
        """
        for i in range(0, 8, 3):
            if len(set(self.pieces[i:i + 3])) == 1 and self.pieces[i] == colour:
                return True
        for i in range(3):
            if len({self.pieces[i], self.pieces[i + 3], self.pieces[i + 6]}) == 1 and self.pieces[i] == colour:
                return True
        if len({self.pieces[0], self.pieces[4], self.pieces[8]}) == 1 and self.pieces[4] == colour:
            return True
        if len({self.pieces[2], self.pieces[4], self.pieces[6]}) == 1 and self.pieces[4] == colour:
            return True
        return False
