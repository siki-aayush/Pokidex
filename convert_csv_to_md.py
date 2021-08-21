import csv

pokedex_data = []
with open("./pokedex.csv", "r", encoding="utf-8", errors="replace") as pokedex:
    reader = csv.reader(pokedex)
    labels  = next(reader)
    temp = ['---' for label in labels]
    pokedex_data.append(f"|{'|'.join(labels)}|")
    pokedex_data.append(f"|{'|'.join(temp)}|")

    for row in reader:
        print("row", row)
        pokedex_data.append(f"|{'|'.join(row)}|")

    [print(t) for t in pokedex_data] 

with open("./pokedex.md", "w", encoding="utf-8", errors="replace") as md:
    for t in pokedex_data:
        md.write(t + '\n')
