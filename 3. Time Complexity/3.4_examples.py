
#3.4.2 Sort and Compare
def anagramSolution1(s1, s2):
    """
    This function checks if two strings are anagrams of each other.
    An anagram is a word or phrase formed by rearranging the letters of another.
    For example, 'abcde' and 'edcba' are anagrams.

    The approach used here is:
    1. Convert both strings into lists of characters.
    2. Sort both lists alphabetically.
    3. Compare the sorted lists element by element.
    If all elements match, the strings are anagrams.
    """
    # Convert strings to lists of characters
    alist1 = list(s1)
    alist2 = list(s2)

    # Sort both lists alphabetically
    alist1.sort()
    alist2.sort()

    # Initialize variables for comparison
    pos = 0  # Position index for iteration
    matches = True  # Flag to track if all characters match

    # Compare sorted lists element by element
    while pos < len(s1) and matches:
        if alist1[pos] == alist2[pos]:  # Check if characters at current position match
            pos += 1  # Move to the next position
        else:
            matches = False  # Set flag to False if characters don't match

    # Return True if all characters match, otherwise False
    return matches

#print(anagramSolution1('abcde','edcba'))

#3.4.4 Count and Compare
def anagramSolution4(s1, s2):
    # Initialize frequency counters for each letter (assuming lowercase a-z)
    c1 = [0] * 26  
    c2 = [0] * 26

    # Count occurrences of each letter in the first string
    for i in range(len(s1)):
        # Calculate the position of the letter in the alphabet (0 for 'a', 1 for 'b', etc.)
        pos = ord(s1[i]) - ord('a')  
        c1[pos] = c1[pos] + 1

    # Count occurrences of each letter in the second string
    for i in range(len(s2)):
        pos = ord(s2[i]) - ord('a')  
        c2[pos] = c2[pos] + 1

    # Compare frequency counts for all letters
    j = 0
    stillOK = True
    while j < 26 and stillOK:
        if c1[j] == c2[j]:  # Check if counts match for the current letter
            j = j + 1  # Move to the next letter
        else:
            stillOK = False  # Stop if counts don't match

    # Return True if all counts match, otherwise False
    return stillOK

#print(anagramSolution4('apple', 'pleap'))  # Expected output: True

