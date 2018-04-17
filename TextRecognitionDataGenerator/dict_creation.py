from random import randint
import shutil
import os

dict_name = "test.txt"
output_file = os.path.join("dicts", dict_name)
# base_file = "de.txt"
base_file = None
if not base_file:
    N_words = 10
N_char_min = 3
N_char_max = 10

letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
numbers = "0123456789"
symbols = ".,-+:*%"  # '/' is missing, because it doesnt work with filename

chars = numbers + symbols
len_chars = len(chars)

with open(output_file, 'w') as f:
    if base_file:
        with open(base_file, 'r') as b:
            line_count = 0
            for line in b:
                f.write(line.upper())
                f.write(line.capitalize())
                line_count += 1
            N_words = line_count
    for i in range(N_words):
        buffer = ""
        word_length = randint(N_char_min, N_char_max)
        for j in range(word_length):
            r = randint(1, len_chars) - 1
            buffer += (chars[r])
        buffer += "\n"
        f.write(buffer)
