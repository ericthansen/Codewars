def binary_array_to_number(arr):
  # your code
    length=len(arr)
    ar2=[None]*length
    count=length-1
    factor=1
    while (count >= 0):
       ar2[count]=arr[count]*factor
       count= count-1
       factor=factor*2
    i=0
    total=0
    while (i<length):
        total=total+ar2[i]
        i=i+1
    return total
print("[0, 0, 0, 1] is ",binary_array_to_number([0, 1, 0, 1]))