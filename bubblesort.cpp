#include <fstream>
#include <iostream>
#include <vector>
#include <chrono>
using namespace std;
using ll = long long;

void bubbleSort(vector<int> &arr, int n, ll &comparisons) {
	int i, j;
	bool swapped;
	for (i = 0; i < n-1; i++) {
		swapped = false;
		for (j = 0; j < n - i - 1; j++) {
            comparisons++;
			if (arr[j] > arr[j + 1]) {
				swap(arr[j], arr[j + 1]);
				swapped = true;
			}
		}
		if (swapped == false)
			break;
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
	bubbleSort(arr, n, comparisons);
    auto end_time = chrono::high_resolution_clock::now();
    //for (int i = 0; i < n; i++) cout << arr[i] << " ";
    //cout << endl;
    auto duration = chrono::duration_cast<chrono::milliseconds>(end_time - start_time);
    cout << duration.count() << " " << comparisons << endl;
	return 0;
}
