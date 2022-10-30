a = int(input())
arr = list(map(int, input().split()))
if sum(arr)%5==0:
    print('yes')
else: print('no')
