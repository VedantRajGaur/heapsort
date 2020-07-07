def heapify(arr,n,parent):
    lar=parent
    left=2*parent+1
    right=2*parent+2

    if left<n and arr[parent]<arr[left]:
      lar=left
    if right<n and arr[lar]<arr[right]:
      lar=right

    if lar!=parent:
      temp=arr[parent]
      arr[parent]=arr[lar]
      arr[lar]=temp
      heapify(arr,n,lar)


def hSort(arr):
    n=len(arr)
    for i in range(n//2-1,-1,-1):
      heapify(arr,n,i)
    for j in range (n-1,0,-1):
      temp=arr[j]
      arr[j]=arr[0]
      arr[0]=temp
      heapify(arr,j,0)

def m():
    arr=[]
    n=int(input("Enter the size of array:"))
    print("Enter the elements of the array:")
    for i in range(n):
      num=int(input())
      arr.append(num)
    hSort(arr)
    print("The sorted array:")
    for i in range(n):
      print(str(arr[i]))
 
m()
