__author__ = 'george'




def binarySearch(a, start,  end,  target):

    middle = (start + end) / 2;

    if(end < start):
        return -1;
    if(target==a[middle]):
        return middle;
    elif(target<a[middle]):
        return binarySearch(a, start, middle - 1, target);
    else:
        return binarySearch(a, middle + 1, end, target);

if __name__== '__main__':
    a=[0,1,2,3,4,5,6,7,8]
    print binarySearch(a,0,len(a)-1,9)