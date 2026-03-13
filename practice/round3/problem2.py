# Problem 2 — Encrypted Card Token Decoder (Foundational)
# Visa's tokenization service encodes card tokens using a simple transformation. 
# You are given a string s consisting of lowercase letters and digits, and an integer shift.
# Apply the following decoding rules in order:

# Reverse every consecutive group of letters (digits stay in place and act as group separators).
# After reversing, shift every letter forward in the alphabet by shift positions (wrap around from z to a).
# Finally, compress the result using run-length encoding: 
# replace consecutive identical characters with the character followed by its count. 
# Single characters (count of 1) should appear without a count.

# Example:
# Input: s = "abc3def2gh", shift = 1

# Step 1 - Reverse letter groups:
#   "abc" → "cba", "def" → "fed", "gh" → "hg"
#   Result: "cba3fed2hg"

# Step 2 - Shift letters by 1:
#   c→d, b→c, a→b, f→g, e→f, d→e, h→i, g→h
#   Result: "dcb3gfe2ih"

# Step 3 - Run-length encode:
#   All characters are unique in sequence → "dcb3gfe2ih"
#   (No compression needed here)

# Output: "dcb3gfe2ih"
input = ["adgw","adgx","adgy","adgz","adhw","adhx","adhy","adhz","adiw","adix","adiy","adiz","aegw","aegx","aegy","aegz","aehw","aehx","aehy","aehz","aeiw","aeix","aeiy","aeiz","afgw","afgx","afgy","afgz","afhw","afhx","afhy","afhz","afiw","afix","afiy","afiz","bdgw","bdgx","bdgy","bdgz","bdhw","bdhx","bdhy","bdhz","bdiw","bdix","bdiy","bdiz","begw","begx","begy","begz","behw","behx","behy","behz","beiw","beix","beiy","beiz","bfgw","bfgx","bfgy","bfgz","bfhw","bfhx","bfhy","bfhz","bfiw","bfix","bfiy","bfiz","cdgw","cdgx","cdgy","cdgz","cdhw","cdhx","cdhy","cdhz","cdiw","cdix","cdiy","cdiz","cegw","cegx","cegy","cegz","cehw","cehx","cehy","cehz","ceiw","ceix","ceiy","ceiz","cfgw","cfgx","cfgy","cfgz","cfhw","cfhx","cfhy","cfhz","cfiw","cfix","cfiy","cfiz"]
print(len(input))


def letterCombinations(digits):
    """
    Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.
    Mapping is like phone buttons.
    """
    if not digits:
        return []
    
    phone = {
        "2": "abc", "3": "def", "4": "ghi", "5": "jkl", 
        "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
    }
    
    res = [""]

    for digit in digits:    
        tmp = []
        for prefix in res:
            for l in phone.get(digit, ""):
                tmp.append(prefix + l)
        res = tmp
    
    return res

# Example usage:
digits = "23"
print(letterCombinations(digits))


print([["-" * 5]*5])
value = ("-"*5)
value = value.split()
print(value)