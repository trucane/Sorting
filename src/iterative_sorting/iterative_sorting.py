# TO-DO: Complete the selection_sort() function below
arraysss = [5,4,10,9,15,8,7]
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
       
        for j in range (i, len(arr)):
            if arr[smallest_index] > arr[j]:
                smallest_index = j

        # TO-DO: swap

        arr[i], arr[smallest_index] = arr[smallest_index], arr[i]


    return arr
selection_sort(arraysss)
print(selection_sort(arraysss))


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    x = len(arr)

    for check_num in range(0, x):
        for i in range(0, x - check_num - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]


    return arr

print(bubble_sort([4,5,39,34,22,11,2]))

# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr