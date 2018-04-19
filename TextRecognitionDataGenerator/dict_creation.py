from random import randint
import shutil
import os

dict_name = "letnumsym.txt"
output_file = os.path.join("dicts", dict_name)
# base_file = "de.txt"
base_file = None
if not base_file:
    N_words = 100000
N_char_min = 2
N_char_max = 8

letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
numbers = "0123456789"
symbols = ".,-+:*%/"

chars = letters + numbers + symbols

def rand_word(characters, word_length):
    """
    Create random words with given length from pool of characters
    :param characters: string with pool of chars from which to sample 
    :param word_length: int with length of word to be returned
    :return: string with random word
    """
    word = ''
    for _ in range(word_length):
        r = randint(1, len(characters)) - 1
        word += (characters[r])
    return word



with open(output_file, 'w') as f:
    # If base_file is specified, add those words to output_file first
    if base_file:
        with open(base_file, 'r') as b:
            line_count = 0
            for line in b:
                f.write(line.upper())
                f.write(line.capitalize())
                line_count += 1
            # Create as many new words as existing words
            N_words = line_count
    # Create new random words from string "chars"
    for i in range(N_words):
        word_length = randint(N_char_min, N_char_max)
        word = rand_word(chars,word_length)
        f.write(word+'\n')
