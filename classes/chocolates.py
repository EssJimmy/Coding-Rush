def solve(n: int, arr: list):
    s = sum(arr)

    print(s//n)

def main():
    n = int(input())
    a = list(map(int, input().split()))

    solve(n ,a)

main()