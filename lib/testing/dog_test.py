# dog_test.py

import pytest
from lib.dog import Dog

class TestDog:
    def test_invalid_breed(self):
        '''Dog breed must be in list of approved breeds'''
        fido = Dog(name="Fido", breed="Unknown")
        assert fido.breed is None

    # Add other test cases as needed
