#!/usr/bin/python3

from dataclasses import dataclass
from dacite import from_dict


@dataclass
class User:
    name: str
    age: int
    is_active: bool


data = {
    'name': 'John',
    'age': 30,
    'is_active': True,
}

user = from_dict(data_class=User, data=data)

assert user == User(name='John', age=30, is_active=True)
