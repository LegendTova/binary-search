import bisect
n,m,q=map(int,input().split())
listx=list(map(int,input().split()))
listy=list(map(int,input().split()))
listx.sort()
listy.sort()
for _ in range(q):
    count=0
    listq=input().split()
    z=int(listq[0])
    qno=listq[1]
    if(qno=='A'):
        p=bisect.bisect_left(listx,int(listq[2]))
        q=bisect.bisect(listx,int(listq[3]))
        listxn=listx[p:q]
        listyn=listy
        l1=q-p
        l2=m
    elif(qno=='B'):
        p = bisect.bisect_left(listy, int(listq[2]))
        q = bisect.bisect(listy, int(listq[3]))
        listyn = listy[p:q]
        listxn=listx
        l1=n
        l2=q-p
    else:
        p = bisect.bisect_left(listx, int(listq[2]))
        q = bisect.bisect(listx, int(listq[3]))
        listxn = listx[p:q]
        r = bisect.bisect_left(listy, int(listq[4]))
        s = bisect.bisect(listy, int(listq[5]))
        listyn = listy[r:s]
        l1=q-p
        l2=s-r
    
    if(l1 ==0 or l2==0 or (listxn[0]+listyn[0])>z):
        print(0)
        continue
    elif(listxn[-1]+listyn[-1]<=z):
        print(l1*l2)
    else:
        for i in reversed(listxn):
            a=bisect.bisect(listyn,(z-i))
            if(a==l2):
                break
            count=count+(l2-a)
        print(l1*l2-count)
