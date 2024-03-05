#include <bits/chrono.h>
#include <iostream>
#include <vector>
#include <random>
#include <fstream>
#include <chrono>
using namespace std;
using ll = long long;

random_device rd;
linear_congruential_engine<std::uint_fast32_t, 48271, 0, 2147483647> rng;

int median(int a, int b, int c) {
    if (a > b) {
        if (b >= c) return b;
        else {
            if (a >= c) return c;
            return a;
        }
    }
    else {
        if (c >= b) return b;
        else {
            if (c >= a) return c;
            return b;
        }
    }
}

int partition(vector<int> &arr, int start, int end, ll &comparisons, int choice) {

    // CHOICE = pivot choice
    // 1 -> first element
    // 2 -> random element
    // 3 -> median of first, last, middle
	int pivot;

    if (choice == 1) pivot = arr[start];
    else if (choice == 2) pivot = arr[start + (rng() % (end - start + 1))];
    else pivot = median(arr[start], arr[end], arr[start + (end-start)/2]);

	int count = 0;
    for (int i = start + 1; i <= end; i++) {
        comparisons++;
		if (arr[i] <= pivot) count++;
	}

	int pivotIndex = start + count;
	swap(arr[pivotIndex], arr[start]);
	int i = start, j = end;
	while (i < pivotIndex && j > pivotIndex) {
		while (arr[i] <= pivot) i++;
		while (arr[j] > pivot) j--;
		if (i < pivotIndex && j > pivotIndex) swap(arr[i++], arr[j--]);
	}

	return pivotIndex;
}

void quickSort(vector<int> &arr, int start, int end, ll &comparisons, int choice) {
	if (start >= end)
		return;
	int p = partition(arr, start, end, comparisons, choice);

	// Sorting the left part
	quickSort(arr, start, p - 1, comparisons, choice);

	// Sorting the right part
	quickSort(arr, p + 1, end, comparisons, choice);
}

int main(int argc, char* argv[]) {
    ll comparisons = 0;
    rng.seed(rd());
    int choice = stoi(argv[1]);
    ifstream inp("input.txt");
    int n;
    inp >> n;
    vector<int> arr(n);
    for (int i = 0; i < n; i++) inp >> arr[i];
    auto start_time = chrono::high_resolution_clock::now();
	quickSort(arr, 0, n - 1, comparisons, choice);
    auto end_time = chrono::high_resolution_clock::now();
    //for (int i = 0; i < n; i++) cout << arr[i] << " ";
    //cout << endl;
    auto duration = chrono::duration_cast<chrono::milliseconds>(end_time - start_time);
    cout << duration.count() << " " << comparisons << endl;
	return 0;
}
