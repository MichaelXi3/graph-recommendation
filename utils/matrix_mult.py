import numpy as np

# both matrix A and B has dimension n, and n must be the power of 2
def matrix_mult(A, B):
  n = len(A)
  if (n == 1):
    return A * B
  else:
    mid = n // 2;  # make half an int using '//' for slicing
    A11, A12, A21, A22 = A[:mid, :mid], A[:mid, mid:], A[mid:, :mid], A[mid:, mid:]
    B11, B12, B21, B22 = B[:mid, :mid], B[:mid, mid:], B[mid:, :mid], B[mid:, mid:]

    D11 = matrix_mult(A11, B11)
    D12 = matrix_mult(A11, B12)
    D21 = matrix_mult(A21, B11)
    D22 = matrix_mult(A21, B12)
    E11 = matrix_mult(A12, B21)
    E12 = matrix_mult(A12, B22)
    E21 = matrix_mult(A22, B21)
    E22 = matrix_mult(A22, B22)

    R11 = D11 + E11
    R12 = D12 + E12
    R21 = D21 + E21
    R22 = D22 + E22

    return np.vstack((np.hstack((R11, R12)), np.hstack((R21, R22))))