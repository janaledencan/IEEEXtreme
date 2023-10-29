n, m, x, y = map(int, input().split())
print((m+n*y)//(x+y) if (m+n*y)//(x+y)< n else n)