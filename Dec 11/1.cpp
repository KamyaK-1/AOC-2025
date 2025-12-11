#include "common.h" 
#include <iostream>

int main(int argc, char* args[])
{
    auto [graph, in_degree] = get_input(args[1]);

    std::cout << getPaths(graph, in_degree, "you", "out") << std::endl;

    return 0;
}