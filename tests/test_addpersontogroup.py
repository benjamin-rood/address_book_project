import pytest
from addressbook.book import Book
from addressbook.person import Person


def test_add_person_to_group(people):
    book = Book()
    for person in people:
        book.add_person_to_group(person, 'testgrp')
        assert person in book.Groups['testgrp']
        assert 'testgrp' in person.membership
