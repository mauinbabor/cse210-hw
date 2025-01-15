import random

def main():
    """Generate and print six sentences."""
    print(make_sentence(1, "past"))
    print(make_sentence(1, "present"))
    print(make_sentence(1, "future"))
    print(make_sentence(2, "past"))
    print(make_sentence(2, "present"))
    print(make_sentence(2, "future"))

def make_sentence(quantity, tense):
    """Create and return a sentence with determiner, noun, verb, and prepositional phrases."""
    determiner = get_determiner(quantity)
    noun = get_noun(quantity)
    verb = get_verb(quantity, tense)
    prepositional_phrase = get_prepositional_phrase(quantity)

    # Exceeding requirements: Add a second prepositional phrase.
    second_prepositional_phrase = get_prepositional_phrase(quantity)

    return f"{determiner.capitalize()} {noun} {verb} {prepositional_phrase} {second_prepositional_phrase}."

def get_determiner(quantity):
    """Return a randomly chosen determiner based on the quantity."""
    if quantity == 1:
        words = ["a", "one", "the"]
    else:
        words = ["some", "many", "the"]
    return random.choice(words)

def get_noun(quantity):
    """Return a randomly chosen noun based on the quantity."""
    if quantity == 1:
        words = ["girl", "bird", "child", "dog", "cat", "rabbit", "car"]
    else:
        words = ["girls", "birds", "children", "dogs", "cats", "rabbits", "cars"]
    return random.choice(words)

def get_verb(quantity, tense):
    """Return a randomly chosen verb based on quantity and tense."""
    if tense == "past":
        words = ["talked", "drank", "laughed", "ran"]
    elif tense == "present":
        if quantity == 1:
            words = ["talks", "drinks", "laughs", "runs"]
        else:
            words = ["talk", "drink", "laugh", "run"]
    elif tense == "future":
        words = ["will talk", "will drink", "will laugh", "will run"]
    return random.choice(words)

def get_preposition():
    """Return a randomly chosen preposition."""
    prepositions = [
        "about", "above", "across", "after", "along",
        "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for",
        "from", "in", "into", "near", "of",
        "off", "on", "onto", "out", "over",
        "past", "to", "under", "with", "without"
    ]
    return random.choice(prepositions)

def get_prepositional_phrase(quantity):
    """Build and return a prepositional phrase."""
    preposition = get_preposition()
    determiner = get_determiner(quantity)
    noun = get_noun(quantity)
    return f"{preposition} {determiner} {noun}"

# Call the main function to execute the program.
if __name__ == "__main__":
    main()
