# a = [1,2,3]
# print(a)
# print("type of a is "+ str(type(a)))

# #List comprehension
# a= [i for i in range(31)]
# print(a)
# #####################
# a=[i for i in range(21)]
# print(a)
# #####################
# a=[i for i in range(21) if i%2==0]
# print(a)
# #####################
# a=[(x,y) for x in range(0,11) for y in range(0,x+1)]
# print(a)
# iterable 
# a=list("Hello Tuấn Duy")
# print(a)
# Data Structure List
# a=[1,2,6,1]
# print(a)
# append(x): them x vao cuoi danh sach
# a.append(1)
# print(a)
#extend(list): noi 2 list lai voi nhau, khong can dung loop+ append
#insert(i,x): chen x tai vi tri i
# a.insert(0,3)
# print(a)
#remove(x): xoa phan tu x dau tien vua gap
# a.remove(1)
# print(a)
#reverse(): dao nguoc list
# x in <list>: kiem tra ton tai
# not <list>: kiem tra co rong khong, 
# True neu rong, False neu khong rong
# print(not a)
#b=a.copy(): copy list a vao b
#khi b thay doi thi a khong bi anh huong

#Sử dụng list như stack

# stack=[3,2,1,6]
# print(stack)
#pop(): lay phan tu o cuoi, phan tu vao sau
#vao sau ra truoc
# print(stack.pop())
# print(stack)
#dung append()

#Sử dụng list như queue
# from collections import deque
# queue= deque([2,3,5,7,9])
# print(queue)

#append(x): Chen phan tu vao cuoi hang doi
#list.popleft(): lay phan tu o dau hang doi
# print(queue.popleft())
# print(queue)


#sap xep bang merge sort
def merge(A, left ,mid, right):
    L=A[left:mid+1]
    R=A[mid+1: right+1]
    i=j=0
    k=left
    #gop 2 mang lai
    while i<len(L) and j<len(R):
        if L[i]<=R[j]:
            A[k]=L[i]
            i+=1
        else:
            A[k]=R[j]
            j+=1
        k+=1
    #them cac phan con lai
    while i<len(L):
        A[k]=L[i]
        i+=1
        k+=1
    while j<len(R):
        A[k]=R[j]
        j+=1
        k+=1  

def mergeSort(A,L,R):
    if L<R:
        M=L+(R-L)//2
        mergeSort(A,L,M)
        mergeSort(A,M+1, R)  
        merge(A,L,M,R)  

A=[2,7,1,3,67,8,2]
print(A)
mergeSort(A,0,len(A)-1)
print(A)