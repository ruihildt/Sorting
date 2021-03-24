# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    for i in range(0, len(arr) - 1):
        smallest_index = i
        temp = arr[i]

        for f in range(i + 1, len(arr)):
            if arr[smallest_index] > arr[f]:
                smallest_index = f

        arr[i], arr[smallest_index] = arr[smallest_index], arr[i]
    return arr

arrTest = [5, 1, 8, 4, 7, 8, 3, 9]
selection_sort_test = selection_sort(arrTest)
# print(selection_sort_test)

# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    swapped = True

    while swapped:
        swapped = False
        for i in range(0, len(arr) - 1):
            # compare if right is bigger than left
            if arr[i] > arr[i+1]:
                # swap
                arr[i], arr[i+1] = arr[i+1], arr[i]
                swapped = True
            # if not, don't swap and compare it to the next one
    return arr

arrTest = [5, 1, 8, 4, 7, 8, 3, 9]
bubble_sort_test = bubble_sort(arrTest)
print(bubble_sort_test)

# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr