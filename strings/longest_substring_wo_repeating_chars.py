def lengthOfLongestSubstring(s: str) -> int:
    res = candidate = ''
    for i in range(0, len(s)):
        if s[i] not in candidate:
            candidate += s[i]
            for j in range(i + 1, len(s)):
                if s[j] not in candidate:
                    candidate += s[j]
                else:
                    break

            if len(res) < len(candidate):
                res = candidate
            candidate = ''

    return len(res)


test = "jbpnbwwd"
# test = " "
print(lengthOfLongestSubstring(test))
