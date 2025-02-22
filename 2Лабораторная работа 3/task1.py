class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    @property
    def name(self) -> str:
        return self._name

    @property
    def author(self) -> str:
        return self._author

    def __str__(self) -> str:
        return f'{self.__class__.__name__}(Книга: "{self._name}". Автор: {self._author})'

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r})"


class PaperBook(Book):
    """Версия бумажной книги"""
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name= name, author=author)
        if not isinstance(pages, int):  # не тот тип вводится
            raise TypeError(f"Не тот тип ввода количества страниц, надо int, а не {type(pages)}")
        self._pages = pages

    @property
    def pages(self) -> int:
        return self._pages

    @pages.setter
    def pages(self, pages: int):
        self._pages = pages

    def __str__(self) -> str:
        return f'Количество страниц в книге {self._pages}.'

    def __repr__(self) -> str:
        return f"PaperBook( value = {self._pages!r})"



class AudioBook(Book):
    """Версия аудиокниги"""
    def __init__(self,name: str, author: str, duration: (int, float)):
        super().__init__(name= name, author=author)
        if not isinstance(duration, (int, float)):  # не тот тип вводится
            raise TypeError(f"Не тот тип ввода продолжительности книги, надо float или int, а не {type(duration)}")
        self._duration = duration

    @property
    def duration(self) -> float:
        return self._duration

    @duration.setter
    def duration(self, duration: float):
        self._duration = duration


    def __str__(self) -> str:
        return f'Продолжительность аудиокниги {self._duration} часов.'

    def __repr__(self) -> str:
        return f"AudioBook(duration = {self._duration!r})"



example = AudioBook("Идиот", "Ф.М.Достоевский", 88.5)
print(example)

example2 = PaperBook("Идиот", "Ф.М.Достоевский", 754)
print(example2)