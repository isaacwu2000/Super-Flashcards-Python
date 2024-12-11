def make_batch(flashcards, batch_size = 20):
    # Organziing flashcards by level ascendingly, and returning a batch of the 20 lowest level flashcards
    ascending_level_flashcards = sorted(flashcards, key = lambda card: card['level'])
    return ascending_level_flashcards[:batch_size]

def batch_retrieval_alg(flashcards, batch, batch_level_goal = 3):
    from model import ci_question, sentence_creation_question
    from flashcard_interpretation import update_flashcards_csv
    import random

    # Retrieval algorithm, runs until the batch_level_goal is reached
    while batch[0]['level'] < batch_level_goal:
        lowest_level_card = batch[0] # Selects the lowest level card (since the batch is sorted)

        # Giving a CI question if the level is 0
        if lowest_level_card['level'] == 0:
            if ci_question(lowest_level_card) == "correct":
                lowest_level_card['level'] += 1
        # Giving a sentence creation question if the level is not 0
        else:
            if sentence_creation_question(lowest_level_card) == "correct":
                lowest_level_card['level'] += 1
            else:
                lowest_level_card['level'] -= 1
        print("--------------") # Seperates words

        random.shuffle(batch)
        batch.sort(key = lambda card: card['level']) # Sorting the batch by level
    
        # Returning the batch (with updated levels) and the rest of the flashcards
        if len(flashcards) > len(batch):
            flashcards = batch + flashcards[(len(batch) + 1):]
        update_flashcards_csv(flashcards)