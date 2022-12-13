import math as m

def pairwise(iterable):
    for i in range(len(iterable) - 1):
        yield iterable[i], iterable[i+1]

def get_len(pair1, pair2):
    return m.sqrt((pair2[0] - pair1[0]) ** 2 + (pair2[1] - pair1[1]) ** 2)

if __name__ == "__main__":
    pts = [
        (3, 4),
        (4.5, 3),
        (2.1, -1),
        (6.8, -3),
        (1.4, 2.9)
    ]

    #gen1 = pairwise(pts)
    #gen2 = pairwise(pts).send(None)
    print(sum(map(get_len, pts, pts[1:])))
