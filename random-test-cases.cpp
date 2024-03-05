#include <filesystem>
#include <random>
#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int main(int argc, char* argv[]) {
    random_device rd;
    linear_congruential_engine<uint_fast32_t, 48271, 0, 2147483647> rng;
    rng.seed(rd());
    int numbers = stoi(argv[1]);
    filesystem::remove("input.txt");
    ofstream inp("input.txt");
    inp << numbers << endl;
    for (int i = 0; i < numbers; i++) {
        inp << rng() << endl;
    }
    inp.close();
}


