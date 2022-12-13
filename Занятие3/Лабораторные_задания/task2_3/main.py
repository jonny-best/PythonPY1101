import json


def task():
    filename = "input.json"
    with open(filename, "r") as file: #  считать содержимое JSON файла
        json_data = json.load(file)

    return max(json_data, key= lambda item: item["score"])  #  найти максимальный элемент по ключу score


if __name__ == "__main__":
    print(task())
