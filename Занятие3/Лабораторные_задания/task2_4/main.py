import json


def task():
    filename = "input.json"
    with open(filename, "r") as file: #  считать содержимое JSON файла
        json_data = json.load(file)

    gen_exr = (item["contains_improvement_appeals"] for item in json_data) #  записать выражение-генератор возвращающее значение по ключу contains_improvement_appeals
    return sum(gen_exr)


if __name__ == "__main__":
    print(task())
