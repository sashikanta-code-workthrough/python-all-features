from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class User:
    name: str
    age: int

    def can_vote(self) -> bool:
        return self.age >= 18


def dataclasses_demo() -> None:
    u = User(name="Asha", age=21)
    print(u)
    print("can_vote:", u.can_vote())
