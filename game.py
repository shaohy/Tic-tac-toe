from collections import deque

from board import Board
from player import Player, AIPlayer
from settings import CROSS, CIRCLE


class Game:
    def __init__(self, players):
        self.board = Board()
        self.list_of_colours = [CROSS, CIRCLE]
        self.players = players
        self.controllers = deque([self._make_controller(c, p) for c, p in zip(self.list_of_colours, self.players)])

    @staticmethod
    def _make_controller(colour, controller_type):
        """
        Returns a controller with the specified colour.
        "player" == Player,
        "ai" == AiPlayer.
        """
        if controller_type == "player":
            return Player(colour)
        else:
            return AIPlayer(colour)

    def show_info(self):
        """
        Prints game information to stdout.
        """
        print("Playing as:       " + self.controllers[0].get_colour())
        print("Current turn:     " + str(self.controllers[0]))

    def show_commands(self):
        moves = self.board.available_moves()
        print("Possible moves are: ", ", ".join([str(i) for i in moves]))

    def run(self):
        """ The game loop will print game information, the board, the possible moves, and then wait for the
            current player to make its decision before it processes it and then goes on repeating itself.
        """
        while True:
            self.show_info()
            self.show_commands()
            print(self.board)
            available_moves = self.board.available_moves()
            cross_win = self.board.is_win_for(CROSS)
            circle_win = self.board.is_win_for(CIRCLE)
            if cross_win:
                print("Cross won this game.")
                exit()
            if circle_win:
                print("Circle won this game.")
                exit()
            if not available_moves:
                print("This game was a tie.")
                exit()
            next_move = self.controllers[0].next_move(self.board)
            self.board.set_piece(next_move, self.controllers[0].get_colour())
            self.controllers.rotate(1)
