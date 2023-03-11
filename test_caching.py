import unittest
from caching.core import CachingMechanism

class TestCaching(unittest.TestCase):
    """Test functions in CachingMechanism"""

    def setUp(self) :
        """Creat initial mechanism"""
        self.mechanism = CachingMechanism(["Lord of the Rings", "The Titanic", "Snow White"],[("New York", 10.4, -12.1), ("Athens", 47.4, 3.6)],2)

    def test_lookup(self):
        """Test if the lookup function can return False if the movie is not in the cache"""
        result1 = self.mechanism.lookup("The Titanic", 10.5, -11.7)
        self.assertEqual(result1,(False, None))

    def test_find_nearest_cache(self):
        """Test if the find_nearest_cache function can correctly find the nearest cache"""
        result2 = self.mechanism.find_nearest_cache(10, -14)
        self.assertEqual(result2, 'New York')

    def test_lookup_update(self):
        """Test if looking for a movie not in the cache, the movie would be updated to the cache afterwards"""
        self.mechanism.lookup("Lord of the Rings", 10, -14)
        result3 = self.mechanism.lookup("Lord of the Rings", 10, -14)
        self.assertEqual(result3, (True, "New York"))

    def test_maximum(self):
        """Test if movies in a cache reach the maximum limit, the first movie would be dropped"""
        self.mechanism.lookup("Lord of the Rings", 10, -14)
        self.mechanism.lookup("The Titanic", 10, -14)
        self.mechanism.lookup("Snow White", 10, -14)
        result4 = self.mechanism.lookup("Lord of the Rings", 10, -14)
        self.assertEqual(result4, (False, None))

    def test_lookup_notinlist(self):
        """Test if looking for a movie not in the movie list, it would not be added to the cache"""
        self.mechanism.lookup("Fake Movie", 10.5, -11.7)
        result5 = self.mechanism.lookup("Fake Movie", 10.5, -11.7)
        self.assertEqual(result5,(False, None))