import random


def get_acronym(string, acronym, fmt, max_word_length=23):
    with open(string) as word_file:
        lines = word_file.readlines()

    words = get_words(acronym, fmt, lines, max_word_length)

    try:
        for j in range(len(fmt)):
            print(words[j][int(random.randrange(len(words[j])))], end=' ')
    except IndexError as e:
        print(e)

    comb = get_combinations(words)
    print(f'\n\nNumber of other Acronym Combinations! {comb - 1}')


def get_words(acronym, fmt, lines, max_len):
    words = [[] for _ in range(len(fmt))]
    for line in lines:
        line = line.split(',')
        line[1] = line[1].rstrip('\n')
        if line[0][0] in acronym:
            if len(line[0]) < max_len:
                # ind = acronym.index(line[0][0])
                indexes = find(acronym, line[0][0])
                for ind in indexes:
                    try:
                        if fmt[ind] in line[1]:
                            words[ind].append(line[0])
                    except IndexError as e:
                        print(e)

    return words


def find(s, ch):
    return [i for i, ltr in enumerate(s) if ltr == ch]


def get_combinations(valid_array):
    # Returns the number of combinations for a format and acronym
    combinations = len(valid_array[0])
    for i in range(1, len(valid_array)):
        combinations *= len(valid_array[i])

    return combinations


if __name__ == "__main__":
    userAcronym = 'will'
    userFmt = 'aann'

    get_acronym('./data.csv', userAcronym, userFmt)
