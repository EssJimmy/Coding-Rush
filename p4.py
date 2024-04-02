def super_reduced_string(s: str):
    is_zero = False

    i = 0
    while i < len(str) and not is_zero:
        if s[i] == s[i+1]:
            s[i] = ''
            s[i] = ''

            i = -1
        
        else:
            i = i+1

        is_zero = len(s) == 0

    if is_zero:
        return "Empty String"
    else:
        return s
    

def main():
    s = input()
    print(super_reduced_string)