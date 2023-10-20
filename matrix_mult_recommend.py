import time
import numpy as np
from utils.matrix_mult import matrix_mult
from utils.file_operations import matrix_to_npmatrix, write_recommendations_to_file


def matrix_recommend(A):
    # get the two paths matrix by A*A
    B = matrix_mult(A, A)
    print(B)

    # get the recommendation dict
    recommendation = parse_matrix_to_get_recommendations(A, B)

    return recommendation


def parse_matrix_to_get_recommendations(A, B):
    recommendation = {}
    number_of_vertices = len(A)

    for u in range(1, number_of_vertices + 1):
      max_two_paths = 0
      recommended_vertex = 0
      for v in range(1, number_of_vertices + 1):
        if u != v and A[u - 1][v - 1] == 0 and B[u - 1][v - 1] > max_two_paths:
           max_two_paths = B[u - 1][v - 1]
           recommended_vertex = v

      recommendation[u] = recommended_vertex
    
    return recommendation


def main():
    # run recommendation in A16
    matrix_small = matrix_to_npmatrix("./files/A16.txt")

    start_time = time.time()
    recommendation_small = matrix_recommend(matrix_small)
    end_time = time.time()

    print(f"A16 (matrix) Execution time: {end_time - start_time:.8f} seconds")
    write_recommendations_to_file(recommendation_small, "rec16_matrix.txt")

    # run recommendation in A1024
    matrix_large = matrix_to_npmatrix("./files/A1024.txt")

    start_time = time.time()
    recommendation_large = matrix_recommend(matrix_large)
    end_time = time.time()

    print(f"A1024 (matrix) Execution time: {end_time - start_time:.8f} seconds")
    write_recommendations_to_file(recommendation_large, "rec1024_matrix.txt")

    with open("matrix_1024_time", 'w') as f:
        f.write(f"A1024 (matrix) Execution time: {end_time - start_time:.8f} seconds\n")
    

if __name__ == "__main__":
    main()
    

    
