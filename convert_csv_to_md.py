import csv

pokedex_data = []
with open("./pokedex.csv", "r", encoding="utf-8", errors="replace") as pokedex:
    """
    Converts the pokedex csv file to a markdown file
    """

    # Initializing reader
    reader = csv.reader(pokedex)

    # Creating header format for markdown table
    labels  = next(reader)
    temp = ['---' for label in labels]
    pokedex_data.append(f"|{'|'.join(labels)}|")
    pokedex_data.append(f"|{'|'.join(temp)}|")

    # Appending data with markdown code
    for row in reader:
        pokedex_data.append(f"|{'|'.join(row)}|")

    # Displaying all the data format
    for t in pokedex_data:
        print(t)

with open("./pokedex.md", "w", encoding="utf-8", errors="replace") as md:
    """
    Writing the markdown code in pokedex.md file
    """
    for t in pokedex_data:
        md.write(t + '\n')
