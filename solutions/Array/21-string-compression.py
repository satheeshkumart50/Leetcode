    # 443. String Compression
    # https://leetcode.com/problems/string-compression/
    # Time Complexity - O(n) where n is the length of chars
    # Space Complexity - O(1) for the variables used in the algorithm
    # Category - Array
    # Hint - Use two pointers, one for reading the characters and one for writing the compressed characters, iterate through the chars and count the occurrences of each character, if the count is greater than 1, write the character and the count to the chars list, at the end return the length of the compressed chars list
    # video - https://www.youtube.com/watch?v=fzUR4_WWKHk
    # video - https://www.youtube.com/watch?v=JycANhXZzyE
    def compress(self, chars: List[str]) -> int:

        read_pt, write_pt = 0, 0

        while read_pt < len(chars):
            start_pt = read_pt

            while read_pt < len(chars) and chars[read_pt] == chars[start_pt]:
                read_pt += 1

            chars[write_pt] = chars[start_pt]
            write_pt += 1

            if read_pt - start_pt > 1:
                for digit in str(read_pt - start_pt):
                    chars[write_pt] = digit
                    write_pt += 1

        return write_pt