def tacos_de_canasta(m: int, arr: list) -> list:
    mpp = {}
    ans = [0, 0]

    for i in range(len(arr)):
        if (m - arr[i]) in mpp:
            ans[0] = mpp[m - arr[i]] + 1
            ans[1] = i + 1
            return ans
        
        mpp[arr[i]] = i

    return ans


def main():
    t = input()

    for i in range(t):
        m = int(input())
        arr = list(map(int, input().split()))
        print(tacos_de_canasta(m, arr))