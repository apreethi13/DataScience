

def read_a_file():
    with open('../data/read.txt', 'r') as file:
        print(file.readline())


def write_to_file():
    with open('../data/write.txt', 'w') as file:
        file.write('Test write')


def main():
    # Read from a file
    read_a_file()

    # Write to a file
    write_to_file()


if __name__ == "__main__":
    main()

