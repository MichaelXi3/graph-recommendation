import numpy as np

# read edge list file and parse into adj_list
def edgelist_to_adjlist(file_path):
    adjlist = {}

    with open(file_path, 'r') as f:
        for line in f:
            u, v = map(int, line.split())

            if u not in adjlist:
                adjlist[u] = []
            adjlist[u].append(v)

    return adjlist


# read matrix file and parse into np matrix
def matrix_to_npmatrix(file_path):
  with open(file_path, 'r') as f:
    matrix = np.array(
        [list(map(int, line.split())) for line in f]
    )
    return matrix
  

# write recommendation dict results into an output file
def write_recommendations_to_file(recommendations, output_filename):
    if recommendations is None:
        print("Error: Recommendations is None.")
        return
    with open(output_filename, 'w') as f:
        for item, recommended_item in recommendations.items():
            f.write(f"{recommended_item}\n")