def is_balanced(s: str) -> str:
    chars = []
    mpp = {}
    mpp['('] = ')'
    mpp['['] = ']'
    mpp['{'] = '}'

    for c in s:
        if len(chars) == 0 or c in mpp:
            chars.append(c)

        elif mpp[chars[0]] == c:
            chars.pop()
        
        else: return "NO"

    if len(chars) != 0:
        return "NO"

    return "YES"


def main():
    s = input()
    return(is_balanced)