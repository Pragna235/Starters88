# cook your dish here
for t in range(int(input())):
    n=int(input())
    arr=list(map(int,input().split()))
    s=set(arr)
    a=list(s)
    a.sort(reverse=True)
    print(a[0]+a[1])
    