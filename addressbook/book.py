from .person import Person


class Book(object):
    '''(Address)Book is a collection of Persons and Groups,
    where a Group is a collection of uuids identifying the
    persons who are members of that group.'''

    def __init__(self):
        self.Persons = set()
        self.Groups = {}

    def add_person(self, person: Person):
        self.Persons |= {person}
        for groupID in person.membership:
            if groupID not in self.Groups:
                self.Groups[groupID] = set()
            self.Groups[groupID] |= {person}

    def find_persons_by_name(self, search_term: str) -> set:
        search_term = search_term.lower()
        result = {person for person in self.Persons
                  if search_term in person.name().lower()}
        return result

    def find_persons_by_email(self, search_term: str) -> set:
        search_term = search_term.lower()
        result = set()
        for person in self.Persons:
            result |= {person for email in person.email
                       if search_term in email}
        return result

    def find_memberships(self, person: Person) -> set:
        result = set()
        if person in self.Persons:
            for groupID in person.membership:
                if groupID in self.Groups:
                    result |= groupID
        return result

    def add_person_to_group(self, person: Person, groupID: str):
        person.membership |= {groupID}
        self.add_person(person)

    def get_persons_in_group(self, groupID: str) -> set:
        result = set()
        if groupID in self.Groups:
            result = self.Groups[groupID]
        return result
