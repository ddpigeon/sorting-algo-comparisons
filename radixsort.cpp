#include <iostream>
#include <vector>
#include <fstream>
#include <chrono>
using namespace std;

// A utility function to get maximum
// value in arr[]
int getMax(vector<int> &arr, int n) {
	int mx = arr[0];
	for (int i = 1; i < n; i++) if (arr[i] > mx) mx = arr[i];
	return mx;
}

void countSort(vector<int> arr, int n, int exp) {
	int output[n];
	int i, count[10] = { 0 };

	for (i = 0; i < n; i++) count[(arr[i] / exp) % 10]++;
	for (i = 1; i < 10; i++) count[i] += count[i - 1];
	for (i = n - 1; i >= 0; i--) {
		output[count[(arr[i] / exp) % 10] - 1] = arr[i];
		count[(arr[i] / exp) % 10]--;
	}

	for (i = 0; i < n; i++) arr[i] = output[i];
}

void radixsort(vector<int> arr, int n) {
	int m = getMax(arr, n);
	for (int exp = 1; m / exp > 0; exp *= 10) countSort(arr, n, exp);
}

int main() {
    ifstream inp("input.txt");
    int n;
    inp >> n;
    vector<int> arr(n);
    for (int i = 0; i < n; i++) inp >> arr[i];
    auto start_time = chrono::high_resolution_clock::now();
	radixsort(arr, n);
    auto end_time = chrono::high_resolution_clock::now();
    //for (int i = 0; i < n; i++) cout << arr[i] << " ";
    //cout << endl;
    auto duration = chrono::duration_cast<chrono::milliseconds>(end_time - start_time);
    cout << duration.count() << endl;
	return 0;
}
