def selectionSort(arr):

    size=len(arr)-1

    for i in range(size+1):
        minVal=arr[i]
        minIndx=i
        for j in range(i+1,size+1):
            if minVal>arr[j]:
                minVal=arr[j]
                minIndx=j

        if minIndx!=i:
            arr[i],arr[minIndx]=arr[minIndx],arr[i]

    return arr

print(selectionSort([3,6,1,2,9,0]))
