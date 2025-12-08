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
    int64_t xCoord1{}, xCoord2{};

    for (const auto& edge : edges){
        if (graph.num_components() == 1)
            break;
        if (graph.add_edge(edge[1], edge[2]))
        {
            xCoord1 = points[edge[1]][0];
            xCoord2 = points[edge[2]][0];
        }
    }

    std::cout << xCoord1 * xCoord2 << std::endl;

    return 0;
}