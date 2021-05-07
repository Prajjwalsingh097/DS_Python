def mergeSort(arr,key,descending):
    if len(arr)<=1:
        return arr

    mid=len(arr)//2
    left=arr[0:mid]
    right=arr[mid:]
    mergeSort(left,key,descending)
    mergeSort(right,key,descending)
    
    mergeSort2Arrays(left,right,key,arr,descending)

def mergeSort2Arrays(left,right,key,arr,descending):

    lenA=len(left)
    lenB=len(right)
    i=j=k=0

    while i<lenA and j <lenB:

        if left[i][key]<=right[j][key]:
            arr[k]=left[i]
            i+=1
        else:
            arr[k]=right[j]
            j+=1

        k+=1
    while i<lenA:
        arr[k]=left[i]
        i+=1
        k+=1
    while j<lenB:
        arr[k]=right[j]
        j+=1
        k+=1
        

arr=[
    {'name':'Prajjwal','age':23},
    {'name':'Govind','age':27},
    {'name':'Sotu','age':25},
    {'name':'Motu','age':26},
    {'name':'Riya','age':20},
    {'name':'Sutku','age':24}
    ]

key='age'
descending=True
mergeSort(arr,key,descending)

for x in arr:
    print(x)
