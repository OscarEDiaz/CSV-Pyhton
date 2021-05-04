import csv
with open('insurance.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    contador_male = 0
    contador_female = 0
    for row in spamreader:
        newList = (row[0].split(","))
        if newList[1] == "female":
            contador_female += 1
        elif newList[1] == "male":
            contador_male += 1

    print(contador_male)
    print(contador_female)
