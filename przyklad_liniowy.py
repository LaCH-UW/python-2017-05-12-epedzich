from matplotlib import pyplot as plt
from matplotlib import rc
from nltk import FreqDist

# ustawiamy czcionkę wspierającą unicode - w domyślnej są tylko znaki ASCII
rc('font', family='DejaVu Sans')

#words = ['Wokulski', 'Rzecki', 'subiekt', 'handel', 'sklep']
words = ['do', 'ma', 'jest', 'kot', 'zrobił']
title1 = 'lalka-tom-pierwszy.txt'
title2 = 'lalka-tom-drugi.txt'
title3 = "lord-jim.txt"
title4 = "przedwiosnie.txt"
title5 = "sklepy-cynamonowe.txt"
title6 = "szewcy.txt"
title7 = "ziemia-obiecana-tom-pierwszy.txt"

# def line_plot(data1, data2, names):
#     plt.title("Liczba wystąpień słów")
#     plt.xlabel("Próbki")
#     plt.ylabel("Liczba wystąpień")
#
#     plt.xticks(range(len(names)), names, rotation=90)
#     plt.grid()
#     plt.scatter(range(len(names)), data1, color='y', label="Wystąpienia słów w I tomie Lalki")
#     plt.scatter(range(len(names)), data2, color='b', label="Wystąpienia słów w II tomie Lalki")
#
#     plt.legend()   #generuje legende

def heatmap_plot(data, names):
    plt.title("Liczba wystąpień słów")
    plt.xlabel("Próbki")
    plt.ylabel("Liczba wystąpień")

    axis = range(len(names))
    plt.yticks([x + 0.5 for x in range(len(names))], ["Lord Jim", "Przedwiośnie", "Sklepy cynamonowe", "Szewcy", "Ziemia obiecana", "Tom I"])
    plt.xticks([x + 0.5 for x in axis], names, rotation=90)
    plt.pcolor(data)


    plt.tight_layout()
    plt.savefig('plot.png')
    plt.show()

def count_freq(fname):
    with open(fname, encoding='utf8') as fp:
        split_words = fp.read().split()
        freq_dist = FreqDist(split_words)
    return freq_dist

def return_values(freq, words):
    result = []
    for s in words:
        result.append(freq[s] if s in freq else 0)
    return result


def make_plot(file1, file2, file3, file4, file5, file6, file7, words):
    freq1 = count_freq(file1)
    freq2 = count_freq(file2)
    freq3 = count_freq(file3)
    freq4 = count_freq(file4)
    freq5 = count_freq(file5)
    freq6 = count_freq(file6)
    freq7 = count_freq(file7)

    val1 = []
    val1.append(return_values(freq1, words))
    val1.append(return_values(freq2, words))
    val1.append(return_values(freq3, words))
    val1.append(return_values(freq4, words))
    val1.append(return_values(freq5, words))
    val1.append(return_values(freq6, words))
    val1.append(return_values(freq7, words))

    heatmap_plot(val1, words)

    res1 = return_values(freq1, words)
    res2 = return_values(freq2, words)

    # line_plot(res1, res2, words)

make_plot(title1, title2, title3, title4, title5, title6, title7, words)

# teraz dopisz kod tworzący wykres punktowy zawierający liczbę wystąpień słów z listy
# z punktami różnych kolorów dla pierwszego i drugiego tomu "Lalki"
# dostosuj legendę itp.

# podpowiedź: funkcję plt.plot(y) zastępuje funkcja plt.scatter(x, y)

