def solve():
    [n, m] = map(int, input().split())
    
    lo = 0
    hi = 0

    a = list(map(int, input().split()))
    hi = max(a)

    hi *= m
    while lo < hi:
        mid = (lo + hi) // 2
        kol = 0

        for i in range(n):
            kol += mid // a[i]
        
        if kol < m: lo = mid + 1
        else: hi = mid

    print(lo)

def main():
    solve()

if __name__ == '__main__':
    main()