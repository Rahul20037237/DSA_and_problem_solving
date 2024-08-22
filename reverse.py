def cyclic_shift_count(length, cycle, s):
    max_binary = '1' * length  # Maximum binary number of length 'length'
    occurrences = []
    original = s
    
    # Perform cyclic shifts and find occurrences of max_binary
    for i in range(length):
        s = s[1:] + s[0]  # Perform cyclic shift
        if s == max_binary:
            occurrences.append(i + 1)  # Record occurrence index (1-indexed)
            if len(occurrences) == cycle:
                return occurrences[-1]  # Return the index of the cycle-th occurrence
    
    return -1  # If there are not enough occurrences, return -1 as per problem statement

# Example usage:
length = 100
cycle = 872744873
s = '1010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010'

# Calculate and print the result
result = cyclic_shift_count(length, cycle, s)
print(result)
