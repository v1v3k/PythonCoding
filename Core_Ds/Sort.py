__author__ = 'george'
import random


def quicksort(A,low,high):
    if low <high:
        pivot = partiton(A,low,high)
        quicksort(A,low,pivot-1)
        quicksort(A,pivot+1,high)


def partiton(A,low,high):
    pivot =low
    swap(A,pivot,high)
    for i in range(low,high):
        if A[i]<=A[high]:
            swap(A,i,low)
            low +=1
    swap(A,low,high)
    return low


def swap(A,pivot,high):
    temp =A[pivot]
    A[pivot]=A[high]
    A[high]= temp



def selectionsort(A):
    for i in range(len(A)):
        temp =i
        for k in range(i+1,len(A)):
            if A[temp]> A[k]:
                temp =k
        swap(A,temp,i)
    #print A

def BubbleSort(A):
    for i in range(len(A)-1):
        for j in range(len(A)-i-1):
            if A[j]>A[j+1]:
                temp=A[j]
                A[j]=A[j+1]
                A[j+1]=temp
    print A

def InsertionSort(A):
    for i in range(1,len(A)):
        temp= A[i]
        k=i
        for j in range(k,0,-1):
            if temp < A[j-1]:
                A[j]=A[j-1]
            else:
                break
        A[j] = temp
    print A



def mergesort(A):
    if len(A)>1:
        mid= len(A)//2
        lefthalf=mergesort(A[0:mid])
        righthalf=mergesort(A[mid:len(A)])
        A = merge(lefthalf,righthalf,len(A))
        return A
    else:
        return A

def merge(lefthalf,righthalf,l):
    i=j=k=0
    A=[]
    while i<len(lefthalf) and j<len(righthalf):

        if lefthalf[i]<righthalf[j]:
            A.append(lefthalf[i])
            i+=1
            k+=1

        elif lefthalf[i]>=righthalf[j]:
            A.append(righthalf[j])
            j+=1
            k+=1

    while i<len(lefthalf):
        A.append(lefthalf[i])
        i+=1
    while j<len(righthalf):
        A.append(righthalf[j])
        j+=1

    return A

if __name__== '__main__':
    A = [2,3,2,9,5,1]
    #InsertionSort(A)
    print mergesort(A)









'''
A = [2,3,2,9,5,1]
quicksort(A,0,len(A)-1)
print A
A = [2,3,2,9,5,1]
selectionsort(A)
print A
A = [2,3,2,9,5,1]
BubbleSort(A)
print A

'''