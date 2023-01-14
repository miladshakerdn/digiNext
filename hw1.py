def count_a(string, num):
    # repeat the string until it reaches the given length
    while len(string) < num:
        string += string

    # count the number of 'a' characters in the new string
    count = 0
    for char in string:
        if char == 'a':
            count += 1

    return count

print(count_a('abcac', 10))