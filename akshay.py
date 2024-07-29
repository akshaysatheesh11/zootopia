
def isIsomorphic(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    
    # Two dictionaries to store mappings
    s_to_t = {}
    t_to_s = {}
    
    for char_s, char_t in zip(s, t):
        # Check and create mapping from s to t
        if char_s in s_to_t:
            if s_to_t[char_s] != char_t:
                return False
        else:
            s_to_t[char_s] = char_t
        
        # Check and create mapping from t to s
        if char_t in t_to_s:
            if t_to_s[char_t] != char_s:
                return False
        else:
            t_to_s[char_t] = char_s
    
    return True

# Test examples
print(isIsomorphic("egg", "add"))  # Output: true
print(isIsomorphic("foo", "bar"))  # Output: false
print(isIsomorphic("paper", "title"))  # Output: true

             


