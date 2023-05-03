# cook your dish here
for t in range(int(input())):
    n,m=map(int,input().split())
    n=n-(0.1*n)
    if(n<m):
        print("ONLINE")
    elif(m<n):
        print("DINING")
    else:
        print("EITHER")
