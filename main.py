def main():
    n, x, y = map(int, input().split())
    t = x
    t += (n - 1) // (x + y)
    print(t + 1)

main()