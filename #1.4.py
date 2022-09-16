n=int(input())
A=list(map(int, input().split()))
A=A[:n]
count=0
for i in range(0,len(A)-2):
    if A[i+1]>A[i] and A[i+1]>A[i+2]:
        count+=1
print(count)
