def binary_search(list,target):
    start = 0
    end = len(list) - 1
    while start<=end:
        m = (start + end)//2
        if list[m] == target:
            return m
        elif list[m] > target:
            end = m - 1
        else:
            start = m + 1
    return None


a = [1,2,3,4,5]
if binary_search(a,5)==None:
    print("target not found")
else:
    print(f"index of target: {binary_search(a,5)}")

