def partition(arr,start, end):

    # Let Suppose the Input Elements (Array)
    
    # [11,5,3,7,92,2,55,1]
    #  ^
    # (PivotIndex : 0)   
    # (Pivot is element at 0th Index
    # 11
    
    # [11,5,3,7,92,2,55,1]
    #     ^
    #     (Start : PivotIndex+1) means   1
    #     (Values indexing start should be lesser then Pivot Data
    
    
    # [11,5,3,7,92,2,55,1]
    #                   ^
    #                   End : Last element of Array 
    #                   (End(Indexs) Should Gretter them Pivot  )   

   
    
    pivotIndx=start
    pivot=arr[pivotIndx]
    while start<end:

        while start<(len(arr)) and pivot>=arr[start]:
            start+=1

        while pivot<arr[end] and end > 0:
            end-=1

        if start<end:
            # It wull swap the start(index) with the end(index)
            arr[start],arr[end]=arr[end],arr[start]

    # And at the end when start>end (like what Happens
    # Start is gone one step more then the end index
    # Or we can say end is less then start(index)
    # Then We swap the pivot with the end index
    # Just to ensure that the elements in theright side of
    # Pivot is gretter then Pivot element
    # And the left side elements are lesser then Pivot

    arr[pivotIndx],arr[end]=arr[end],arr[pivotIndx]

    # [2, 5, 3, 7, 1, 11, 55, 92]
    #                 ^
    #                 |
    #        Pivot Element 

    return end
    
    

def QuickSort(arr,start,end):

    # It was nothing but the End index where the Pivot is placed Now
    
    if start<end:
        partitionIndex=partition(arr,start,end)
        # For the Left Side Partition(Or Pivot Smaller) upto the index-1 then Pivot Element
        QuickSort(arr,start,partitionIndex-1)

        # For the right side of Pivot data
        QuickSort(arr,partitionIndex+1,end)

    
    
    return arr


arr=[11,5,3,7,92,2,55,1]
print(QuickSort(arr,0,len(arr)-1))
