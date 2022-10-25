def get_count_char(str_):
    letter_dict = {}
    new_str = str_.lower()
    for letter_ in new_str:
        if letter_.isalpha():

            if letter_ in letter_dict:
                letter_dict[letter_] += 1
            else:
                letter_dict[letter_] = 1
    return letter_dict

def matematika(dict_):
    SUMMA = sum(dict_.values())
    for each_ in dict_:
        dict_[each_] = round(dict_[each_] * 100 / SUMMA, 3)
    return dict_





main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
print(get_count_char(main_str))
print(matematika(get_count_char(main_str)))