def LIS(A, i, n, prev):
 
    # Base case: not hing is remaining
    if i == n:
        return 0
 
    # case 1: exclude the current element and process the
    # remaining elements
    excl = LIS(A, i + 1, n, prev)
 
    # case 2: include the current element if it is greater
    # than previous element in LIS
    incl = 0
    if A[i] > prev:
        incl = 1 + LIS(A, i + 1, n, A[i])
 
    # return maximum of above two choices
    return max(incl, excl)
 
 
# Program for Longest Increasing Subsequence
if __name__ == '__main__':
 
    A = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]
 
    print("Length of LIS is", LIS(A, 0, len(A), float('-inf')))