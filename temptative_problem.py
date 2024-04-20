def super_digit(x):
    if x < 10: return x
    
    newx = 0
    
    while x > 0:
        newX += x%10
        x = x//10

    return super_digit(newx)

def main():
    n = input()
    k = int(input())

    p = 0
    for i in n:
        p += int(i)

    p *= k

    print(super_digit(p))

if __name__ == '__main__':
    main()