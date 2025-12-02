#include<iostream>
#include<fstream>

long long checkRange(long long startRange, long long endRange)
{
    long long invalidIDSum = 0;
    for (long long val = startRange ; val <= endRange ; val++)
    {
        auto s = std::to_string(val);
        if (s.length() % 2 == 0)
        {
            std::size_t n = s.length();
            invalidIDSum += val;
            for (std::size_t i = 0 ; i < n / 2; i++)
            {
                if (s[i] != s[i + n / 2])
                {
                    invalidIDSum -= val;
                    break;
                }
            }   
        }
    }
    return invalidIDSum;
}

int main()
{
    std::ifstream fs;
    fs.open("input.txt",std::fstream::in); 
    std::string inp;
    fs >> inp;
    
    int64_t invalidIDSum = 0;
    std::size_t idx = 0;
    do
    {
        std::size_t nextIdx = inp.find_first_of(',',idx);
        std::size_t sep = inp.find_first_of('-',idx);
        long long l = std::stol(inp.substr(idx,sep - idx));
        long long r = std::stol(inp.substr(sep + 1,nextIdx - sep));
        invalidIDSum += checkRange(l,r);
        idx = nextIdx;
    } while (idx++ != std::string::npos);
    
    std::cout << invalidIDSum << std::endl;

    fs.close();
    return 0;
}