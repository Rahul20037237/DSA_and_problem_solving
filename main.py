def cyclic_shift_count(length, cycle, s):
    max_binary = '1' * length  # Maximum binary number of length 'length'
    max_integer = int(max_binary, 2)  # Convert max_binary to integer
    occurrences = []
    original = s
    
    # Perform cyclic shifts and find occurrences of max_binary
    for i in range(length):
        s = s[1:] + s[0]  # Perform cyclic shift
        if int(s, 2) == max_integer:  # Convert current s to integer and compare
            occurrences.append(i + 1)  # Record occurrence index (1-indexed)
            if len(occurrences) == cycle:
                return occurrences[-1]  # Return the index of the cycle-th occurrence
    
    return -1  # If there are not enough occurrences, return -1 as per problem statement
N=int(input())
for i in range(N):
    length,cycle=map(int,input().split())
    s=input()
    a=cyclic_shift_count(length,cycle,s)
    print(a)
# 1745489744