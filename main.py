import random
import data_to_csv


def get_acronym(string, acronym, fmt):
    with open(string) as word_file:
        lines = word_file.readlines()

    # for i in range(max([len(line) for line in lines])):
    i = 22
    words = data_to_csv.get_words(acronym, fmt, lines, i)
    try:
        for j in range(len(fmt)):
            print(words[j][int(random.randrange(len(words[j])))], end=' ')
    except IndexError as e:
        print(e)

    comb = get_combinations(words)
    print(f'\nComb: {i:2.0f}: {comb}')


def get_combinations(words):
    combinations = len(words[0])
    for i in range(1, len(words)):
        combinations *= len(words[i])

    return combinations


if __name__ == "__main__":
    acronym = 'saturn'
    fmt = 'aanvan'

    get_acronym('./words', acronym, fmt)
