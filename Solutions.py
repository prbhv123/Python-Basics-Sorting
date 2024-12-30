## Selection Sort Algorithm
The algorithm divides the array into two parts:
1. A sorted part (initially empty).
2. An unsorted part.
3. Repeatedly selects the smallest element from the unsorted part and swaps it with the first element of the unsorted part. 
4. Gradually grows the sorted part while shrinking the unsorted part.

## Solution:
class Solution: 
    def selectionSort(self, arr):
        n = len(arr)
        for i in range(n):
            min_index = i
            for j in range(i+1, n):
                if arr[j] < arr[min_index]:
                    min_index = j
            arr[i],arr[min_index] = arr[min_index],arr[i]
        return arr


## Bubble Sort Algorithm
1. Repeatedly compare adjacent elements in the array.
2. Swap them if they are in the wrong order (i.e., if the first is greater than the second).
3. Continue the process until the array is sorted.

## Solution:
class Solution:
    def bubbleSort(self,arr):
        n = len(arr)
        for i in range(n):
            swapped = False
            for j in range(n-i-1):
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
                    swapped = True
            if not swapped:
                break
        return arr

## Insertion Sort Algorithm
1. Insertion Sort is a simple sorting algorithm that works similarly to how you would sort playing cards in your hand.
2. It builds the sorted array one element at a time by:
  2.1 Picking the next element.
  2.2 Placing it in the correct position in the sorted portion of the array.

## Solution
class Solution:
    def insertionSort(self, arr):
        n = len(arr)
        for i in range(1,n):
            key = arr[i]
            j = i-1
            while (j >= 0 and arr[j] > key):
                arr[j+1] = arr[j]
                j-=1
            arr[j+1] = key
        return arr

## Quick Sort Algorithm
1. The Quick Sort algorithm is a divide-and-conquer sorting technique. 
2. It works by selecting a "pivot" element, partitioning the array around the pivot.
3. Then recursively sorting the subarrays.

## Solution
class Solution:
    def quickSort(self,arr,low,high):
        if low < high:
            pivot_index = self.partition(arr, low, high)
            self.quickSort(arr, low, pivot_index - 1)
            self.quickSort(arr, pivot_index + 1, high)
    def partition(self,arr,low,high):
        pivot = arr[high]
        i = low -1
        for j in range(low,high):
            if arr[j] <= pivot:
                i+=1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1



  
