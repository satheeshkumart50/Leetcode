    # 151. Reverse Words in a String
    # https://leetcode.com/problems/reverse-words-in-a-string/
    # Time Complexity - O(n) where n is the length of string s
    # Space Complexity - O(n) for the variables used in the algorithm
    # Category - Array
    # Hint - Use split() method to split the string into words, split method splits even when there are multiple spaces and ignores the multiple spaces, then reverse the list of words and join them back into a string using join() method, at the end we return the reversed string

    def reverseWords(self, s: str) -> str:
        words = s.split()
        reversed_words = words[::-1]  # rds.reverse()
        return " ".join(reversed_words)