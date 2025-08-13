import random
def quicksort(a, L, R):
    if(L>=R):
        return
    pv= partition(a, L, R)
    quicksort(a, L, pv)
    quicksort(a, pv+1,R)
def partition(a, L, R):
    pv= pivot = a[random.randint(L, R)]
    i=L-1
    j=R+1
    while True:
        while True:
            i+=1
            if a[i]>=pv: 
                break
        while True:
            j-=1
            if a[j]<=pv:
                break
        if i>=j:
            return j
        a[i], a[j] = a[j], a[i]
def merge(a,L, M, R):
    A=a[L:M+1]
    B=a[M+1:R+1]
    # n=M-L+1
    # m=R-M
    # for i in range(0, n):
    #     A.append(a[L+i])
    # for j in range(0, m):
    #     B.append(a[M+1+j])
    i=j=0
    k=L
    while i<len(A) and j<len(B):
        if A[i]>B[j]:
            a[k]= A[i]
            i+=1
        else:
            a[k]=B[j]
            j+=1
        k+=1
    while i<len(A):
        a[k]= A[i]
        k+=1
        i+=1
    while j<len(B):
        a[k]=B[j]
        k+=1
        j+=1


def merge_sort(a, L, R):
    if(L>=R):
        return
    mid= L+(R-L)//2
    merge_sort(a, L, mid)
    merge_sort(a, mid+1, R)
    merge(a, L, mid, R)