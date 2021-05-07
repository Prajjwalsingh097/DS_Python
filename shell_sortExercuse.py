
def shell_sort(arr):
    set={arr[0]}
    for x in arr:
        set.add(x)
    arr1=[]
    print("The Set : ",set)
    for x in set:
        arr1.append(x)

    arr=arr1
    size=len(arr)
    gap=size//2

    while gap>0:
        for i in range (gap,size):
            anchor=arr[i]
            j=i
            
            while j>=gap and arr[j-gap]>anchor:
                arr[j]=arr[j-gap]
                j-=gap
            arr[j]=anchor


        gap=gap//2

    print(arr)


arr=[5,2,3,1,6,8,1,2,3,4,5,11,54,4]

shell_sort(arr)
