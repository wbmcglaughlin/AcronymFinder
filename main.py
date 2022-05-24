import random
import nltk


def get_acronym(string, acronym, fmt):
    with open(string) as word_file:
        lines = word_file.readlines()

    # for i in range(max([len(line) for line in lines])):
    i = 22
    words = get_words(acronym, fmt, lines, i)
    try:
        for j in range(len(fmt)):
            print(words[j][int(random.randrange(len(words[j])))], end=' ')
    except IndexError as e:
        print(e)

    comb = get_combinations(words)
    print(f'\nComb: {i:2.0f}: {comb}')


def get_words(acronym, fmt, lines, max_len):
    words = [[] for _ in range(len(fmt))]
    for line in lines:
        line = line.rstrip('\n')
        if line[0] in acronym:
            if len(line) < max_len:
                ind = acronym.index(line[0])
                try:
                    if fmt[ind] in wn.synsets(line)[0].pos():
                        words[ind].append(line)
                except IndexError as e:
                    pass

    return words


def get_combinations(words):
    combinations = len(words[0])
    for i in range(1, len(words)):
        combinations *= len(words[i])

    return combinations


if __name__ == "__main__":
    try:
        nltk.data.find('wordnet')
    except LookupError as e:
        nltk.download('wordnet')

    from nltk.corpus import wordnet as wn

    acronym = 'saturn'
    fmt = 'aanvan'

    get_acronym('./words', acronym, fmt)
