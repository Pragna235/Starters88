# cook your dish here
for t in range(int(input())):
    n=int(input())
    arr=list(map(int,input().split()))
    count=0
    
    def f(l,r):
        sum=0
        if(l==r):
            sum=0
        else:
            for i in range(l,r):
                sum+=(arr[i] - arr[i+1])
        return sum
        
    for i in range(len(arr)):
        for j in range(i):
            if(f(i,j) != (arr[j]-arr[i])):
                count+=1
            
        
        
    print(count)
