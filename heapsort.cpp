#include <iostream>
#include <fstream>
#include <chrono>
#include <vector>
using namespace std;
using ll = long long;

void heapify(vector<int> &arr, int n, int i, ll &comparisons) {
	int largest = i; // Initialize largest as root Since we are using 0 based indexing
	int l = 2 * i + 1; // left = 2*i + 1
	int r = 2 * i + 2; // right = 2*i + 2

    comparisons += 5;

	if (l < n && arr[l] > arr[largest]) largest = l;
	if (r < n && arr[r] > arr[largest]) largest = r;

	if (largest != i) {
		swap(arr[i], arr[largest]);
		heapify(arr, n, largest, comparisons);
	}
}

void heapSort(vector<int> &arr, int n, ll &comparisons) {
	for (int i = n / 2 - 1; i >= 0; i--) heapify(arr, n, i, comparisons);
	for (int i = n - 1; i >= 0; i--) {
		swap(arr[0], arr[i]);
		heapify(arr, i, 0, comparisons);
	}
}

int main() {
    ifstream inp("input.txt");
    int n;
    inp >> n;
    vector<int> arr(n);
    for (int i = 0; i < n; i++) inp >> arr[i];
    ll comparisons = 0;
    auto start_time = chrono::high_resolution_clock::now();
    for (int i = n/2 - 1; i >= 0; i--) heapify(arr, n, i, comparisons);
    heapSort(arr, n, comparisons);
    auto end_time = chrono::high_resolution_clock::now();
    //for (int i = 0; i < n; i++) cout << arr[i] << " ";
    //cout << endl;
    auto duration = chrono::duration_cast<chrono::milliseconds>(end_time - start_time);
    cout << duration.count() << " " << comparisons << endl;
	return 0;
}
