
def BubbleSort(arr, itr):

    size=len(arr)
    
    for i in range(size-1):
        flag=False
        for j in range(size-1-i):
            itr=itr+1
            if arr[j]>arr[j+1]:
                tmp=arr[j]
                arr[j]=arr[j+1]
                arr[j+1]=tmp
                flag=True
        if not flag:
            break
    
    
    print("\n\n Total Iterations : ",itr)
    return itr
    


arr=[15,2,6,1,3,8,11]
itr=0

BubbleSort(arr,itr)

print("\n\n Array ",arr)

