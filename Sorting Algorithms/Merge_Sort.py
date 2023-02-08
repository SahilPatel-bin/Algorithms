def merge(arr,left,mid,right):
    n1 = mid-left+1
    n2 = right-mid
    leftArr = []
    RightArr = []
    for i in range(n1):
        leftArr.append(arr[left+i])
    for j in range(n2):
        RightArr.append(arr[mid+1+j]) 
    
    i = 0
    j = 0
    k = left
    while(i<n1 and j<n2):
        if leftArr[i]<RightArr[j]:
            arr[k]   = leftArr[i]
            i+=1 
        else :
            arr[k] = RightArr[j]
            j+=1
        k+=1

    while(i<n1):
        arr[k] = leftArr[i]
        i+=1
        k+=1

    while(j<n2):
        arr[k] = RightArr[j]
        j+=1
        k+=1
    
def mergeSort(arr,left,right) :
    if left>=right :
        return ;
    mid = (left+right)//2
    mergeSort(arr,left,mid)
    mergeSort(arr,mid+1,right)
    merge(arr,left,mid,right)

length = int(input("enter the length of Array:- "))
arr = []

for i in range(length):
    arr.append(int(input(f"Enter the {i+1} element value:- ")))

mergeSort(arr,0,len(arr)-1)

print("\nAfter Applying Sorting Algorithm:- ")
for index,value in enumerate(arr,start=0):
  print(f"arr[{index}] = {value}")
