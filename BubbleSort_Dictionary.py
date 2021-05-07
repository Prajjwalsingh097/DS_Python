
def BubbleSort(arr, key, itr):

    size=len(arr)
    
    
    for i in range(size-1):
        flag=False
        for j in range(size-1-i):
            itr=itr+1
            if arr[j][key]>arr[j+1][key]:
                tmp=arr[j][key]
                arr[j][key]=arr[j+1][key]
                arr[j+1][key]=tmp
                flag=True
        if not flag:
            break
    
    
    print("\n\n Total Iterations : ",itr)
    return itr
    




arr=[
    {'name':'Prajjwal','transactionAmount':1000,'device':'IPhone-8'},
    {'name':'Riya','transactionAmount':300,'device':'Nokia-5'},
    {'name':'Sotu','transactionAmount':900,'device':'Blackberry-8'},
    {'name':'Abhi','transactionAmount':100,'device':'Samsung-A5'},
    ]
itr=0


print(f"\n\n\t---------Array Data As Input--------------")

for x in arr:
    print("\n\n\t : ",x)


key=input("\n\t : Enter Key : ") 

BubbleSort(arr,key,itr)

print(f"\n\n\t---------Array Data After Sort on Key : '{key}' Basis--------------")

for x in arr:
    print("\n\n\t : ",x)
