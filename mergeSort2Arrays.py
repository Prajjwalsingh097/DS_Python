def mergeSort(arr):
    if len(arr)<=1:
        return arr

    mid=len(arr)//2
    left=arr[:mid]
    right=arr[mid:]

    mergeSort(left)
    mergeSort(right)


    mergeSort2Arrays(left,right,arr)




# It only works on sorted Array 
def mergeSort2Arrays(a,b,arr):

    lenA=len(a)
    lenB=len(b)

    # Make two indexs for comparision
    i=j=k=0
    # i for left array(a)
    # j for rigth array(b)
    # k for index of arr(from 0 to len(arr))

    while i<lenA and j<lenB:
        if a[i]<=b[j]:
            # Suppose [1,2,4,6] in a 
            #sortedArray.append(a[i])
            arr[k]=a[i]
            i+=1
        else:
            # Suppose [3,5,7,9] in n
            #sortedArray.append(b[j])
            arr[k]=b[j]
            j+=1
        k+=1

    while i<lenA:
        arr[k]=a[i]
        i+=1
        k+=1

    while j<lenB:
        arr[k]=b[j]
        j+=1
        k+=1

    
        

'''
# Only for sorted Arrays (a and b)

a=[1,2,4,6]


b=[3,5,7,9]


print(mergeSort2Arrays(a,b))
'''


arr=[
    [4,3,2,7,59,1,33,20],
    [],
    [59,1,33,20,2,1,0],
    [1,2,3,5],
    [9,7,5,4,2,1]
    ]

for x in arr:
        
    mergeSort(x)

    print(x)

