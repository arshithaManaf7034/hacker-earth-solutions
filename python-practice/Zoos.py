# Read input word
word = input()

# Count z and o
z_count = 0
o_count = 0

for ch in word:
    if ch == 'z':
        z_count += 1
    elif ch == 'o':
        o_count += 1

# Check condition
if o_count == 2 * z_count:
    print("Yes")
else:
    print("No")
