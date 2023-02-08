length = int(input("enter the length of Array:- "))
arr = []

for i in range(length):
    arr.append(int(input(f"Enter the {i+1} element value:- ")))

for i in range(length-1):
  flag = False
  for j in range(0,length-i-1):
    if arr[j]>arr[j+1] :
      temp = arr[j]
      arr[j] = arr[j+1]
      arr[j+1] = temp
      flag = True

  if (not flag) :
    break

print("After Sort array:- ")
for index,value in enumerate(arr,start=0):
  print(f"arr[{index}] = {value}")
