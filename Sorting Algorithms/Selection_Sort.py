length = int(input("enter the length of Array:- "))
arr = []

for i in range(length):
    arr.append(int(input(f"Enter the {i+1} element value:- ")))

for i in range(length-1):
  minIndex = i
  for j in range(i+1,length):
    if (arr[j]<arr[minIndex]):
      minIndex = j

  if (minIndex!=i):
    temp = arr[i]
    arr[i] = arr[minIndex]
    arr[minIndex] = temp

print("After Applying Sorting Algorithm:- ")
for index,value in enumerate(arr,start=0):
  print(f"arr[{index}] = {value}")
