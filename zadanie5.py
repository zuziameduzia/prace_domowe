rodzaj_kodowania = input("Które szyfrowanie chcesz wybrać?\n 1.GA-DE-RY-PO-LU-KI \n 2.PO-LI-TY-KA-RE-NU\n 3.własny szyfr\n Podaj cyfrę: ")
if rodzaj_kodowania == "3":
    kodowanie = input("Podaj rodzaj kodowania: ")
wiadomosc_do_zakod  = input("Podaj wiadomość do zakodowania: ")


def Merge(dict1, dict2):
    res = {**dict1, **dict2}
    return res

def czy_klucz_w_słowniku(test_dict, key):
    if key in test_dict.keys():
        return True
    else:
        return False

def szyfruj(wiadomosc_do_zakod):
    if rodzaj_kodowania == "1":
        dict1 = {
            'G':'A', 'D':'E', 'R':'Y', 'P':'O', 'L':'U', 'K':'I'
        }
        dict2 = {y: x for x, y in dict1.items()}

        full_dict = Merge(dict1, dict2)
        output = ""
        for i in range(len(wiadomosc_do_zakod)):
            if czy_klucz_w_słowniku(full_dict, wiadomosc_do_zakod[i].upper()) == True:
                output += full_dict[wiadomosc_do_zakod[i].upper()]
            else:
                output += wiadomosc_do_zakod[i].upper()
        return output
    elif rodzaj_kodowania == "2":
        dict3 = {
            'P':'O', 'L':'I', 'T':'Y', 'K':'A', 'R':'E', 'N':'U'
        }
        dict4 = {y: x for x, y in dict3.items()}

        full_dict2 = Merge(dict3, dict4)
        output = ""
        for i in range(len(wiadomosc_do_zakod)):
            if czy_klucz_w_słowniku(full_dict2, wiadomosc_do_zakod[i].upper()) == True:
                output += full_dict2[wiadomosc_do_zakod[i].upper()]
            else:
                output += wiadomosc_do_zakod[i].upper()
        return output
    elif rodzaj_kodowania == "3":
        kodowanie_bez_myslnika = str(kodowanie.replace("-", ""))
        for i in kodowanie_bez_myslnika:
            if kodowanie_bez_myslnika.count(i) >= 2:
                print("Błędne szyfrowanie")
                return False
            elif kodowanie_bez_myslnika.count(i) == None:
                continue
            else:
                continue

        dict_wlasny_kod = {}
        nowa_lista = []
        lista = kodowanie.split("-")
        for i in range(len(lista)):
            for j in range(len(lista[i])):
                nowa_lista.append(lista[i][j])

        for i in range(0, len(nowa_lista) - 1, 2):
            dict_wlasny_kod[nowa_lista[i]] = nowa_lista[i + 1]
            dict_wlasny_kod[nowa_lista[i + 1]] = nowa_lista[i]


        output = ""
        for i in range(len(wiadomosc_do_zakod)):
            if czy_klucz_w_słowniku(dict_wlasny_kod, wiadomosc_do_zakod[i].upper()) == True:
                output += dict_wlasny_kod[wiadomosc_do_zakod[i].upper()]
            else:
                output += wiadomosc_do_zakod[i].upper()
        return output









if rodzaj_kodowania == "1":
    print(szyfruj(wiadomosc_do_zakod))

elif rodzaj_kodowania == "2":
    print((szyfruj(wiadomosc_do_zakod)))


elif rodzaj_kodowania == "3":
    print(szyfruj(wiadomosc_do_zakod))