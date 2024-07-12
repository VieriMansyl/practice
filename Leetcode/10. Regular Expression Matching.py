def isMatch(s: str, p: str) -> bool:
    i, j = len(s) - 1, len(p) - 1
    return backtrack({}, s, p, i, j)

def backtrack(cache, s, p, i, j):
    key = (i, j)
    if key in cache:
        return cache[key]

    if i == -1 and j == -1:
        cache[key] = True
        return True

    if i != -1 and j == -1:
        cache[key] = False
        return cache[key]

    if i == -1 and p[j] == '*':
        k = j
        while k != -1 and p[k] == '*':
            k -= 2
        
        if k == -1:
            cache[key] = True
            return cache[key]
        
        cache[key] = False
        return cache[key]
    
    if i == -1 and p[j] != '*':
        cache[key] = False
        return cache[key]

    if p[j] == '*':
        if backtrack(cache, s, p, i, j - 2):
            cache[key] = True
            return cache[key]
        
        if p[j - 1] == s[i] or p[j - 1] == '.':
            if backtrack(cache, s, p, i - 1, j):
                cache[key] = True
                return cache[key]
    
    if p[j] == '.' or s[i] == p[j]:
        if backtrack(cache, s, p, i - 1, j - 1):
            cache[key] = True
            return cache[key]

    cache[key] = False
    return cache[key]

print(isMatch("aa", "a"))
print(isMatch("aaa", "a*a"))
print(isMatch("aaa", "aaaa"))
print(isMatch("aa", "a*"))
print(isMatch("ab", ".*"))
print(isMatch("ab", ".*c"))
print(isMatch("aab", "c*a*b"))
print(isMatch("mississippi", "mis*is*ip*."))