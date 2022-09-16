n=int(input())
A=list(map(int, input().split()))
A=A[:n]
listA=A
mina=0
mina=min(A)
A=A.remove(min(A))
mina2=min(listA)
print(mina,mina2)
