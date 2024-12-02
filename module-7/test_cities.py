# Kyle Marlia-Conner
# Assignment 7.2

import unittest
from city_functions import format_city_country

class TestCityFunctions(unittest.TestCase):
    ### Tests for the 'format_city_country' function.
    
    def test_city_country(self):
        """Test that city and country are formatted correctly."""
        formatted = format_city_country("Santiago", "Chile")
        self.assertEqual(formatted, "Santiago, Chile")

if __name__ == "__main__":
    unittest.main()