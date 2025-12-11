#include <fstream>
#include <vector>
#include <string>
#include <unordered_map>
#include <utility>
#include <queue>

typedef std::unordered_map<std::string, std::vector<std::string>> Graph;
typedef std::unordered_map<std::string, int> InDegreeMap;

std::pair<Graph, InDegreeMap> get_input(char* file_name);
int64_t getPaths(const Graph& graph, 
    InDegreeMap in_degree, 
    const std::string& start, const std::string& end);
