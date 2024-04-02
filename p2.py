def largest_rectangle(n: int, arr: list) -> int:
    maxArea = -1
    s = []
    topArea = 0

    i = 0
    while i < n:
        if len(s) == 0 or arr[s[0]] <= arr[i]:
            s.push(i)
            i = i + 1
        else:
            tp = s[0]
            s.pop()
            topArea = arr[tp]*(i if len(s) == 0 else i - s[0] - 1)

            if maxArea < topArea:
                maxArea = topArea

    for i in s:
        topArea = arr[tp]*(i if len(s) == 0 else i - s[0] - 1)

        if maxArea < topArea:
                maxArea = topArea

    return maxArea

def main():
    n = int(input())

    arr = list(map(int, input().split()))
    print(largest_rectangle(n, arr))