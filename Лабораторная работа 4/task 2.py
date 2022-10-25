def delete(list_, index=None):
    if index is not None:
        left_part = list_[:index]
        right_part = list_[index+1:]
        return left_part + right_part
    else:
        last_el = list_[:-1]
        return  last_el



print(delete([0, 0, 1, 2], index=0))  # [0, 1]
print(delete([0, 1, 1, 2, 3], index=1))  # [0, 1, 2]
print(delete([0, 1, 2, 3, 4, 4]))  # [0, 1, 2, 3]
