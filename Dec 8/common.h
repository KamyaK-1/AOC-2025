#include<fstream>
#include<iostream>
#include<vector>
#include<array>
#include<sstream>
#include<numeric>
#include<algorithm>

class UnionFind{

public:
    UnionFind(int nodes);
    bool add_edge(int node1, int node2);
    int num_components();
    std::vector<int> get_component_sizes();
private:
    std::vector<int> parent;
    std::vector<int> component_size;
    int find(int node);
};
int64_t distance_squared(std::vector<int> point1, std::vector<int> point2);