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

    #variable = length of array 
    x = len(arr)

    for check_num in range(0, x):
        #range is 0 (start) to value of x 
        for i in range(0, x - check_num - 1):
            # for each element in provided array from start(0) to 7-position-1
            if arr[i] > arr[i + 1]:
                #if 1st iteration in array is less than 2nd iteration of array:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                #then swap posotions greater goes to the right then right position goes to the left 


    return arr

print(bubble_sort([4,5,39,34,22,11,2]))

# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr