from typing import TypedDict


class Person(TypedDict):
    id: int
    name: str


p = Person(id=1, name='Вася')

print(p)
