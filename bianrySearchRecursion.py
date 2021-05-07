# BinarySearch Using Recursion


def BinarySearch(arr, valueToFind, start, end, itr):
    itr+=1
    if start>end:
        print("\n\n\t Total Recursion : ",itr)
        print("\n\n\t Data Not Found ")
        return -1

    mid=(start+end)//2

    midVal=arr[mid]

    if midVal==valueToFind:
        print("\n\n\t Total Recursion : ",itr)
        print(f"\n\n\t Value Find, at Index {mid} ",arr[mid])
        return mid

    if midVal<valueToFind:
        if mid<end:
            start=mid+1
            return BinarySearch(arr, valueToFind, start, end, itr)
    else:
        if mid>start:
            end=mid-1
            return BinarySearch(arr, valueToFind, start, end, itr)

    return None
            


arr=[1,3,4,6,7,9,11,11,11,11,17,21]
itr=0
print("\n\t Raw Data       : ",arr)
valueToFind=int(input("\n\n\t Enter Data to Find "))
start=0
end=len(arr)-1
print("\n\t Data To Find   : ",valueToFind)
print("\n\t Start of Array : ",start)
print("\n\t End of Array : ",end)

print("\n\n\t Results :- ")

print(f"\n\n\t Binary Search for {valueToFind} ",BinarySearch(arr, valueToFind, start, end, itr))
