import pytest


def test_find_person_by_name(book):
    for person in book.Persons:
        first_name_results = book.find_persons_by_name(person.first_name)
        assert person in first_name_results
        last_name_results = book.find_persons_by_name(person.last_name)
        assert person in last_name_results
        name_results = book.find_persons_by_name(person.name())
        assert person in name_results
