'''
Created on 03.06.2019

@author: Oskar Kowalczyk

'''


def calculate(usb_size, memes):
    """
    Function calculates the best set of memes,
    function is based on knapsack problem with dynamic solution

    - **parameters**, **types**, **return** and **return types**::
        :param usb_size: - a number describing the capacity of the USB stick in GiB
        :param memes:  a list of 3-element tuples, each with the name,
                       size in MiB, and price in caps of a meme:
        :type usb_size: int
        :type memes: list
        :return: a 2-element tuple, value of memes on pendrive and
                  a set containing names of memes saved on the pendrive
        :rtype: tuple
    """
    # Input type and value checking.
    check_inputs(usb_size, memes)

    # Amount of meme in memes list.
    n = len(memes)
    # Usb size in MiB.
    usb_size = usb_size * 1024
    # Matrix for dynamic programming.
    K = [[0 for _ in range(usb_size + 1)] for _ in range(n + 1)]

    # Sorting list of memes by value.
    memes.sort(key=lambda x: int(x[2]))
    weights = []
    values = []
    # Creating separate lists for weight and value.
    for meme in memes:
        weights.append(meme[1])
        values.append(meme[2])

    # Calculating which items to take using matrix.
    for i in range(n + 1):
        for w in range(usb_size + 1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif weights[i - 1] <= w:
                K[i][w] = max(values[i - 1] + K[i - 1][w - weights[i - 1]], K[i - 1][w])
            else:
                K[i][w] = K[i - 1][w]
    # Stores the result of matrix.
    result = K[n][usb_size]

    w = usb_size
    final_set_names = set()
    final_set_value = 0

    # Creating return for function by finding names of chosen items and adding their values.
    for i in range(n, 0, -1):
        if result <= 0:
            break

        # If result is equal to K[i - 1][w], it means item is not included.
        if result == K[i - 1][w]:
            continue
        else:
            final_set_names.add(memes[i-1][0])
            final_set_value += memes[i-1][2]

            # After we collect name and value we exclude the item.
            result = result - values[i - 1]
            w = w - weights[i - 1]
    final_set = (final_set_value, final_set_names)
    print(final_set)


def check_inputs(usb_size, memes):
    assert(isinstance(usb_size, int))
    assert(isinstance(memes, list))
    assert(all(isinstance(meme, tuple) for meme in memes))
    assert(all(isinstance(meme[0], str) for meme in memes))
    assert(all(isinstance(meme[1], int) for meme in memes))
    assert(all(meme[1] >= 0 for meme in memes))
    assert(all(isinstance(meme[2], int) for meme in memes))
    assert(all(meme[2] >= 0 for meme in memes))
    assert(usb_size > 0)


if __name__ == '__main__':
    usb_size = 1
    memes = [
        ('rollsafe.jpg', 205, 6),
        ('sad_pepe_compilation.gif', 410, 10),
        ('yodeling_kid.avi', 605, 12)
    ]

    calculate(usb_size, memes)


