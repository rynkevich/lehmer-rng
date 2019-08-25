import itertools

TEST_SEQUENCE_SIZE = 5000000


def indirect_uniformity_analysis(values):
    k = sum(x1 ** 2 + x2 ** 2 < 1 for x1, x2 in zip(values[::2], values[1::2]))
    return 2 * k / len(values)


def period(rng):
    first_run = tuple(rng(TEST_SEQUENCE_SIZE))
    start = None
    for i, x in enumerate(rng(TEST_SEQUENCE_SIZE)):
        if x == first_run[-1] and x == first_run[i]:
            if start is None:
                start = i
            else:
                return i - start
    return None


def aperiodicity_interval_length(rng, period_value):
    iterator, shifted_iterator = itertools.tee(rng(TEST_SEQUENCE_SIZE))
    shifted_iterator = itertools.islice(shifted_iterator, period_value)
    for i, (x, x_shifted) in enumerate(zip(iterator, shifted_iterator)):
        if x == x_shifted:
            return i + period_value
    return None
