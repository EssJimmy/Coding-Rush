def solve(n:int, arr:list):
    s = set()
    arr.sort()

    for i in range(n//2):
        s.add((arr[i] + arr[n - i - 1])/2)

    print(len(s))

def main():
    n = int(input())
    arr = list(map(int, input().split()))

    solve(n, arr)

if __name__ == '__main__':
    main()