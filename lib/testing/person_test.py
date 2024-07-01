# lib/person_test.py

import pytest
from lib.person import Person

class TestPerson:
    def test_is_class(self):
        '''is a class with the name "Person"'''
        john = Person(name="John")
        assert isinstance(john, Person)
        assert john.name == "John"

    def test_talk_method(self):
        '''Person class has a talk method'''
        john = Person(name="John")
        assert hasattr(john, 'talk')
        john.talk()

    def test_walk_method(self):
        '''Person class has a walk method'''
        john = Person(name="John")
        assert hasattr(john, 'walk')
        john.walk()

    def test_invalid_name(self):
        '''Person name must be string between 1 and 25 characters'''
        john = Person(name="")
        assert john.name is None
        john.name = "A very long name that exceeds the limit"
        assert john.name is None

    def test_invalid_job(self):
        '''Person job must be in list of approved jobs'''
        john = Person(name="John", job="Unknown")
        assert john.job is None
        john.job = "Invalid Job"
        assert john.job is None
