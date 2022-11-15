# TODO решить с помощью list comprehension и распечатать его
from pprint import pprint

skolko = 15

# dict_bin = {i: bin(i) for i in range(skolko+1)}
# dict_dec = {i: i for i in range(skolko+1)}
# dict_hex = {i: hex(i) for i in range(skolko+1)}
# dict_oct = {i: oct(i) for i in range(skolko+1)}
#
# pprint([f'bin: {dict_bin[n]}, dec: {dict_dec[n]}, hex: {dict_hex[n]}, oct: {dict_oct[n]}' for n in range(skolko+1)])

pprint([{'bin': bin(i), 'dec': i, 'hex': hex(i), 'oct': oct(i)} for i in range(skolko+1)])

