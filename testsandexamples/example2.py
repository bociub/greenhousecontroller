#You cannot just dump the content of an object, even an object as simple as this one.
    
import json


class Who:
    def __init__(self, name, age):
        self.name = name
        self.age = age


def encode_who(w): #encoder!!!
    if isinstance(w, Who):
        return w.__dict__
    else:
        raise TypeError(w.__class__.__name__ + ' is not JSON serializable')


some_man = Who('John Doe', 42)
print(json.dumps(some_man, default=encode_who))

#Note: the process in which an object (stored internally by Python) is converted into textual or any other portable aspect is often called serialization. Similarly, the reverse action (from portable into internal) is called deserialization.
