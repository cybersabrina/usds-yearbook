import collections
import json

class Person(object):

    def __init__(self, user_id, name, bio, image_url):
        self.user_id = user_id
        self.name = name
        self.bio = bio
        self.image_url = image_url

    def __str__(self):
        return repr(self)

    def __repr__(self):
        return '%s (%s) [%s] %s' % (self.name, self.user_id, self.image_url, self.bio)

    def to_json(self):
        return json.dumps(self, cls=PersonEncoder)

    @staticmethod
    def from_json(data):
        return json.loads(data, cls=PersonDecoder)


class PersonEncoder(json.JSONEncoder):

    def default(self, obj):
        if isinstance(obj, Person):
            result = collections.OrderedDict()
            result['type'] = 'directory.Person'
            result['user_id'] = obj.user_id
            result['name'] = obj.name
            result['bio'] = obj.bio
            result['image_url'] = obj.image_url
            return result
        return obj
 

class PersonDecoder(json.JSONDecoder):

    def __init__(self, *args, **kwargs):
        super(PersonDecoder, self).__init__(object_hook=self.parse_data, *args, **kwargs)

    def parse_data(self, data):
        if 'type' in data:
            t = data['type']
            if t == 'directory.Person':
                return Person(
                    data['user_id'],
                    data['name'],
                    data['bio'],
                    data['image_url']
                )
        return data
