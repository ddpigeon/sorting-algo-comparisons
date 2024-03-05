import matplotlib.pyplot as plt
import os

random_bs = []
random_is = []
random_ms = []
random_qs = []
random_hs = []
random_rs = []

inc_bs = []
inc_is = []
inc_ms = []
inc_qs = []
inc_hs = []
inc_rs = []

dec_bs = []
dec_is = []
dec_ms = []
dec_qs = []
dec_hs = []
dec_rs = []

os.system("g++ random-test-cases.cpp -o rtc")
os.system("g++ decreasing-test-cases.cpp -o dtc")
os.system("g++ increasing-test-cases.cpp -o itc")
os.system("g++ quicksort.cpp -o qs")
os.system("g++ mergesort.cpp -o ms")
os.system("g++ insertionsort.cpp -o is")
os.system("g++ bubblesort.cpp -o bs")
os.system("g++ heapsort.cpp -o hs")
os.system("g++ radixsort.cpp -o rs")

for i in range(1, 150002, 100):
    os.system(f"./rtc {i}")
    if i <= 10000:
        random_bs.append(int(os.popen("./bs").read().strip("\n").split(" ")[0]))
    if i <= 20000:
        random_is.append(int(os.popen("./is").read().strip("\n").split(" ")[0]))
    random_ms.append(int(os.popen("./ms").read().strip("\n").split(" ")[0]))
    random_qs.append(int(os.popen("./qs 2").read().strip("\n").split(" ")[0]))
    random_hs.append(int(os.popen("./hs").read().strip("\n").split(" ")[0]))
    random_rs.append(int(os.popen("./rs").read().strip("\n")))

for i in range(1, 150002, 100):
    os.system(f"./itc {i}")
    inc_bs.append(int(os.popen("./bs").read().strip("\n").split(" ")[0]))
    inc_is.append(int(os.popen("./is").read().strip("\n").split(" ")[0]))
    inc_ms.append(int(os.popen("./ms").read().strip("\n").split(" ")[0]))
    inc_qs.append(int(os.popen("./qs 2").read().strip("\n").split(" ")[0]))
    inc_hs.append(int(os.popen("./hs").read().strip("\n").split(" ")[0]))
    inc_rs.append(int(os.popen("./rs").read().strip("\n")))

for i in range(1, 150002, 100):
    os.system(f"./dtc {i}")
    if i <= 10000:
        dec_bs.append(int(os.popen("./bs").read().strip("\n").split(" ")[0]))
    if i <= 20000:
        dec_is.append(int(os.popen("./is").read().strip("\n").split(" ")[0]))
    dec_ms.append(int(os.popen("./ms").read().strip("\n").split(" ")[0]))
    dec_qs.append(int(os.popen("./qs 2").read().strip("\n").split(" ")[0]))
    dec_hs.append(int(os.popen("./hs").read().strip("\n").split(" ")[0]))
    dec_rs.append(int(os.popen("./rs").read().strip("\n")))

x_axis = list(range(1, 150002, 100))

fig, axs =  plt.subplot_mosaic([['qs1'], ['qs2'], ['qs3']])

#axs['qs1'].set_xscale('log')
axs['qs1'].plot(x_axis, random_qs, "b", label="quicksort", linestyle =':')
axs['qs1'].plot(x_axis[:len(random_bs)], random_bs, "g", label="Bubble sort", linestyle ='-')
axs['qs1'].plot(x_axis[:len(random_is)], random_is, "r", label="Insertion sort", linestyle='-.')
axs['qs1'].plot(x_axis, random_ms, "y", label="Merge sort", linestyle='--')
axs['qs1'].plot(x_axis, random_hs, "brown", label="heap sort", linestyle='-')
axs['qs1'].plot(x_axis, random_rs, "r", label="radix sort", linestyle=':')
axs['qs1'].set_ylim(0, 200)
axs['qs1'].set_xlim(0, 150003)
axs['qs1'].set_title("Comparison of sorts with random arrays")
axs['qs1'].grid(axis='y')
axs['qs1'].set_xlabel("Length of array")
axs['qs1'].set_ylabel("Time taken in miliseconds")
axs['qs1'].legend()

#axs['qs2'].set_xscale('log')
axs['qs2'].plot(x_axis, inc_qs, "b", label="quicksort", linestyle='-')
axs['qs2'].plot(x_axis, inc_bs, "g", label="Bubble sort", linestyle="-")
axs['qs2'].plot(x_axis, inc_is, "r", label="Insertion sort", linestyle="-")
axs['qs2'].plot(x_axis, inc_ms, "y", label="Merge sort", linestyle='--')
axs['qs2'].plot(x_axis, inc_hs, "brown", label="heap sort", linestyle='-')
axs['qs2'].plot(x_axis, inc_rs, "r", label="radix sort", linestyle=':')
axs['qs2'].set_ylim(0, 200)
axs['qs2'].set_xlim(0, 150003)
axs['qs2'].set_title("Comparison of sorts with increasing test cases (already sorted array)")
axs['qs2'].grid(axis='y')
axs['qs2'].set_xlabel("Length of array")
axs['qs2'].set_ylabel("Time taken in miliseconds")
axs['qs2'].legend()

#axs['qs3'].set_xscale('log')
axs['qs3'].plot(x_axis, dec_qs, "b", label="quicksort", linestyle =':')
axs['qs3'].plot(x_axis[:len(dec_bs)], dec_bs, "g", label="Bubble sort", linestyle ='-')
axs['qs3'].plot(x_axis[:len(dec_is)], dec_is, "r", label="Insertion sort", linestyle='-.')
axs['qs3'].plot(x_axis, dec_ms, "y", label="Merge sort", linestyle='--')
axs['qs3'].plot(x_axis, dec_hs, "brown", label="heap sort", linestyle='-')
axs['qs3'].plot(x_axis, dec_rs, "r", label="radix sort", linestyle=':')
axs['qs3'].set_ylim(0, 200)
axs['qs3'].set_xlim(0, 150003)
axs['qs3'].set_title("Comparison of sorts with array of decreasing numbers")
axs['qs3'].grid(axis='y')
axs['qs3'].set_xlabel("Length of array")
axs['qs3'].set_ylabel("Time taken in miliseconds")
axs['qs3'].legend()

os.system("rm rtc dtc itc qs ms is bs hs rs")

plt.tight_layout()
plt.show()
