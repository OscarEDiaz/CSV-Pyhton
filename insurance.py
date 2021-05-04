import csv # Libreria para leer archivos de CSV /Comma Separated Values/
with open('insurance.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    contador_male = 0
    contador_female = 0
    for row in reader: # row va tomando un valor de lista por cada que avanza en reader, el cual es una lista grande de listas.
        newList = (row[0].split(",")) # Dado que row es solo una lista con un solo string, solo tiene posicion 0
        if newList[1] == "female":
            contador_female += 1
        elif newList[1] == "male":
            contador_male += 1

    print(contador_male)
    print(contador_female)
