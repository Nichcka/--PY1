import random
import string


def get_random_password(n: int) -> str:
    full_list = string.ascii_lowercase + string.ascii_uppercase + string.digits
    your_password = ''.join(random.sample(full_list, n))
    return your_password



print(get_random_password(8))
