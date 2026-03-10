import numpy as np

def matrix_transpose(A):
    """
    Return the transpose of matrix A (swap rows and columns).
    """
    # Write code here
    M,N= np.array(A).shape

    result=np.zeros((N,M))

    for i in range(M):
        for j in range(N):
            result[j][i] = A[i][j]

    return result
