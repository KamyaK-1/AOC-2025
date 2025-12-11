#include "common.h"

std::pair<Graph, InDegreeMap> get_input(char* file_name)
{
    std::ifstream fs(file_name);
    Graph graph;
    InDegreeMap in_degree;
    std::string line, start;

    fs >> line;
    do
    {   
        start = line;
        start.pop_back();
        graph[start] = std::vector<std::string>();
        while (fs >> line && line.back() != ':'){
            graph[start].push_back(line);
            in_degree[line]++;
        }
    } while (line.find(':') != std::string::npos);

    return std::make_pair(graph, in_degree);
}

int64_t getPaths(const Graph& graph, 
    InDegreeMap in_degree, 
    const std::string& start, const std::string& end)
{
    std::unordered_map<std::string, int64_t> paths_from_start;
    std::queue<std::string> queue;
    
    paths_from_start[start] = 1;
    for (const auto& [node, _] : graph) {
        if (in_degree[node] == 0) {
            queue.push(node);
        }
    }

    while (!queue.empty()) {
        std::string current = queue.front();
        queue.pop();
        if (graph.find(current) == graph.end()) {
            continue;
        }
        for (const auto& neighbor : graph.at(current)) {
            paths_from_start[neighbor] += paths_from_start[current];
            in_degree[neighbor]--;
            if (in_degree[neighbor] == 0) {
                queue.push(neighbor);
            }
        }
    }

    return paths_from_start[end];

}