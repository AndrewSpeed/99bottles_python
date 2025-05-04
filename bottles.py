class BottleNumber:
    _number: int

    def __init__(self, number: int):
        self._number = number

    def container(self) -> str:
        if self._number == 1:
            return "bottle"
        return "bottles"

    def pronoun(self) -> str:
        if self._number == 1:
            return "it"
        return "one"

    def successor(self) -> int:
        if self._number == 0:
            return 99
        return self._number - 1

    def quantity(self) -> str:
        if self._number == 0:
            return "no more"
        return str(self._number)

    def action(self) -> str:
        if self._number == 0:
            return "Go to the store and buy some more"
        return f"Take {self.pronoun()} down and pass it around"


class Bottles:
    def verse(self, verse_number: int) -> str:
        bottle_number = BottleNumber(verse_number)
        next_bottle_number = BottleNumber(bottle_number.successor())

        return (
            f"{bottle_number.quantity().capitalize()} {bottle_number.container()} of beer on the wall, "
            f"{bottle_number.quantity()} {bottle_number.container()} of beer.\n"
            f"{bottle_number.action()}, "
            f"{next_bottle_number.quantity()} {next_bottle_number.container()} of beer on the wall.\n"
        )

    def verses(self, verse_start: int, verse_end: int) -> str:
        verse_indices = range(verse_start, verse_end - 1, -1)

        return "\n".join(self.verse(index) for index in verse_indices)

    def song(self) -> str:
        return self.verses(99, 0)
