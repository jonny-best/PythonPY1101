from string import ascii_lowercase, ascii_uppercase, digits
import random

k = 8
population = ascii_lowercase + ascii_uppercase + digits
my_password = random.sample(population, k)

if __name__ == "__main__":
    print(ascii_lowercase)
    print(ascii_uppercase)
    print(digits)
    print(my_password)
