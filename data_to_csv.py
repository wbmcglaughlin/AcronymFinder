import nltk
import csv


def data_to_csv(word_file_path):
    with open(word_file_path) as word_file:
        lines = word_file.readlines()

    lines_no_new_line = [line.rstrip('\n') for line in lines]

    print(len(lines_no_new_line))

    word_type_result = []

    for line in lines_no_new_line:
        try:
            word_type_result.append(wn.synsets(line)[0].pos())
        except IndexError as e:
            word_type_result.append('')

    with open("./data.csv", "w+") as data_csv:
        csv_writer = csv.writer(data_csv)
        csv_writer.writerow(['word', 'type'])
        for i in range(len(lines_no_new_line)):
            csv_writer.writerow([lines_no_new_line[i], word_type_result[i]])


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


if __name__ == "__main__":
    # try:
    #     nltk.data.find('all-corpora')
    # except LookupError as e:
    #     nltk.download('all-corpora')

    from nltk.corpus import wordnet as wn

    data_to_csv("words")