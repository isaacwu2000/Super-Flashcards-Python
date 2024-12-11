def model(system_prompt="", user_prompt=""):
    from openai import OpenAI
    model = OpenAI(api_key = "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")

    completion = model.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ],
        temperature=0.5
    )

    return completion.choices[0].message.content

def ci_question(card): # ci stands for comprehensible input
    system = "Your sentences should serve as comprehensible input (CI) for the given vocabulary, such that the User could guess the vocab word from the context. Make your sentences enitrely in Spanish."
    task = f"Make a CI sentence with the word {card['term']}"
    print(f"\nSentence: {model(system, task)}")

    user_def = input(f"\nBased on the sentence above, what is the meaning of the term \'{card['term']}\'?\n>> ")
    check_user_def = model("Answer with exactly 'y' or 'n' with no quotation marks. Also, ensure that it is not random text such as a one letter character. However, accept synonyms and minor variations / spelling errors.", f"Is the User's definition '{user_def}' GENERALLY correct for the Spanish term \'{card['term']}\'?")

    if check_user_def == 'y':
        print(f"\nCorrect, the definition of \'{card['term']}\' is {card['definition']}")
        return "correct"
    else:
        print(f"\nIncorrect, the definition of \'{card['term']}\' is {card['definition']}")
        return "incorrect"

def sentence_creation_question(card):
    user_sentence = input(f"\nCreate a sentence with the term \'{card['term']}\'\n>> ")
    check_user_sentence = model("Answer with exactly 'y' or 'n' with no quotation marks. IGNORE minor variations, spelling errors, and small mistakes.", f"Does this sentence GENERALLY use the term \'{card['term']}\' correctly? Sentence: '{user_sentence}'")

    if check_user_sentence == 'y':
        print(f"\nCorrect, the definition of \'{card['term']}\' is {card['definition']}.")
        print("\n"+model("You provide concise gramatical, word-use, and general constructive feedback on Spanish learners\' sentences.", f"Provide feedback on this sentence '{user_sentence}'"))
        return "correct"
    else:
        print(f"\nIncorrect, the definition of \'{card['term']}\' is {card['definition']}")
        print("\n"+model("You provide concise gramatical, word-use, and general constructive feedback on Spanish learners\' sentences.", f"Provide feedback on this sentence '{user_sentence}'"))
        return "incorrect"