# Test file - Game of life
import unittest
from project import *

class TestProject(unittest.TestCase):
    """Test project.py"""

    def test_main_Beacon(self):
        """Test main Beacon """
        map2 = np.ones((maxx + 1, maxy + 1))*0
        map2[2][4] = 1
        self.assertEqual(map2.all(), input_map(3,5).all())


if __name__ == '__main__':
    unittest.main()
