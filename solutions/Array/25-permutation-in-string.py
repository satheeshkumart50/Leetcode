    # 567. Permutation in String
    # https://leetcode.com/problems/permutation-in-string/
    # Time Complexity - O(n*m) where n is the length of s2 and m is the length of s1
    # Space Complexity - O(1) for the variables used in the algorithm
    # Category - Array
    # Hint - Use two character arrays to store the frequency of characters in s1 and s2, then iterate through s2 and for each substring of length equal to s1, compare the frequency arrays, if they are equal, return True, otherwise continue, at the end we return False if no permutation is found
    # Refer - video - https://www.youtube.com/watch?v=quSfR-uwkZU

    def checkInclusion(self, s1: str, s2: str) -> bool:

        # Approach 1 - using Character Array
        s1_lst = [0] * 26
        s2_lst = [0] * 26

        for ch in s1:
            s1_lst[ord(ch) - 97] += 1

        i = 0
        while i < (len(s2) - len(s1) + 1):
            for x in range(i, i + len(s1)):
                s2_ch = s2[x]
                s2_lst[ord(s2_ch) - 97] += 1

            if s1_lst == s2_lst:
                return True
            else:
                i += 1
                s2_lst[:] = [0] * 26

        return False

        # Approach 2 - using Map
        """
        s1_map = dict()
        s2_map = dict()
        is_sub_str = False

        for ch in s1:
            s1_map[ch] = s1_map.get(ch,0)+1

        i = 0
        while i < (len(s2)-len(s1)+1):
            for x in range(i, i+len(s1)):
                s2_ch = s2[x]
                s2_map[s2_ch] = s2_map.get(s2_ch, 0)+1
            
            j = 0
            for k in s1_map:
                j += 1
                if k not in s2_map or s1_map[k] != s2_map[k]:
                    break
                if j == len(s1_map):
                    is_sub_str = True

            if is_sub_str:
                return is_sub_str
            else:
                i += 1
                s2_map.clear()

        return is_sub_str
        """