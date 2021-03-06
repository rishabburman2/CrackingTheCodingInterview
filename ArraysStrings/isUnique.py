# Is Unique: Implement an algorithm to determine if a string has all unqiue characters. What if you cannot use additional Data Structures

# Brute Force with O(N**2) runtime
def isUniqueBrute(s):

    if len(s) > 256:
        return False

    for i in range(len(s) - 1):
        for j in range(i + 1, len(s)):
            if s[i] == s[j]:
                return False

    return True


# Code with extra memory but O(N) run time
def isUniqueWithExtraMem(s):
    boolSet = [False] * 256

    if len(s) > 256:
        return False

    for i in range(len(s)):
        # If character is already at the position
        if boolSet[ord(s[i])]:
            return False

        boolSet[ord(s[i])] = True
    return True


# Code with constant space and O(N log N) time
def sort_string(s):
    s = ''.join(sorted(s))
    for i in range(len(s)):
        if s[i] == s[i - 1]:
            return False

    return True


def main():
    s = "Rishab2355"
    ans = sort_string(s)
    if ans:
        print('All Unique Characters')
    else:
        print('Not all characters unique')


main()
