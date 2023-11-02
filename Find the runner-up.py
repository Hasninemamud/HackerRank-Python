n = int(input())
arr = map(int, input().split())
result = sorted(set(arr), reverse=True)
print(result[1])