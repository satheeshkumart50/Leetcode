    # 76. Minimum Window Substring
    # https://leetcode.com/problems/minimum-window-substring/
    # Time Complexity - O(n) where n is the length of string s
    # Space Complexity - O(m) where m is the length of string t
    # Category - Array
    # Hint - Use a sliding window approach with two pointers and a hash map(Counter Class) to store the frequency of characters in string t, we can iterate through string s and for each character, we can update the frequency of characters in the current window, if the frequency of characters in the current window matches the frequency of characters in string t, then we can update the minimum length of the window and the starting index of the window, at the end we return the substring of s that corresponds to the minimum length window that contains all characters of t
    # Refer - video - https://www.youtube.com/watch?v=SdeaOYoPhIs

    # from collections import Counter
    def minWindow(self, s: str, t: str) -> str:

        if not t or not s or len(t) > len(s):
            return ""

        min_len = float("inf")
        ans = (0, 0)

        # counter is a subclass of dict that helps to count hashable objects, it is an unordered collection where elements are stored as dictionary keys and their counts are stored as dictionary values, it is a part of collections module
        # for t = "ABC", Counter(t) will return Counter({'A': 1, 'B': 1, 'C': 1})
        t_count = Counter(t)  # frequency of required chars
        s_count = Counter()

        l = 0
        formed = False

        for r, ch in enumerate(s):
            s_count[ch] += 1

            # Counter objects support rich comparison operators for equality and inequality, as well as the subset and superset operations. This means that we can compare two Counter objects to see if they have the same elements with the same counts, or if one is a subset or superset of the other. In this case, we are checking if s_count has all the required characters with their respective counts as in t_count.
            # Counter({'A':1,'B':1,'C':1}) == Counter({'A':1,'B':1,'C':1}) returns True
            # Counter({'A':1,'B':2,'C':1,'D':2}) == Counter({'A':1,'B':1,'C':1}) returns False
            # Counter({'A':1,'B':2,'C':1,'D':2}) >= Counter({'A':1,'B':1,'C':1})  returns True
            if s_count >= t_count:
                formed = True

            while formed:
                min_len = min(min_len, r - l + 1)
                if min_len == r - l + 1:
                    ans = (l, r + 1)

                s_count[s[l]] -= 1

                if s_count[s[l]] == 0:
                    del s_count[s[l]]

                if not s_count >= t_count:
                    formed = False

                l += 1

        if min_len == float("inf"):
            return ""

        return s[ans[0] : ans[1]]