__author__ = 'george'

A=[]

N=None

def Binary(n):
    if(n<1):
        print A
    else:
        A[n-1]=0
        Binary(n-1)
        A[n-1]=1
        Binary(n-1)

def nk_prob(n,k):

    if (n<1):
        print A

    else:
        for i in range(k):
            A[n-1]=i
            nk_prob(n-1,k)

if __name__== '__main__':

    print'Eneter N'
    N=int(raw_input())
    A=[None]*N
    K=int(raw_input())

    # N times using 1 - K Problem
    print 'NK Problem set'
    nk_prob(N,K)
    # Binary N times
    print 'Binnary Problem set'
    Binary(N)
