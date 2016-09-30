# tests/config.py
import pytest
from addressbook.book import Book
from addressbook.person import Person

adam = Person('Adam',
              'West',
              '681-705-8384',
              'adam.west@mail.com',
              '''4 East Arnold Dr.
              Goose Creek,
              SC 29445
              U.S.A.''',
              {'Boys', 'American'})

alexander = Person('Alexander',
                   'Popov',
                   '+7-495-555-12-34',
                   'alexander@company.com',
                   '''Lesnoy,
                   Sverdlovsk,
                   Russia''',
                   {'Boys', 'Russian'})

ben = Person('Ben',
             'Jones',
             '362-007-4797',
             'ben.jones@mail.com',
             '''53 Thorne Dr.
             Salt Lake City,
             UT 84119
             U.S.A.''',
             {'Boys', 'American'})

mike = Person('Michael',
              'Jordan',
              '842-248-6197',
              'idunk@nike.com',
              '''708 Kent Rd.
              Neptune,
              NJ 07753,
              U.S.A.''',
              {'Boys', 'American'})

sally = Person('Sally',
               'Draper',
               '908-834-7645',
               'nil',
               '''7396 Pennsylvania Ave.
               Clifton Park,
               NY 12065,
               U.S.A.''',
               {'Girls', 'American'})

jean_luc = Person('Jean-Luc',
                  'Picard',
                  '+33 (1) 53 90 20 20',
                  'picard.jl@starfleet.ufp',
                  '''Impasse de la Sylve
                  85550 La Barre-de-Monts
                  France''',
                  {'Boys', 'French'})


@pytest.fixture(scope='module')
def people():
    return {adam, alexander, ben, mike, sally, jean_luc}


@pytest.fixture(scope='module')
def book():
    test_book = Book()
    for p in {adam, alexander, ben, mike, sally, jean_luc}:
        test_book.add_person(p)
    return test_book
