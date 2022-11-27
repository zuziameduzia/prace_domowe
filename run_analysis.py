from iris_analysis.calculate import median, mean, std
from iris_analysis.io import load, save


def main():
    results = []
    print("Podaj ścieżkę do pliku csv: ")
    input_file = input()
    print("Podaj ścieżkę, gdzie chcesz, aby plik został zapisany: ")
    result_file = input()
    data = load.zaladuj(input_file)
    result = []
    result.append(median(data))
    result.append(mean(data))
    result.append(std(data))
    results = [[row[i] for row in result] for i in range(len(result[0]))]
    save.save_result(results, result_file)

if __name__ == '__main__':
    main()


