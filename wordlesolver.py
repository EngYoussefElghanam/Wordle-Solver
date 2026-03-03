import json
import math

with open('targets_5_letter.json','r') as file:
    answers = json.load(file)

with open('dictionary_5_letter.json','r') as file2:
    guesses = json.load(file2)

def feedback(g,a):
    #TODO write the feedback function
    pass

def score_guess(guess, possible_answers):
    patterns = {}
    for answer in possible_answers:
        pat = feedback(guess, answer)
        patterns[pat] = patterns.get(pat, 0) + 1
    # entropy
    total = len(possible_answers)
    entropy = 0
    for count in patterns.values():
        p = count / total
        entropy -= p * math.log2(p)

    return entropy

gss = list(guesses)
s = list(answers)
for turn in range(1, 7):  # max 6 turns
    print(f"\n===== Turn {turn} =====")
    print("Remaining possible answers:", len(s))

    # TODO handle the case if no possible answer remains len(s) == 0 ERROR HE GAVE US WRONG INFO
    if(turn != 1):
        scored_guesses = sorted(
            gss,
            key=lambda g: score_guess(g, s),
            reverse=True
        )
    else:
        scored_guesses = gss

    # --- Show Top Suggestions ---
    print("----------- Top Suggestions -----------")
    for i in range(min(10, len(scored_guesses))):
        print(f"{i+1} - {scored_guesses[i]}")

    # TODO User Input store in guess and the pattern store in pattern
    guess = None
    pattern = None
    # TODO handle the case of ggggg before filtering

    # --- FILTER POSSIBLE ANSWERS ---
    s = [word for word in s if feedback(guess, word) == pattern]

    # TODO if only one solution remains
