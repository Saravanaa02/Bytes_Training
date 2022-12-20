chars = {}
        start = 0
        max_length = 0
            
        for end, c in enumerate(s):
            if c in chars:
                start = max(start, chars[c] + 1)
            
            max_length = max(max_length, end - start + 1)
            chars[c] = end
        return max_length
