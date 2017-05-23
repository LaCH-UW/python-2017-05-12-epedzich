from nltk import FreqDist
from matplotlib import pyplot as plt
from matplotlib import rc

rc('font', family='DejaVu Sans')

words = ['dom', 'Rzecki', 'subiekt', 'handel', 'sklep']
title1 = 'lalka-tom-pierwszy.txt'
title2 = 'lalka-tom-drugi.txt'

plt.xlabel("Słowa")
plt.ylabel("Liczba wystąpień")

def scatter_plot(x, y, words):

    plt.title("Liczba wystąpień słów w Lalce - porównanie tomów")

    axis = range(len(words))
    plt.xticks(x, words)
    plt.yticks(x, rotation=90)

    plt.bar([x + 50 for x in axis], y, width= 3, color='b', label='Lalka 1', align='center')
    plt.bar(x, y, width=3, color='r', label='Lalka 2', align='center')

    plt.grid()
    plt.autoscale()
    plt.legend()
    plt.tight_layout()

    plt.show()


def count_freq_and_len(fname):
    with open(fname, encoding='utf8') as fp:
        split_words = fp.read().split()
        freq_dist = FreqDist(split_words)
    return freq_dist, len(split_words)


def return_values(freq, words):
    result = []
    for s in words:
        result.append(freq[s] if s in freq else 0)
    return result


def make_plot(file1, file2, words):
    freq1, len1 = count_freq_and_len(file1)
    freq2, len2 = count_freq_and_len(file2)

    res1 = return_values(freq1, words)
    res2 = return_values(freq2, words)

    scatter_plot(res1, res2, words)


make_plot(title1, title2, words)
