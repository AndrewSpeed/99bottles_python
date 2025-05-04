class Bottles:
    def container(self, number: int) -> str:
        if number == 1:
            return "bottle"
        return "bottles"

    def pronoun(self, number: int) -> str:
        if number == 1:
            return "it"
        return "one"

    def successor(self, number: int) -> int:
        if number == 0:
            return 99
        return number - 1

    def quantity(self, number: int) -> str:
        if number == 0:
            return "no more"
        return str(number)

    def action(self, number: int) -> str:
        if number == 0:
            return "Go to the store and buy some more"
        return f"Take {self.pronoun(number)} down and pass it around"

    def verse(self, verse_number: int) -> str:
        return (
            f"{self.quantity(verse_number).capitalize()} {self.container(verse_number)} of beer on the wall, "
            f"{self.quantity(verse_number)} {self.container(verse_number)} of beer.\n"
            f"{self.action(verse_number)}, "
            f"{self.quantity(self.successor(verse_number))} {self.container(self.successor(verse_number))} of beer on the wall.\n"
        )

    def verses(self, verse_start: int, verse_end: int) -> str:
        verse_indices = range(verse_start, verse_end - 1, -1)

        return "\n".join(self.verse(index) for index in verse_indices)

    def song(self) -> str:
        return self.verses(99, 0)
