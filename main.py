import statistics as stat
import math
import matplotlib.pyplot as plt

from analysis import indirect_uniformity_analysis, period, aperiodicity_interval_length
from rng import random_sequence
from reader import read_positive_integer_from_keyboard

RANDOM_SEQUENCE_SIZE = 50000
HISTOGRAM_BINS_COUNT = 20

# For a = 0, b = 1
UNIFORM_DISTRIBUTION_EXPECTED = 0.5  # 0.5 * (a + b)
UNIFORM_DISTRIBUTION_VARIANCE = 1 / 12  # 1 / 12 * (a + b) ^ 2
UNIFORM_DISTRIBUTION_STANDARD_DEVIATION = math.sqrt(UNIFORM_DISTRIBUTION_VARIANCE)  # σ = √D
REFERENCE_UNIFORMITY_EVALUATION = math.pi / 4


def main():
    a = read_positive_integer_from_keyboard('a')
    m = read_positive_integer_from_keyboard('m', lambda x: x > a, 'm must be a positive integer, greater than a')
    r_0 = read_positive_integer_from_keyboard('R0')

    rng = lambda size: random_sequence(a, m, r_0, size)
    generated_sequence = tuple(rng(RANDOM_SEQUENCE_SIZE))

    expected = stat.mean(generated_sequence)
    variance = stat.variance(generated_sequence)
    standard_deviation = stat.stdev(generated_sequence)
    uniformity_evaluation = indirect_uniformity_analysis(generated_sequence)
    generator_period = period(rng)
    generator_aperiodicity_interval_length = \
        aperiodicity_interval_length(rng, generator_period) if generator_period is not None else None

    show_difference('Expected', expected, UNIFORM_DISTRIBUTION_EXPECTED)
    show_difference('Variance', variance, UNIFORM_DISTRIBUTION_VARIANCE)
    show_difference('Standard Deviation', standard_deviation, UNIFORM_DISTRIBUTION_STANDARD_DEVIATION)
    show_difference('Uniformity Evaluation (2K/N)', uniformity_evaluation, REFERENCE_UNIFORMITY_EVALUATION)
    print(f'Period: {generator_period}')
    print(f'Aperiodicity Interval Length: {generator_aperiodicity_interval_length}')

    plot_freqency_histogram(generated_sequence)
    plt.show()


def show_difference(name, actual_value, reference_value):
    print(f'{name}: {actual_value:.5f} '
          f'(reference = {reference_value:.5f}, '
          f'Δ = {abs(reference_value - actual_value):.5f})')


def plot_freqency_histogram(sequence):
    fig, ax = plt.subplots()
    fig.canvas.set_window_title('Lehmer Random Number Generator')
    fig.suptitle('RNG Frequency Histogram')
    ax.set_xlabel('Generated value')
    ax.set_ylabel('Frequency')
    ax.hist(sequence, bins=HISTOGRAM_BINS_COUNT, weights=([1 / RANDOM_SEQUENCE_SIZE] * RANDOM_SEQUENCE_SIZE))


if __name__ == '__main__':
    main()
