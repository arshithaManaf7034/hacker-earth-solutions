# Read number of songs
n = int(input())

# Read singers of each song
songs = list(map(int, input().split()))

# Create empty dictionary
count = {}

# Count songs for each singer
for singer in songs:
    if singer in count:
        count[singer] = count[singer] + 1
    else:
        count[singer] = 1

# Find maximum count
max_count = 0
for value in count.values():
    if value > max_count:
        max_count = value

# Count how many singers have max_count
favourite = 0
for value in count.values():
    if value == max_count:
        favourite = favourite + 1

# Print result
print(favourite)
