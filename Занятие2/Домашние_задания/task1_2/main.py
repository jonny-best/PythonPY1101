def flatten(list_of_lists: list):
    for inside_list in list_of_lists:
        for value in inside_list: # yield from inside_list (эта конструкция заменяет строки 3 и 4)
            yield value


if __name__ == "__main__":
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    for ceil in flatten(matrix):
        print(ceil)
