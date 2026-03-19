A* Algorithm for UGV Path Planning

Overview

This project implements the **A* (A-Star) Algorithm** for an **Unmanned Ground Vehicle (UGV)** navigating a battlefield grid.

The UGV finds the **shortest path from a start node to a goal node** while avoiding obstacles.

Algorithm Idea

A* uses a combination of:

* Actual cost from start → g(n)
* Estimated cost to goal → h(n)

Evaluation function:

This makes A* faster than Dijkstra by guiding the search toward the goal.

Environment

* Grid size: 70 × 70
* Cells represent terrain
* Obstacles are randomly generated

 Obstacle Density Levels

* Low: 10%
* Medium: 25%
* High: 40%

Features

* Grid-based path planning
* Obstacle avoidance
* Random obstacle generation
* Shortest path computation
* Supports dynamic replanning (basic version)

Input

* Start position (x, y)
* Goal position (x, y)
* Grid with obstacles

Output

* Shortest path from start to goal
* Path coordinates
* Performance metrics

Measures of Effectiveness (MOE)

* Path Length
* Computation Time
* Nodes Expanded
* Success Rate
* Optimality

Dynamic Obstacles Extension

In real-world scenarios, obstacles may change.

Solutions:

* Replanning A*
* D* Lite algorithm

Advantages

* Faster than Dijkstra
* Heuristic-guided search
* Suitable for robotics

Limitations

* Requires good heuristic
* May degrade if heuristic is poor

Complexity

* Time: O(E) (depends on heuristic)
* Space: O(V)

Applications

* Robotics (UGV navigation)
* Game AI pathfinding
* Autonomous vehicles

Author

Shloka
