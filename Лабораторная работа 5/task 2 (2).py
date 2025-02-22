import random

def get_unique_list_numbers(list_size, min_num, max_num) -> list[int]:

      list_num = random.sample(range(min_num, max_num), list_size)
      return list_num


list_unique_numbers = get_unique_list_numbers(15, -10, 10)
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
