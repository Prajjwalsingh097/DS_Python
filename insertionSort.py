def insertionSort(arr):

    for i in range(1,len(arr)):
        anchor=arr[i]
        j=i-1
        while j>=0 and anchor<arr[j]:
            arr[j+1]=arr[j]
            j=j-1

        arr[j+1]=anchor



arr=[5,3,1,6,7,22,4]

insertionSort(arr)

print(arr)
