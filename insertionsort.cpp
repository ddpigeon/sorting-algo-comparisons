#include <fstream>
#include <iostream>
#include <chrono>
#include <vector>
using namespace std;
using ll = long long;

void insertionSort(vector<int> &arr, int n, ll &comparisons) {
	int i, key, j;
	for (i = 1; i < n; i++) {
		key = arr[i];
		j = i - 1;
		while (j >= 0 && arr[j] > key) {
            comparisons++;
			arr[j + 1] = arr[j];
			j = j - 1;
		}
		arr[j + 1] = key;
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
    insertionSort(arr, n, comparisons);
    auto end_time = chrono::high_resolution_clock::now();
    //for (int i = 0; i < n; i++) cout << arr[i] << " ";
    //cout << endl;
    auto duration = chrono::duration_cast<chrono::milliseconds>(end_time - start_time);
    cout << duration.count() << " " << comparisons << endl;
	return 0;
}
