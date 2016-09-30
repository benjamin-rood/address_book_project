import pytest
from addressbook.book import Book


def test_add_person(people):
    book = Book()
    for person in people:
        book.add_person(person)
        assert person in book.Persons
