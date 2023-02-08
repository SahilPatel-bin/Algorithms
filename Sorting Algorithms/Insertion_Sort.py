length = int(input("enter the length of Array:- "))
arr = []

for i in range(length):
    arr.append(int(input(f"Enter the {i+1} element value:- ")))

for i in range(1,length):
  j = i
  while(j>0 and arr[j-1]>arr[j]):
    temp = arr[j]
    arr[j] = arr[j-1]
    arr[j-1] = temp
    j-=1

print("\nAfter Applying Sorting Algorithm:- ")
for index,value in enumerate(arr,start=0):
  print(f"arr[{index}] = {value}")
