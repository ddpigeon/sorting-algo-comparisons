#include <iostream>
#include <chrono>
#include <fstream>
#include <vector>
using namespace std;
using ll = long long;

void merge(vector<int> &arr, int p, int q, int r, ll &comparisons) {
    int n1 = q - p + 1;
    int n2 = r - q;
    vector<int> l(n1), m(n2);

    for (int i = 0; i < n1; i++) l[i] = arr[p + i];
    for (int j = 0; j < n2; j++) m[j] = arr[q + 1 + j];

    int i, j, k;
    i = 0;
    j = 0;
    k = p;

    while (i < n1 && j < n2) {
        comparisons++;
        if (l[i] <= m[j]) {
            arr[k] = l[i];
            i++;
        } 
        else {
            arr[k] = m[j];
            j++;
        }
        k++;
    }

    while (i < n1) {
        arr[k] = l[i];
        i++;
        k++;
    }

    while (j < n2) {
        arr[k] = m[j];
        j++;
        k++;
    }
}

void mergeSort(vector<int> &arr, int l, int r, ll &comparisons) {
    if (l < r) {
        int m = l + (r - l) / 2;
        mergeSort(arr, l, m, comparisons);
        mergeSort(arr, m + 1, r, comparisons);
        merge(arr, l, m, r, comparisons);
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
    mergeSort(arr, 0, n-1, comparisons);
    auto end_time = chrono::high_resolution_clock::now();
    //for (int i = 0; i < n; i++) cout << arr[i] << " ";
    //cout << endl;
    auto duration = chrono::duration_cast<chrono::milliseconds>(end_time - start_time);
    cout << duration.count() << " " << comparisons << endl;
    return 0;
}
