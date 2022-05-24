def read_file(string):
    with open(string) as word_file:
        lines = word_file.readlines()

    print(lines)


if __name__ == "__main__":
    read_file('./words')
