Dijkstra’s Algorithm on Indian Cities

Overview

This project implements **Dijkstra’s Algorithm** (also known as **Uniform Cost Search**) to compute the shortest path between Indian cities using road distances.

It guarantees the **optimal shortest path** when all edge costs are non-negative.

Algorithm Idea

Dijkstra expands the node with the **lowest cumulative path cost** from the start node.

The algorithm uses a **priority queue (min-heap)** to always explore the cheapest path first.

Features

* Graph representation of Indian cities and road distances
* Shortest path from a source city to all other cities
* Efficient implementation using Python `heapq`
* Handles weighted graphs

Input

Graph of cities in the format:
```
Delhi Mumbai 1400
Delhi Jaipur 280
Jaipur Ahmedabad 660
```
## 📤 Output
```
Delhi -> Mumbai = 1400 km
Delhi -> Pune = 1550 km
```

Applications

* GPS Navigation Systems
* Network Routing
* Logistics and Transportation

Advantages

* Always finds optimal path
* Works with any non-negative weights

Limitations

* Slower than A* for large graphs
* Does not use heuristics

Complexity

* Time: O(E log V)
* Space: O(V)

Author

Shloka
