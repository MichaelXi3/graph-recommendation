import time
from utils.file_operations import edgelist_to_adjlist, write_recommendations_to_file


def adjac_list_recommend(adj_list):
    # step 1: ensure all vertices are in adj_list, even the vertices without outgoing edges
    all_vertices = set(adj_list.keys())
    for neighbors in adj_list.values():
        all_vertices.update(neighbors)
    
    for vertex in all_vertices:
        if vertex not in adj_list:
            adj_list[vertex] = []

    # step 2: count all two-paths in G and store in dict
    # - key: two path (u, i), value: number of two paths between u, i
    two_paths = get_two_path_dict(adj_list)


    # step 3: turn two-paths dict into adjlist representation of weighted graph
    weighted_graph = get_two_path_weighted_graph(two_paths)
                    
    # step 4: based on the two-path weighted graph, get recommendation of each vertices
    # - key: vertex u, value: recommendation for u
    recomendation = get_recommendation_dict(weighted_graph, adj_list)

    return recomendation


def get_two_path_weighted_graph(two_paths):
    adj_list_weighted = {}

    for pair, count in two_paths.items():
        u, v = pair

        # Add edge from u to v with weight count
        if u not in adj_list_weighted:
            adj_list_weighted[u] = [(v, count)]
        else:
            adj_list_weighted[u].append((v, count))

    return adj_list_weighted
        

def get_recommendation_dict(weighted_graph, adj_list):
    recommendation = {}

    # find recommendation result for all vertices in G
    for u in sorted(adj_list.keys()):
        max_num_two_paths = 0
        recommendation_result = 0
        # if current vertex has two-paths
        if u in weighted_graph and weighted_graph[u] is not None:
            # traverse all u's two-paths neighbors, keep the max weighted one
            for neighbor, weight in sorted(weighted_graph[u]):
                # break tie by choosing smallest index
                if weight > max_num_two_paths:
                    max_num_two_paths = weight
                    recommendation_result = neighbor
            
        recommendation[u] = recommendation_result
    
    return recommendation
        

def get_two_path_dict(adj_list):
    two_paths = {}

    for u in adj_list:
        # u's neighbors
        for v in adj_list[u]:
            # v's neighbors
            for i in adj_list[v]:
                # vertex two hops away is not
                # 1. not same as u
                # 2. not directly connect to u
                if (u != i and i not in adj_list[u]):
                    if (u, i) in two_paths:
                        two_paths[(u, i)] += 1
                    else:
                        two_paths[(u, i)] = 1
    return two_paths



def main():
    # run recommendation in A16
    adj_list_small = edgelist_to_adjlist("./files/A16-edge.txt")

    start_time = time.time()
    recommendation_small = adjac_list_recommend(adj_list_small)
    end_time = time.time()

    print(f"A16 (AdjList) Execution time: {end_time - start_time:.8f} seconds")
    write_recommendations_to_file(recommendation_small, "t-rec16_list.txt")

    # run recommendation in A1024
    adj_list_large = edgelist_to_adjlist("./files/A1024-edge.txt")

    start_time = time.time()
    recommendation_large = adjac_list_recommend(adj_list_large)
    end_time = time.time()

    print(f"A1024 (AdjList) Execution time: {end_time - start_time:.8f} seconds")
    write_recommendations_to_file(recommendation_large, "t-rec1024_list.txt")


if __name__ == "__main__":
    main()
    
