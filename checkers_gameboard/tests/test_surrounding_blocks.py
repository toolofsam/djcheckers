import unittest
import sys
import os
sys.path.append('../')
print os.getcwd()
from gameboard.move import *
from gameboard.draw import *


class TestSurroundingMembers(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_surrounding(self):
        grid = create_gameboard()
        n = where_can_i_go(grid, 38)
        print "Surrounding %s is %s" % (38, n)
        
        n = where_can_i_go(grid, 12)
        print "Surrounding %s is %s" % (12, n)
        
        n = where_can_i_go(grid, 4)
        print "Surrounding %s is %s" % (4, n)

        n = where_can_i_go(grid, 62)
        print "Surrounding %s is %s" % (63, n)
