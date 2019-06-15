# Test file - Game of life
import unittest
from project import *

class TestProject(unittest.TestCase):
    """Test project.py"""

    def test_main_Beacon(self):
        """Test main Beacon """
        map1 = np.ones((maxx + 1, maxy + 1))*0
        map1[1][1] = map1[1][2] = map1[2][1] = map1[2][2] = map1[3][3] = map1[3][4] = map1[4][3] = map1[4][4] = 1

        map_after = np.ones((maxx + 1, maxy + 1))*0
        map_after[1][1] = map_after[1][2] = map_after[2][1]  = map_after[3][4] = map_after[4][3] = map_after[4][4] = 1

        self.assertEqual(map_after.all(), main(map1).all())

if __name__ == '__main__':
    unittest.main()