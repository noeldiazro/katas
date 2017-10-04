import unittest


class LeapYearTest(unittest.TestCase):

    def test_normal_leap_year(self):
        self.assertTrue(is_leap(1996))

    def test_normal_common_year(self):
        self.assertFalse(is_leap(2001))

    def test_atypical_common_year(self):
        self.assertFalse(is_leap(1900))

    def test_atypical_leap_year(self):
        self.assertTrue(is_leap(2000))


def is_leap(year):
    return _is_normal_leap_year(year) and not _is_atypical_common_year(year)

def _is_atypical_common_year(year):
    return year % 100 == 0 and not year % 400 == 0

def _is_normal_leap_year(year):
    return year % 4 == 0
