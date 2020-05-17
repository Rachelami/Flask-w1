from ExtendedPost import ExtendedPost
import json


class JsonablePost(ExtendedPost):
    def to_json(self):
        return json.dumps(self.__dict__),

    def __init__(self, userId, id, title, body):
        ExtendedPost.__init__(self, userId, id, title, body)


        # data = ExtendedPost(1, 1, 'hello', 'all my friend')
        # myJson = json.dumps(data.__dict__),
        # myJson = json.dumps(data, default=lambda o: o.__dict__),
        # return myJson
