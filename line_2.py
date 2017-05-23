from matplotlib import pyplot as plt
from matplotlib import rc
from nltk import FreqDist

rc('font', family='DejaVu Sans')

word = ['ojciec']

title1 = "lord-jim.txt"
title2 = "przedwiosnie.txt"
title3 = "sklepy-cynamonowe.txt"
title4 = "szewcy.txt"
title5 = "ziemia-obiecana-tom-pierwszy.txt"

def line_plot(data1, data2, data3, data4, data5, name):
    plt.title("Liczba wystąpień słów")
    plt.xlabel("Wyrazy")
    plt.ylabel("Liczba wystąpień")

    plt.xticks(range(6), name, rotation=90)
    plt.grid(linestyle='-.')
    plt.plot(range(6), data1, color='y', label="Lord Jim")
    plt.plot(range(6), data2, color='b', label="Przedwiośnie")
    plt.plot(range(6), data3, color='r', label="Sklepy cynamonowe")
    plt.plot(range(6), data4, color='m', label="Szewcy")
    plt.plot(range(6), data5, color='g', label="Ziemia obiecana Tom 1")

    plt.legend()
    plt.tight_layout()
    plt.show()

def count_freq(fname):
    with open(fname, encoding='utf8') as fp:
        split_words = fp.read().split()
        freq_dist = FreqDist(split_words)
    return freq_dist

def return_values(freq, word):
    result = []
    for s in word:
        result.append(freq[s] if s in freq else 0)
    return result


def color_lines(file1, file2, file3, file4, file5, word):
    freq1 = count_freq(file1)
    freq2 = count_freq(file2)
    freq3 = count_freq(file3)
    freq4 = count_freq(file4)
    freq5 = count_freq(file5)

    res1 = return_values(freq1, word)
    res2 = return_values(freq2, word)
    res3 = return_values(freq3, word)
    res4 = return_values(freq4, word)
    res5 = return_values(freq5, word)

    line_plot(res1, res2, res3, res4, res5, word)

color_lines(title1, title2, title3, title4, title5, word)
