import itertools

def solve_crypto():
    # Take input from user in the format WORD1 + WORD2 = WORD3
    equation = input("Enter cryptoarithmetic equation (e.g., SEND+MORE=MONEY): ").replace(" ", "")

    # Extract unique letters
    letters = sorted(set([ch for ch in equation if ch.isalpha()]))

    if len(letters) > 10:
        print("Too many unique letters! Cannot assign digits.")
        return

    # Digits 0-9
    digits = range(10)

    # Words in the equation
    left_side, result = equation.split("=")
    left_terms = left_side.split("+")

    # Try all permutations
    for perm in itertools.permutations(digits, len(letters)):
        assign = dict(zip(letters, perm))

        # Skip if any word starts with zero
        if any(assign[word[0]] == 0 for word in left_terms + [result]):
            continue

        # Convert words to numbers
        left_values = [int("".join(str(assign[ch]) for ch in word)) for word in left_terms]
        result_value = int("".join(str(assign[ch]) for ch in result))

        # Check sum
        if sum(left_values) == result_value:
            print("\nSolution Found!")
            for word, value in zip(left_terms + [result], left_values + [result_value]):
                print(f"{word} = {value}")
            print("Mapping:", assign)
            return

    print("No solution found.")

# Run the solver
solve_crypto()
