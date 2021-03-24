# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    # elements = len( arrA ) + len( arrB )
    # merged_arr = [0] * elements
    # # TO-DO
    merged_arr = arrA + arrB
    
    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # base
    if len(arr) < 1:
        return arr
    else:
    # separate array in 2
        half = len(arr) // 2
        left = arr[:half]
        right = arr[half:]

    return arr

listTest = [5, 1, 8, 4, 7, 8, 3, 9, 2]
merge_Sorted = merge_sort(listTest)

# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
