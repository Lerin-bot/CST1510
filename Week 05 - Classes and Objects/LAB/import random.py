import random

nouns = ["penguin", "robot", "wizard", "student", "dragon"]
verbs = ["ate", "discovered", "investigated", "trained", "optimised"]
adjectives = ["confused", "tiny", "mysterious", "ancient", "enthusiastic"]

noun_weights = [1, 5, 2, 3, 1]
verb_weights = [1, 5, 2, 3, 2]
adjective_weights = [2, 3, 4, 2, 5]


def make_sentence():
    noun = random.choices(nouns, weights=noun_weights, k=1)[0]
    verb = random.choices(verbs, weights=verb_weights, k=1)[0]
    adjective = random.choices(adjectives, weights=adjective_weights, k=1)[0]
    return f"The {adjective} {noun} {verb} the hidden vault."


for _ in range(3):
    print(make_sentence())
