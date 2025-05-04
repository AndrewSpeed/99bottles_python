from typing import override


class BottleNumber:
    _number: int

    def __init__(self, number: int):
        self._number = number

    def container(self) -> str:
        return "bottles"

    def pronoun(self) -> str:
        return "one"

    def successor(self) -> "BottleNumber":
        return BottleNumber(self._number - 1)

    def quantity(self) -> str:
        return str(self._number)

    def action(self) -> str:
        return f"Take {self.pronoun()} down and pass it around"

    @override
    def __str__(self) -> str:
        return f"{self.quantity()} {self.container()}"

    @override
    def __new__(cls, number: int):
        match number:
            case 0:
                cls = BottleNumber0
            case 1:
                cls = BottleNumber1
            case _:
                cls = BottleNumber

        return super().__new__(cls)


class BottleNumber0(BottleNumber):
    @override
    def quantity(self) -> str:
        return "no more"

    @override
    def action(self) -> str:
        return "Go to the store and buy some more"

    @override
    def successor(self) -> BottleNumber:
        return BottleNumber(99)


class BottleNumber1(BottleNumber):
    @override
    def container(self) -> str:
        return "bottle"

    @override
    def pronoun(self) -> str:
        return "it"


class Bottles:
    def verse(self, verse_number: int) -> str:
        bottle_number = BottleNumber(verse_number)

        return (
            f"{bottle_number} of beer on the wall, ".capitalize()
            + f"{bottle_number} of beer.\n"
            + f"{bottle_number.action()}, "
            + f"{bottle_number.successor()} of beer on the wall.\n"
        )

    def verses(self, verse_start: int, verse_end: int) -> str:
        verse_indices = range(verse_start, verse_end - 1, -1)

        return "\n".join(self.verse(index) for index in verse_indices)

    def song(self) -> str:
        return self.verses(99, 0)
