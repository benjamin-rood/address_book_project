===================
Simple Address Book
===================

Version: 0.0.1

A **Person** object consists of `first_name` and `last_name` string fields, sets of telephone numbers, email, and physical addresses (all as strings), as well as the set of keys to Groups which a Person is a member of.

Let us look at an example represented as a JSON object:

::

    {
        first_name: 'Adam',
        last_name: 'West',
        phone: {'681-705-8384', '620-187-0901'},
        email: {'adam.west@mail.com'},
        street: {'''4 East Arnold Dr.
                    Goose Creek
                    SC 29445
                    U.S.A.'''},
        membership: {'Males', 'American'}
    }

*(n.b. Of the above fields, when creating a Person object instance only the membership set is optional)*


An **(Address) Book** object consists of the collection of all individual **Persons**, and **Groups** of Person objects.

We can illustrate an example Address Book as a JSON object:

::

    {
        Persons: {
            {
                first_name: 'Adam',
                last_name: 'West',
                phone: {'681-705-8384', '620-187-0901'},
                email: {'adam.west@mail.com'},
                street: {'''4 East Arnold Dr.
                            Goose Creek
                            SC 29445
                            U.S.A.'''},
                membership: {'Males', 'American'}
            },
            {
                first_name: 'David',
                last_name: 'Jones',
                phone: {'362-007-4797'},
                email: {'david.jones@mail.com', 'davidj@yahoo.com'},
                street: {'''53 Thorne Dr.
                            Salt Lake City
                            UT 84119
                            U.S.A.'''},
                membership: {'Males', 'American'}
            },
            {
                first_name: 'Benjamin',
                last_name: 'Rood',
                phone: {'64-22-0235611', '09-446-1055'},
                email: {'benisrood@gmail.com', 'ben@yahoo.co.nz'},
                street: {},
                {'Males', 'Kiwi'}
            }
        },
        'Groups': {
            'Males': {<David Jones Person object>,
                <Adam West Person object>, <Benjamin Rood Person object>},
            'American': {<David Jones Person object>,
                <Adam West Person object>},
            'Kiwi': {<Benjamin Rood Person object>}
        }
    }


All **Person** objects are collected in the *Persons* set of an (Address) Book object.

Furthermore, as each Person object in the Address Book "refers" to the same Person in memory, we can use *sets* to collect the Person objects as a Group and inherit the property of sets which requires that all elements be unique: this means that when adding Person(s) to a Group we do not have to worry about duplication *internally* inside the Address Book.

Note that a Person need not be a member of any groups at all, but the membership set of a Person and its existence in a given Group must correspond exactly *i.e. the sets are guaranteed isomorphic within an (Address) Book object if using the class Methods.*

In fact, this is the logic behind using Python's set type for all *multiples* in the Address Book library: Simplicity and the Principle of Least Surprise.



Basic Usage
-------------------
::

    # create an Address Book

    >>> from addressbook.book import Book

    >>> book = Book() # new (empty) address book

    # create a person object

    >>> from addressbook.person import Person

    >>> jean_luc = Person('Jean-Luc',
                    'Picard',
                    '+33 (1) 53 90 20 20',
                    'picard.jl@starfleet.ufp',
                    '''Impasse de la Sylve
                    85550 La Barre-de-Monts
                    France''',
                    {'Males', 'French'})

    # add Person record to Address Book:
    >>> book.add_person(jean_luc)
    '45aca510-9892-4961-9901-b61102cb531b'

    # add Person record to a Group in the Address Book:
    >>> book.add_person_to_group(jean_luc, 'Starfleet')

In the code above, when ``jean_luc`` is added to ``book``, he will automatically be added to the 'Males' and 'French' Groups also.

With the next command to add ``jean_luc`` to a new Group named 'Starfleet', the Group is created inside `book` and ``jean_luc`` is added to it - in addition, 'Starfleet' is added to the membership set for the ``jean_luc`` object itself.

Suppose, however, that the ``jean_luc`` Person object was not already part of the Persons collected in the Address Book? In that case 'Starfleet' would be added to the membership set in ``jean_luc``, and the *add_person* method would be called instead. In this way, we preseve the required isomorphism of the membership set of any Person object in an Address Book.

In addition, the following features are also provided for as methods on an Address Book object:

*find_persons_by_name(search_term)*: Takes a (case-insensitive) string and searches for ANY partial matches in the combined *first_name* and *last_name* fields of all Persons in the Address Book, returning the set of Persons where a partial match was found.

*find_persons_by_email(search_term)*: Takes a (case-insensitive) string and searchwa for ANY partial matches in the set of email addresses for all Persons in the address book, returning the set of Persons where a partial match was found.

*find_memberships(person)*: Returns the set of groupIDs (keys) which identify the groups the person is a member of in the Address Book object.
*n.b. If the person* **object** *is not already present in the Address Book, the empty set is returned.*

*get_persons_in_group(groupID)*: Returns the set of Person objects in the Group corresponding to the provided ``groupID`` string.
*n.b. If the provided* ``groupID`` *does not match any Group in the Address Book, then the empty set is returned.*
