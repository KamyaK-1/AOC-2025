#include "common.h"

int main()
{
    std::ifstream fs;
    fs.open("input.txt",std::fstream::in); 

    std::vector<std::vector<int> > points;
    std::string inp, coordinate;
    while (fs >> inp){
        points.emplace_back();
        std::stringstream ss(inp);
        while (std::getline(ss,coordinate,','))
        {
            points.back().push_back(std::stoi(coordinate));
        }
    }

    UnionFind graph(points.size());
    std::vector<std::array<int64_t,3> > edges;
    for (int64_t i = 0 ; i < points.size() ; i++){
        for (int64_t j = i + 1 ; j < points.size(); j++){
            edges.push_back(std::to_array({distance_squared(points[i],points[j]),i,j}));
        }
    }

    std::sort(edges.begin(), edges.end());
    edges.resize(1000);

    for (const auto& edge : edges){
        graph.add_edge(edge[1], edge[2]);
    }

    auto component_sizes = graph.get_component_sizes();
    std::sort(component_sizes.begin(), component_sizes.end(), std::greater());
    std::cout << component_sizes[0] * component_sizes[1] * component_sizes[2] << std::endl;

    return 0;
}