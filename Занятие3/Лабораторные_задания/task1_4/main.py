INPUT_FILE = "input.txt"
OUTPUT_FILE = "output.txt"


def task():
    with open(INPUT_FILE) as f1: #  перезаписать содержимое одного файла в другой
        with open(OUTPUT_FILE, "w") as f2:
            for upper_line in map(str.upper, f1):
                f2.write(upper_line)


if __name__ == "__main__":
    task()

    with open(OUTPUT_FILE) as file:
        for line in file:
            print(line, end="")
