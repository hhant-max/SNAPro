
#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <sstream>

int main()
{
    std::vector<std::vector<int>> vv;
    std::ifstream infile("/home/sfy/Documents/VScodeProject/SNAPro/Expriment/testComu.txt");
    if (infile.is_open())
    {
        for (std::string line; getline(infile, line);)
        {
            std::vector<int> v;

            int f;                      /* declare int */
            std::stringstream ss(line); /* make stringstream from s */
            while ((ss >> f))           /* read ints from ss into f */
                v.push_back(f);         /* add f to vector */

            vv.push_back(v);
        }
    }
    // {
    //     std::string line;
    //     while (std::getline(infile, line))
    //     {
    //         std::vector<int> v;
    //         // size here is not correct
    //         for (size_t i = 0; i < line.size(); i++)
    //         {
    //             int f;                      /* declare int */
    //             std::stringstream ss(line[i]); /* make stringstream from s */
    //             while ((ss >> f))           /* read ints from ss into f */
    //                 v.push_back(f);         /* add f to vector */
    //         }
    //         vv.push_back(v);
    //     }
    // }
}
// append to text file
// std::stringstream is("0 1 2 3 ");
// std::string s;
// std::vector<int> vec;

// for (auto &i : vec) /* output integers in vector */
//     std::cout << i << '\n';

// show the menu screen

// int main()
// {
//     string s("0 1 2 3 ");
//     vector<int> v(s.begin(), s.end());
//     for (int i =0; i < v.size(); i++){
//         cout << v[i] <<endl;
//     }
// for (int i = 0; i < s.size(); ++i)
// {
//     char h = s[i];
//     cout << h;
// int hi = int(h - '0');
// cout << hi;
// }
// }