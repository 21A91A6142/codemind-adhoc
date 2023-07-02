def isdisc(a,c,d,b):
    m=[]
    for i in range(b):
        k=max(d)
        l=[]
        for j in c:
            if a.count(j)==k:
                l.append(j)
        m.append(max(l))
        d.remove(k)
        c.remove(max(l))
    print(*m)
                
n=int(input())
a=list(map(int,input().split()))
b=int(input())
c=set(a)
c=sorted(c)
d=[]
for i in c:
    d.append(a.count(i))
isdisc(a,c,d,b)