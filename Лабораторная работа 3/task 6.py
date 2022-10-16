list_numbers = [2, -93, -2, 8, -36, -44, -1, -85, -14,
                90, -22, -90, -100, -8, 38, -92, -45,
                67, 53, 25]

# TODO Оформить решение
max_i = 0
max_num = list_numbers[max_i]
#max_num = list_numbers[0]

for current_i, current_num in enumerate(list_numbers) :
    max_num = list_numbers [max_i]
    if current_num > max_num:
        max_i = current_i
        max_num = current_num
#print(max_i)
list_numbers[-1],list_numbers [max_i]= list_numbers [max_i], list_numbers[-1]
print(list_numbers)
