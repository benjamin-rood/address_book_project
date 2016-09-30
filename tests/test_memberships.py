import pytest
from addressbook.book import Book


def test_memberships(book):
    for person in book.Persons:
        groups = person.membership
        for groupID in groups:
            assert person in book.Groups[groupID]
