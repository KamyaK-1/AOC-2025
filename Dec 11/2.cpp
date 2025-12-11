#include "common.h" 
#include <iostream>

int main(int argc, char* args[])
{
    auto [graph, in_degree] = get_input(args[1]);

    std::cout << getPaths(graph, in_degree, "svr", "dac") * getPaths(graph, in_degree, "dac", "fft") * getPaths(graph, in_degree, "fft", "out") 
        + getPaths(graph, in_degree, "svr", "fft") * getPaths(graph, in_degree, "fft", "dac") * getPaths(graph, in_degree, "dac", "out") << std::endl;

    return 0;
}