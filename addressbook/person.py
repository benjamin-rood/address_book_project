class Person(object):
    '''Person record, gets stored in (Address) Book'''

    def __init__(self, fn: str, ln: str, phone: str, email: str,
                 street: str, membership: set=set()):
        self.first_name = fn
        self.last_name = ln
        self.phone = {phone}
        self.email = {email}
        self.street = {street}
        self.membership = membership  # keys to groups the person blongs to

    def name(self):
        return self.first_name + ' ' + self.last_name
