# Two-Paths Graph Recommendation

This project contains a recommendation system based on the principle of transitivity. It operates on both adjacency lists and matrix representations of graphs.

## Overview

The recommendation operates in two modes:

1. **Adjacency List Mode**: This mode processes the graph represented as an adjacency list.
2. **Matrix Mode**: This mode processes the graph represented as a matrix.

The system recommends nodes based on the weights of their connections to other nodes.

## Compilation Instructions

```python
python3 adjace_list_recommend.py 
python3 matrix_mult_recommend.py 
```

## File Descriptions

- **adjace_list_recommend.py**: Contains the functions to run the recommendation for graph adjacency list representations.
- **matrix_mult_recommend.py**: Contains the functions to run the recommendation for graph matrix representations.
- **utils.py**: Contains utility functions to help in processing and recommendations.
- **/files/**: Directory containing the sample graph files.

## Result

### Time Comparison Between the Matrix and List Methods

```
A16 (adList) Execution time: 0.00013399 seconds
A16 (matrix) Execution time: 0.02661300 seconds
```

```
A1024 (adList) Execution time: 0.17569900 seconds
A1024 (matrix) Execution time: 6417.33650184 seconds
```

The adjacency list has a much lower time complexity compared to the matrix method. The time complexity of the matrix algorithm is `O(n^3)`. On the other hand, though the upper bound time complexity of the adjacency list method is `O(n^3)` (`O(n * d * d)`), this upper bound is very unlikely, as it represents a scenario where all vertices are connected to all other vertices, resulting in a very dense graph. For example, in A1024-edge data, most vertices have an out-degree around d equals 5, and n equals1024, so the `O(n * d * d)` is far less than `O(n^3)`.

### Recommendation based on word.txt

As an example of recommendation, the algorithm recommend word_1 to word_4.

```
1 → 4
existence → unsubstantiality
```

The two path between word_1 to word_4 is 1 to 2 to 4.

```
1 → 2 → 4
existence → inexistence → unsubstantiality
```

The recommendation is meaningful because existence is related to nonexistence, as they are counterparts of each other. Similarly, nonexistence is related to unsubstantiality, as both words convey a sense of discontinuity.

