"""
Sample tests
"""

from django.test import SimpleTestCase
from app import calc

class CalcTests(SimpleTestCase):
    """Test calc modules"""
    
    def test_add(self):
        """Test add function"""
        res = calc.add(5,6)
        self.assertEqual(res,11)

    def test_subtract(self):
        """Test subtract function"""
        res = calc.subtract(10,15)
        self.assertEqual(res, -5)



    


        