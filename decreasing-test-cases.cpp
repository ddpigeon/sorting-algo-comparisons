#include <filesystem>
#include <random>
#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int main(int argc, char* argv[]) {
    random_device rd;
    linear_congruential_engine<std::uint_fast32_t, 48271, 0, 2147483647> rng;
    uniform_int_distribution<int> int_gen(0, 200);
    rng.seed(rd());
    int numbers = std::stoi(argv[1]);
    filesystem::remove("input.txt");
    ofstream inp("input.txt");
    inp << numbers << endl;
    int sum = 200 * numbers;
    for (int i = 0; i < numbers; i++) {
        sum -= int_gen(rng);
        inp << sum << endl;
    }
    inp.close();
}


