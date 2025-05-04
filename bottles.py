class Bottles:
    def container(self, number: int) -> str:
        if number == 1:
            return "bottle"
        return "bottles"

    def verse(self, verse_number: int) -> str:
        match verse_number:
            case 0:
                return (
                    "No more bottles of beer on the wall, "
                    "no more bottles of beer.\n"
                    "Go to the store and buy some more, "
                    "99 bottles of beer on the wall.\n"
                )
            case 1:
                return (
                    "1 bottle of beer on the wall, "
                    "1 bottle of beer.\n"
                    "Take it down and pass it around, "
                    "no more bottles of beer on the wall.\n"
                )
            case _:
                return (
                    f"{verse_number} bottles of beer on the wall, "
                    f"{verse_number} bottles of beer.\n"
                    "Take one down and pass it around, "
                    f"{verse_number - 1} {self.container(verse_number - 1)} of beer on the wall.\n"
                )

    def verses(self, verse_start: int, verse_end: int) -> str:
        verse_indices = range(verse_start, verse_end - 1, -1)

        return "\n".join(self.verse(index) for index in verse_indices)

    def song(self) -> str:
        return self.verses(99, 0)
