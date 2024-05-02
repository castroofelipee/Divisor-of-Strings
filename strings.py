class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if not str1 or not str2:
            return ""

        len1, len2 = len(str1), len(str2)
        while len1 != len2:
            len1 = len2 if len1 < len2 else len1 % len2
            len2 = len1

        return str1[:len1]



# Author: Felipe Castro on May 2, 2024

# 'class Solution' defines a class named Solution
# The code checks if either str1 or str2 is empty. If so, it returns an empty string ("").
# It then calculates the lengths of str1 and str2 and stores them in len1 and len2.
# A loop iterates until len1 and len2 are equal.

    # Inside the loop, it uses a modulo operation (%) to find the remainder when len1 is divided by len2.
    # The shorter length (len1 or len2) is updated to this remainder to ensure both strings eventually have the same length (the GCD length).

# After the loop, len1 (or len2 as they'll be identical) represents the GCD length.
# The function returns the first len1 characters of str1 (or str2) as that substring represents the GCD.