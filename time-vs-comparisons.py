import matplotlib.pyplot as plt
import os

random_bs = []
random_is = []
random_ms = []
random_qs = []
random_hs = []
random_rs = []

os.system("g++ random-test-cases.cpp -o rtc")
os.system("g++ decreasing-test-cases.cpp -o dtc")
os.system("g++ increasing-test-cases.cpp -o itc")
os.system("g++ quicksort.cpp -o qs")
os.system("g++ mergesort.cpp -o ms")
os.system("g++ insertionsort.cpp -o is")
os.system("g++ bubblesort.cpp -o bs")
os.system("g++ heapsort.cpp -o hs")
os.system("g++ radixsort.cpp -o rs")

for i in range(1000, 150002, 100):
    os.system(f"./rtc {i}")
    if i <= 15000:
        ti, cmp = [int(i) for i in os.popen("./bs").read().strip("\n").split(" ")]
        random_bs.append(ti / cmp)

    if i <= 30000:
        ti, cmp = [int(i) for i in os.popen("./is").read().strip("\n").split(" ")]
        random_is.append(ti/cmp)

    ti, cmp = [int(i) for i in os.popen("./ms").read().strip("\n").split(" ")]
    random_ms.append(ti/cmp)

    ti, cmp = [int(i) for i in os.popen("./qs 2").read().strip("\n").split(" ")]
    random_qs.append(ti/cmp)

    ti, cmp = [int(i) for i in os.popen("./hs").read().strip("\n").split(" ")]
    random_hs.append(ti/cmp)

x_axis = list(range(1000, 150002, 100))

fig, axs =  plt.subplot_mosaic([['qs1']])

#axs['qs1'].set_xscale('log')
axs['qs1'].plot(x_axis, random_qs, "b", label="quicksort", linestyle ='-')
axs['qs1'].plot(x_axis[:len(random_bs)], random_bs, "g", label="Bubble sort", linestyle ='-')
axs['qs1'].plot(x_axis[:len(random_is)], random_is, "r", label="Insertion sort", linestyle='-')
axs['qs1'].plot(x_axis, random_ms, "y", label="Merge sort", linestyle='-')
axs['qs1'].plot(x_axis, random_hs, "brown", label="heap sort", linestyle='-')
axs['qs1'].set_ylim(bottom=0)
axs['qs1'].set_xlim(1000, 150003)
axs['qs1'].set_title("Comparison of sorts with random arrays")
axs['qs1'].grid(axis='y')
axs['qs1'].set_xlabel("Length of array")
axs['qs1'].set_ylabel("execution time / number of comparisons")
axs['qs1'].legend()

os.system("rm rtc dtc itc qs ms is bs hs rs")

plt.tight_layout()
plt.show()
