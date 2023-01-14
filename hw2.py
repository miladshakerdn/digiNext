def minCharsToRemove(str):
    count = 0
    for i in range(len(str) - 1):
        if str[i] == str[i + 1]:
            count += 1
    return count

print(minCharsToRemove("AAAA"))
print(minCharsToRemove("BBBBB"))
print(minCharsToRemove("ABABABAB"))
print(minCharsToRemove("BABABA"))
print(minCharsToRemove("AAABBB"))