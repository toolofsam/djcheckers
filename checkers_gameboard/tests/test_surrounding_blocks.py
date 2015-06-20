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

        n = where_can_i_go(grid, 63)
        print "Surrounding %s is %s" % (63, n)

        print "\n\nGetting edges"
        
        n = 36
        left_edge = get_left_edge(n)
        right = get_right_edge(n)
        self.assertEquals(left_edge, 33)
        self.assertEquals(right_edge, 40)

        n = 4
        left_edge = get_left_edge(n)
        right_edge = get_right_edge(n)
        self.assertEquals(left_edge, 1)
        self.assertEquals(right_edge, 8)

        n = 63
        left_edge = get_left_edge(n)
        right_edge = get_right_edge(n)
        self.assertEquals(left_edge, 57)
        self.assertEquals(right_edge, 64)



if __name__ == "__main__":
    unittest.main()
