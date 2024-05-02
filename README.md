# Divisor of Strings
- This is an 'easy' `Leetcode` logic project that involves a sequence of strings with divisor functions;
- The code checks if either `str1` or `str2` is empty. If so, it returns an empty string ("").
- It then calculates the lengths of str1 and str2 and stores them in `len1` and `len2`
- A loop iterates until len1 and len2 are equal.

    - Inside the loop, it uses a modulo operation (%) to find the remainder when len1 is divided by len2.
    - The shorter length (len1 or len2) is updated to this remainder to ensure both strings eventually have the same length (the GCD length).

- After the loop, len1 (or len2 as they'll be identical) represents the GCD length.
- The function returns the first len1 characters of str1 (or str2) as that substring represents the GCD.

- If you want to follow any of my challenges made on `Leetcode` [Follow me](https://leetcode.com/u/castroofelipee/)