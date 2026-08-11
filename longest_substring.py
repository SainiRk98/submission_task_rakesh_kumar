def longest_substring(s):
    words={}
    left=0
    max_length=0
    for right in range(len(s)):
        char=s[right]
        if char in words and words[char]>=left:
            left=words[char]+1
        words[char]=right
        max_length=max(max_length, right-left+1)
    return max_length

s= "abcabcbb"
print(longest_substring(s))