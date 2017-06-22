import collections
import json

import person
import directory

class LocalDirectory(directory.Directory):
    """ The set of people and their related information. 

        Python doesn't have interfaces, but this is basically the interface for
        the Directory service/API.
    """

    # people arg is a list of People objects
    def __init__(self, people):
        self.people = collections.OrderedDict()
        for person in people:
            self.people[person.user_id] = person

    def list(self):
        """ Lists all of the users in the directory.

        Returns:
            List of all of the Person objects in the directory.
        """
        return sorted(self.people.values(), key=lambda x: x.user_id)

    def get(self, user_id):
        """ Gets the person in the directory with the given id.

        Args:
            id: (string) The GitHub username of the person being looked up.
        
        Returns:
            The Person object from the directory. None if they can't be found.
        """
        return self.people.get(user_id, default=None)

    def update(self, person):
        self.people[person.user_id] = person

    def create(self, person):
        self.update(person)

    def __str__(self):
        return repr(self)

    def __repr__(self):
        return '\n\t' + '\n\t'.join([str(x) for x in self.list()])

    @staticmethod
    def from_json(data):
        return json.loads(data, cls=LocalDirectoryDecoder)

class LocalDirectoryDecoder(json.JSONDecoder):

    def __init__(self, *args, **kwargs):
        super(LocalDirectoryDecoder, self).__init__(object_hook=self.parse_data, *args, **kwargs)

    def parse_data(self, data):
        if 'type' in data:
            t = data['type']
            if t == 'directory.Person':
                return person.PersonDecoder().parse_data(data)
            if t == 'directory.Directory':
                return LocalDirectory(data['people'])
        return data


