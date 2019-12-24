"""This program solves the Codebreaker board game"""
import itertools

COLORS = ["white", "black", "blue", "red", "green", "yellow", "orange", "pink"]
CODELENGTH = 5

candidate_permuations = list(itertools.permutations(COLORS, CODELENGTH))

def num_matching_colors(a, b):
    return len(set(a).intersection(b))

def has_expected_num_matching_colors(a,b,expected):
    return expected == num_matching_colors(a,b)

def num_matching_positions(a,b):
    counter = 0
    for i, elm in enumerate(a):
        if b[i] == elm:
            counter += 1
    return counter

def has_expected_num_matching_positions(a,b,expected):
    return expected == num_matching_positions(a,b)

def make_guess(guess, num_correct_colors, num_correct_positions, candidate_permuations):
    filtered_correct_positions = filter(lambda x: has_expected_num_matching_positions(guess, x, num_correct_positions), candidate_permuations)
    filtered_num_colors = filter(lambda x: has_expected_num_matching_colors(guess, x, num_correct_colors), filtered_correct_positions)
    return list(filtered_num_colors)

suggested_guess = candidate_permuations[0]
print("Suggested guess: ", suggested_guess)

while(True):
    guess = input("Guess: (enter to accept suggested)").split(" ")
    if not guess[0]:
        guess = suggested_guess
    matching_colors, matching_positions = input("Matching colors, positions: ").split(" ")
    matching_colors = int(matching_colors)
    matching_positions = int(matching_positions)

    matching_colors += matching_positions # The board convention is that the number of matching colors is exclusive of the number of matching positions

    print("Matching Colors: ", matching_colors, "   Matching Positions: ", matching_positions)

    candidate_permuations = make_guess(guess, matching_colors, matching_positions, candidate_permuations)

    print("Candidates narrowed to: ", len(candidate_permuations))
    suggested_guess = candidate_permuations[0]

    print("")
    print("Suggested guess: ", suggested_guess)
    if len(candidate_permuations) == 1:
        answer = candidate_permuations[0]
        print("Answer: ", answer)
        break
