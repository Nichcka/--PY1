import doctest
# TODO Написать 3 класса с документацией и аннотацией типов
class Number_of_cases:
    """
    Работа с количеством долгов
    """
    def __init__(self, numer_of_subjects: int, days_before_deadline: int, number_of_glycine_tablets: int ):
        """
        :param numer_of_subjects: количество предметов
        :param days_before_deadline: время до дедлайна
        :param number_of_glycine_tablets: сколько таблеток глицина осталось
        :return:
        """
        if not isinstance(numer_of_subjects, int):  # не тот тип вводится
            raise TypeError(f"Не тот тип количества долгов, надо int, а не {type(numer_of_subjects)}")
        self.numer_of_subjects = numer_of_subjects
        if not isinstance(days_before_deadline, (int, float)): # не тот тип вводится
            raise TypeError(f"Не тот тип количества дней до дедлайна, надо int, а не {type(days_before_deadline)}")
        self.days_before_deadline = days_before_deadline
        if not isinstance(number_of_glycine_tablets, (int, float)):  # не тот тип вводится
            raise TypeError(f"Не тот тип количества таблеток глицина, надо int, а не {type(number_of_glycine_tablets)}")
        self.number_of_glycine_tablets =  number_of_glycine_tablets

    def procrastination(self, numer_of_subjects: int) -> str:
        """
        когда стоит начинать
        :param numer_of_subjects:
        :return:
        """
        if self.numer_of_subjects >10:
            return "Лучше начать сейчас же"
        else:
            return "Можно подождать еще пару деньков"

    def energy(self, numer_of_subjects, days_before_deadline, number_of_glycine_tablets) -> str:
        """
        сколько покупать энергетиков, чтобы успеть сделать все
        :param numer_of_subjects:
        :param days_before_deadline:
        :param number_of_glycine_tablets:
        :return:
        """
        if self.number_of_glycine_tablets != 0:
            return f"надо купить {self.numer_of_subjects*self.days_before_deadline/(4*self.number_of_glycine_tablets)} энергетиков"

    def no_glycine (self) -> str:
        """
        Проверяем запасы глицина
        :return:
        """
        if self.number_of_glycine_tablets == None:
            return "иди в аптеку!"
        else:
            return "Живем живем"


class TV:
    def __init__(self, num_of_channels: int, hours_of_free_time: int):
        """
        Решение, что посмотреть по телевизору
        :param num_of_channels:
        :param hours_of_free_time:
        """
        if not isinstance(num_of_channels, int):  # не тот тип вводится
            raise TypeError(f"Не тот тип количества каналов, надо int, а не {type(num_of_channels)}")
        self.num_of_channels = num_of_channels
        if not isinstance(hours_of_free_time, int): # не тот тип вводится
            raise TypeError(f"Не тот тип количества свободного времени, надо int, а не {type(hours_of_free_time)}")
        self.hours_of_free_time = hours_of_free_time

    def time_to_choose(self) ->str:
        """
        В зависимости от количества свободного времени
        :return:
        """
        if self.hours_of_free_time >= 2:
            return "Посмотри 'Иллюзион+' или 'tv1000'"
        else:
            return "Посмотри 'Disney' или 'СТС'"

    def about_channels(self)->str:
        """
        Проверяем возможности телевизора
        :return:
        """
        if self.num_of_channels < 10:
            return "Подключи кабельное тв!"
        else:
            return "Наслаждайся жизнью"


class Performance:
    """
    Ставим перформанс, основанный на разных текстах
    """
    def __init__(self, num_of_texts: int, how_many_pages: float, amount_of_actors: int):
        if not isinstance(num_of_texts, int):  # не тот тип вводится
            raise TypeError(f"Не тот тип количества текстов, надо int, а не {type(num_of_texts)}")
        self.num_of_texts = num_of_texts
        if not isinstance(how_many_pages, float): # не тот тип вводится
            raise TypeError(f"Не тот тип количества страниц в тексте, надо float, а не {type(how_many_pages)}")
        self.how_many_pages = how_many_pages
        if not isinstance(amount_of_actors, int):  # не тот тип вводится
            raise TypeError(f"Не тот тип количества актеров, надо int, а не {type(amount_of_actors)}")
        self.amount_of_actors = amount_of_actors

    def showing(self)->str:
        """
        Расчитываем время показа
        :return:
        """
        return f"показ буедт длиться {self.num_of_texts*self.how_many_pages/6} часов"
    def space(self)->str:
        """
        Проверяем, хватит ли пространства на сцене для каждого актера
        :return:
        """
        self.space_of_actors = self.amount_of_actors * 1.8
        if self.space_of_actors >= 12:
            return "все не поместятся"
        else:
            return "можете начинать репетировать"


if __name__ == "__main__":
    doctest.testmod()
    nuber_of_cases = Number_of_cases(15, 3, 100)
    cosy_evening = TV(72, 1)
    theater = Performance(11, 0.5, 6)
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    pass
