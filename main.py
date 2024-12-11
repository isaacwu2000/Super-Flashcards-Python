def main():
    from flashcard_interpretation import interpret_flashcards_csv, update_flashcards_csv
    flashcards = interpret_flashcards_csv()
    flashcards.sort(key = lambda card: card['level'])
    LEVEL_GOAL = 3

    while flashcards[0]['level'] < LEVEL_GOAL:
        flashcards = interpret_flashcards_csv()
        flashcards.sort(key = lambda card: card['level'])

        for i in range(9):
            from flashcard_alg import make_batch, batch_retrieval_alg
            batch = make_batch(flashcards, batch_size = 10)
            batch_retrieval_alg(flashcards, batch, batch_level_goal = 2)

        for i in range(9):
            from flashcard_alg import make_batch, batch_retrieval_alg
            batch = make_batch(flashcards, batch_size = 10)
            batch_retrieval_alg(flashcards, batch, batch_level_goal = 4)

if __name__ == "__main__":
    main()
