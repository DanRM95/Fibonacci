#  This prints Fibonacci's sequence
def fib(n_terms):  # "shadows name from outer scope" WHAT?!
    count = 0  # This counts how many loops or, in other words, how many Fibonacci terms we calculate
    a, b = 0, 1
    while count < n_terms:  # Number of terms in the sequence stop
        print(a)
        count = count + 1  # I completely stole this, but I understand how it works: with MATH.
        a, b = b, a + b  # In which order does this happen?


# Asking user for how many terms
while True:  # Loopy-loop-loop, does this makes it so that it keeps asking you unless we hit 'break'?
    n_terms = input(f'How many terms would you like to calculate?\n')
    try:  # Is try somewhat similar to 'if'?
        n_terms = int(n_terms)  # How can I check for point zero values and turn them into int?
        break  # Exits the loop
    except ValueError:  # What types of errors are there?
        print(f'Invalid value. Try again.\n')  # Can I use 'raise'?


fib(n_terms)

# Still spaghetti?
