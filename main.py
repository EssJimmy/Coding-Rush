import math

n = int(input())

for i in range(n):
    consoleInput = input()
    arr = list(map(int, consoleInput.split(" ")))

    largest_ending_here = 0
    largest_overall = -math.inf

    for j in range(len(arr)):
        largest_ending_here += arr[j]
        largest_overall = max(largest_ending_here, largest_overall)
        if largest_ending_here < 0:
            largest_ending_here = 0

    print(f"Caso #{i+1}: {largest_overall}")
