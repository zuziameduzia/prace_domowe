import statistics


def mean (data):
    lista_srednich = []
    for i in range(len(data)):
        lista_srednich.append(statistics.mean(data[i]))

    return lista_srednich

def median (data):
    lista_median = []
    for i in range(len(data)):
        lista_median.append(statistics.median(data[i]))

    return lista_median

def std(data):
    lista_std = []
    for i in range(len(data)):
        lista_std.append(statistics.stdev(data[i]))

    return lista_std
