def interpret_flashcards_csv():
    import csv
    flashcards = []
    with open('flashcards.csv', 'r') as flashcards_csv:
        flashcards_reader = csv.DictReader(flashcards_csv)
        for card in flashcards_reader:
            flashcards.append({"term":card['term'], "definition":card['definition'], "level":int(card['level'])})
    return flashcards

def update_flashcards_csv(flashcards):
    import csv
    with open('flashcards.csv', 'w', newline='') as csvfile:
        fieldnames = ['term', 'definition', 'level']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for row in flashcards:
            writer.writerow(row)