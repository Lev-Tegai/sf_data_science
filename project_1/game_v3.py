"""Guess-Number Game.
Computer itself sets and guesses number
"""

import numpy as np
def random_predict(number: int = np.random.randint(1, 101)) -> int:
    """Guessing number at random
    Args:
        number (int, optional): Set number. Defaults to 1.
    Returns:
        int: Number of attempts
    """

    count = 0
    max_number = 100
    min_number = 0
    predict_number = np.random.randint(1, 101) # presumptive number

    while True:
        count += 1

        if predict_number > number:
            max_number = predict_number - 1
            predict_number = (max_number + min_number) // 2

        elif predict_number < number:
            min_number = predict_number + 1
            predict_number = (max_number + min_number) // 2

        else:
            break # end game, loop exit

    return count


def score_game(random_predict) -> int:
    """On average, how many attempts does our algorithm need to guess number, out of 1000 approaches
    Args:
        random_predict ([type]): guess function
    Returns:
        int: average number of attempts
    """

    count_ls = [] # list for saving number of attempts
    np.random.seed(1) # fix the seed for reproducibility
    random_array = np.random.randint(1, 101, size=(1000)) # set a list of numbers

    i = 0
    for number in random_array:
        i += 1
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls)) # find average number of attempts

    print(f'On average, your algorithm guesses number for: {score} attempts')
    return score


if __name__ == '__main__':
    score_game(random_predict)
