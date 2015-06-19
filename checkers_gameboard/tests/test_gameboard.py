import unittest
import sys
import os
sys.path.append('../')
print os.getcwd()
from gameboard.draw import *

class TestGameboard(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_gameboard(self):
        board = create_gameboard()
        self.assertTrue(board)
        self.assertTrue(type(board) == list)
        for n in range(0,64):
            if board[n].get('number') == 9:
                self.assertEquals(board[n].get('color'),
                                  board[n-1].get('color'))

        for i in board:
            print "%s - %s" % (i.get('number'), i.get('color'))

            
