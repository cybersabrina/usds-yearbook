import collections
import json

import person

class Directory(object):
    """ The set of people and their related information. 

        Python doesn't have interfaces, but this is basically the interface for
        the Directory service/API.
    """

    def list(self):
        """ Lists all of the users in the directory.

        Returns:
            List of all of the Person objects in the directory.
        """
        raise NotImplementedError('Derived classes must implement this method')

    def get(self, user_id):
        """ Gets the person in the directory with the given id.

        Args:
            id: (string) The GitHub username of the person being looked up.
        
        Returns:
            The Person object from the directory. None if they can't be found.
        """
        raise NotImplementedError('Derived classes must implement this method')

    def update(self, person):
        raise NotImplementedError('Derived classes must implement this method')

    def create(self, person):
        raise NotImplementedError('Derived classes must implement this method')

    def __str__(self):
        return repr(self)

    def __repr__(self):
        return '\n\t' + '\n\t'.join([str(x) for x in self.list()])

    def to_json(self):
        return json.dumps(self, cls=DirectoryEncoder, indent=2)


class DirectoryEncoder(json.JSONEncoder):

    def default(self, obj):
        if isinstance(obj, person.Person):
            return person.PersonEncoder().default(obj)
        if isinstance(obj, Directory):
            result = collections.OrderedDict()
            result['type'] = 'directory.Directory'
            result['people'] = obj.list()
            return result
        return obj
 