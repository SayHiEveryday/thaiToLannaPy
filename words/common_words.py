import csv, os

common_words = {}

with open(os.path.join(os.path.dirname(__file__),"common_words.csv"), 'r', encoding='utf-8-sig', newline='') as file:
    reader = csv.reader(file)
    header = list(next(reader))

    for item in reader:
        common_words[item[0]] = item[1]

