def merge_sort(arr):
    if(len(arr)>1):
        m = len(arr)//2
        L = arr[:m]
        R = arr[m:]
        merge_sort(L)
        merge_sort(R)
        i=j=k=0
        while(i<len(L) and j<len(R)):
            if(L[i]<R[j]):
                arr[k]=L[i]
                i+=1
            else:
                arr[k]=R[j]
                j+=1
            k+=1
        while(i<len(L)):
            arr[k]=L[i]
            i+=1
            k+=1
        while(j<len(R)):
            arr[k]=R[j]
            j+=1
            k+=1
    return arr
arr = [55,76,1,5,76,99,22]
print(merge_sort(arr))
