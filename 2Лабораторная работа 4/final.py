class McDonald:
    """Базовый класс МакДоналдс"""
    def __init__(self, menu: dict, waiters: int, terminals: int):
        """скрываем количество официантов и терминалов, как базовые характеристики обслуживания посетителей"""
        if not isinstance(menu, dict):
            raise TypeError(f"Неправильный тип ввода, надо dict, а не {type(menu)}")
        self.menu = menu
        self._waiters = waiters
        self._terminals = terminals

    @property
    def waiters(self) -> int:
        """Возвращает количество официантов."""
        return self._waiters

    @waiters.setter
    def waiters(self, new_waiters: int):
        """Устанавливает количество официантов."""
        if not isinstance(new_waiters, int):
            raise TypeError(f"Неправильный тип ввода, надо int, а не {type(new_waiters)} ")
        self._waiters = new_waiters

    @property
    def terminals(self) -> int:
        """Возвращает количество терминалов."""
        return self._terminals

    @terminals.setter
    def terminals(self, new_terminals: int):
        """Устанавливает количество терминалов."""
        if not isinstance(new_terminals, int):
            raise TypeError(f"Неправильный тип ввода, надо int, а не {type(new_terminals)} ")
        self._terminals = new_terminals

    def __str__(self) -> str:
        return f'({self.__class__.__name__})Количество работающих официантов: {self._waiters}, терминалов: {self._terminals}. Меню ресторана:{self.menu}. '

    def __repr__(self) -> str:
        return f"({self.__class__.__name__})Официанты: {self._waiters!r}, терминалы: {self._terminals!r}, меню:{self.menu!r} ."


    def food_for_children(self, menu: dict):
        try:
            menu['HappyMill']
        except:
            KeyError(f'Пусть дети едят, что есть')



class TastyAndPoint(McDonald):
    """Дочерний класс 'Вкусно и точка'"""
    def __init__(self, menu: dict, waiters: int, terminals: int, logo: str):
        super().__init__(menu, waiters, terminals)
        self.logo = logo

    @property
    def logo(self) -> str:
        """Возвращает логотип."""
        return self._logo

    @logo.setter
    def logo(self, new_logo: str) -> None:
        """Устанавливает логотип"""
        if not isinstance(new_logo, str):  # не тот тип вводится
            raise TypeError(f"Не тот тип ввода количества страниц, надо str, а не {type(new_logo)}")
        self._logo = new_logo

    def __str__(self) -> str:
        return f'Логотип организации "{self.logo}".'

    def __repr__(self) -> str:
        return f'TastyAndPoint(Логотип = "{self.logo!r}")'


    def food_for_children(self, menu: dict):
        return KeyError(f"Еду для детей не поставляем")





actual_menu = {'Напитки': 'Американо',
                    'Снеки':'Сырные палочки',
                    'Бургеры':'ЧикенБургер'}

if __name__ == "__main__":
    mac = McDonald(actual_menu, 25, 10)
    new_stuff = TastyAndPoint(actual_menu, 25, 10, "Вкусно и точка")
    pass

