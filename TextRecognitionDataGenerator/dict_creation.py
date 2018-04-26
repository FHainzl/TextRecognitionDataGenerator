from random import randint
import os


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


def get_char_pool(char_pool_arg):
    char_pool = ''
    if "let" in char_pool_arg:
        char_pool += "abcdefghijklmnopqrstuvwxyz"
    if "num" in char_pool_arg:
        char_pool += "0123456789"
    if "sym" in char_pool_arg:
        char_pool += ".,-+:*%/"

    return char_pool


def write_random_dict(char_pool_arg, n_char_min, n_char_max, n_new_words=None, new_dict=None, base_dict=None):
    """
    Writes a ned dictionary in dict/ that is then used by 'run.py -l mydict.txt' to generate images
    :param char_pool_arg: String including any combination of "let","num","sym" to include letters, numbers, symbols
    :param n_char_min: Minimum word length
    :param n_char_max: Maximum word length
    :param n_new_words: New words to be created
    :param new_dict: Name of .txt-File containing new dictionary to be created
    :param base_dict: Name of .txt-File on which to base new dict
    """


    if not new_dict:
        new_dict = char_pool_arg + '.txt'
    output_file = os.path.join("dicts", new_dict)

    char_pool = get_char_pool(char_pool_arg)
    if not base_dict and not n_new_words:
        # If n_new_words == None, but base_file != None: as many new words as words in base_file will be created
        raise ValueError("Specify either base_file or n_new_words")

    with open(output_file, 'w') as f:
        # If base_file is specified, add those words to output_file first
        if base_dict:
            input_file = os.path.join("dicts", base_dict)
            with open(input_file, 'r') as b:
                line_count = 0
                for line in b:
                    # Capitalize with frequency 1/cap_chance
                    cap_chance = 3
                    if randint(0, cap_chance - 1):
                        f.write(line.capitalize())
                    else:
                        f.write(line.upper())
                    line_count += 1

                # Create as many new words as existing words
                if not n_new_words:
                    n_new_words = line_count

        # Create new random words from string "chars"
        for i in range(int(n_new_words)):
            word_length = randint(n_char_min, n_char_max)
            word = rand_word(char_pool, word_length)
            f.write(word + '\n')


if __name__ == '__main__':
    write_random_dict("letnumsym", 2, 10, 1e5)
