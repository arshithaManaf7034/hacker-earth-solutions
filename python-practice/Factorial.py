# Read input
n = int(input())

# Initialize factorial
fact = 1

# Calculate factorial
for i in range(1, n + 1):
    fact = fact * i

# Print result
print(fact)
