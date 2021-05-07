
def BinarySearch(arr, data):
    
    start=0
    end=len(arr)-1
    itr = 0
    while start<=end:
        itr+=1
        midIndx=(start+end)//2

        midData=arr[midIndx]

        if midData==data:
            print(f"\n\t Data Found at Index: {midIndx}\n\t Data :",arr[midIndx])
            return itr

        if midData<data:
            start=midIndx+1
        else:
            end=midIndx-1

    print("Data Not Found ")
    return itr
    


    
        


 

arr=[1,3,4,6,7,9,11,17,21]
itr=0

print("\n\t Raw Data : ",arr)
ind =BinarySearch(arr,19)

print("\n\n\t Total Iteration ",ind)
