#include<iostream>
#include<fstream>
using namespace std;

long long checkRange(long long startRange, long long endRange)
{
    long long invalidIDSum = 0;
    for (long long val = startRange ; val <= endRange ; val++)
    {
        std::string s = std::to_string(val);
        std::size_t len = s.length();
        bool idInvalid = false;
        for (std::size_t repeatingPatternSize = 1 ; repeatingPatternSize < s.length() && !idInvalid; repeatingPatternSize++)
        {
            if (len % repeatingPatternSize == 0)
            {
                bool repeating = true;
                std::size_t numPatterns = len / repeatingPatternSize;
                for (std::size_t patternNum = 1 ; patternNum < numPatterns ; patternNum++)
                {
                    for (std::size_t idx = 0 ; idx < repeatingPatternSize && repeating; idx++)
                        if (s[patternNum * repeatingPatternSize + idx] != s[idx])
                            repeating = false;
                }
                if (repeating)
                    idInvalid = true;
            }
        }
        if (idInvalid)
            invalidIDSum += val;

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

    fs.close();
    return 0;    
}