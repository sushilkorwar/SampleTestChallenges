from zipcode import format_zipcode 
from unittest import TestCase
from unittest.mock import patch, MagicMock

class TestZipCode(TestCase):
    
    def test_format_zipcode(self):
        '''Unittest for 'format_zipcode' function.'''

        ## Test for the length of zip_code less than 5
        self.assertEqual(format_zipcode('abc'), '00abc')

        ## Test for the length of zip_code equals to 10
        self.assertEqual(format_zipcode('abcd1234yz'), 'abcd1234yz')

        ## Test for the length of zip_code equals to 9
        self.assertEqual(format_zipcode('1234abcdz'), '1234a-bcdz')

        ## Test for invalid input
        self.assertRaises(TypeError, format_zipcode, 1234)
