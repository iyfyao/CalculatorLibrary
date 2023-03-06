"""
unit tests for Calculator module.
"""
# pylint : disable =  E0211

from unittest import TestCase

from .. import calculator


class TestCalculator(TestCase):
    """testing calculator class"""

    def test_addition(self): # pylint : disable =  E0211
        """unit test for addition"""
        assert 4 == calculator.addition(2, 2)

    def test_substraction(self): # pylint : disable =  E0211
        """Unit test for substraction"""
        assert 0 == calculator.substraction(2,2)
