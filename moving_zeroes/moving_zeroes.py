'''
Input: a List of integers
Returns: a List of integers
'''


def moving_zeroes(arr):
    # Your code here
    # pass
    count = 0
    for i in arr:
        # print(i)
        if i:
            arr[count] = i
            count += 1

    for i in range(count, len(arr)):
        arr[i] = 0

    return arr


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    #arr = [0, 3, 1, 0, -2]
    arr = [0, 0, 0, 0, 3, 2, 1]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")
