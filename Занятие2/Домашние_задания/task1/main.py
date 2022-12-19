def count(start_number):
    while True:
        yield start_number
        start_number += 1


if __name__ == "__main__":
    # Write your solution here
    my_count = count(1)
    for _ in range(10):
        print(next(my_count))
