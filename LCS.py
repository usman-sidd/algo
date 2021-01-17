def LCSLength(X, Y, m, n):
 
    # return if we have reached the end of either sequence
    if m == 0 or n == 0:
        return 0
 
    # if last character of X and Y matches
    if X[m - 1] == Y[n - 1]:
        return LCSLength(X, Y, m - 1, n - 1) + 1
 
    # else if last character of X and Y don't match
    return max(LCSLength(X, Y, m, n - 1), LCSLength(X, Y, m - 1, n))
 
 
if __name__ == '__main__':
 
    X = "ABCBDAB"
    Y = "BDCABA"
 
    print("The length of LCS is", LCSLength(X, Y, len(X), len(Y)))