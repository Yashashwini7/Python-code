numbers = [2, 3, 4, 55, 56, 78, 75, 69, 66, 101, 100]

# Initialize counters
even_count = 0
odd_count = 0

# Iterate through the list
for num in numbers:
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

# Print the results
print("Number of even numbers:", even_count)
print("Number of odd numbers:", odd_count)
