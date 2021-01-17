def subsetSum(A, n, sum):
 
    # return true if sum becomes 0 (subset found)
    if sum == 0:
        return True
 
    # base case: no items left or sum becomes negative
    if n < 0 or sum < 0:
        return False
 
    # Case 1. include current item in the subset (A[n]) and recur
    # for remaining items (n - 1) with remaining sum (sum - A[n])
    include = subsetSum(A, n - 1, sum - A[n])
 
    # return true if we get subset by including the current item
    if include:
        return True
 
    # Case 2. exclude current item n from subset and recur for
    # remaining items (n - 1)
    exclude = subsetSum(A, n - 1, sum)
 
    # return true if we get subset by excluding the current item
    return exclude
 
 
# Return true if given list A[0..n-1] can be divided into two
# sublists with equal sum
def partition(A):
 
    total = sum(A)
 
    # return true if sum is even and list can can be divided into
    # two sublists with equal sum
    return (total & 1) == 0 and subsetSum(A, len(A) - 1, total/2)
 
 
if __name__ == '__main__':
 
    # Input: set of items
    A = [7, 3, 1, 5, 4, 8]
 
    print(partition(A))