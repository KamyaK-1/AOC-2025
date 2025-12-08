#include "common.h"

UnionFind::UnionFind(int nodes){
    parent.resize(nodes);
    component_size.resize(nodes,1);
    std::iota(parent.begin(), parent.end(), 0);
}

bool UnionFind::add_edge(int node1, int node2){
    node1 = find(node1);
    node2 = find(node2);
    if (node1 == node2)
        return false;
    if (component_size[node1] > component_size[node2])
        std::swap(node1, node2);

    parent[node1] = node2;
    component_size[node2] += component_size[node1];

    return true;
}

int UnionFind::num_components(){
    int components = 0;
    for (std::size_t i = 0 ; i < parent.size() ; i++){
        components += (parent[i] == i);
    }   
    return components;
}

std::vector<int> UnionFind::get_component_sizes(){
    std::vector<int> sizes;
    for (std::size_t i = 0 ; i < parent.size() ; i++){
        if (parent[i] == i)
            sizes.push_back(component_size[i]);
    }
    return sizes;
}

int UnionFind::find(int node){
    if (parent[node] == node)
        return node;
    return parent[node] = find(parent[node]);
}



int64_t distance_squared(std::vector<int> point1, std::vector<int> point2){
    int64_t d_squared = 0;
    for (std::size_t i = 0; i < point1.size() ; i++){
        d_squared += static_cast<int64_t> (point1[i] - point2[i]) * (point1[i] - point2[i]);
    }
    return d_squared;
}
