import matplotlib.pyplot as plt
import os

random_1 = []
random_2 = []
random_3 = []

inc_1 = []
inc_2 = []
inc_3 = []

dec_1 = []
dec_2 = []
dec_3 = []


os.system("g++ random-test-cases.cpp -o rtc")
os.system("g++ decreasing-test-cases.cpp -o dtc")
os.system("g++ increasing-test-cases.cpp -o itc")
os.system("g++ quicksort.cpp -o qs")


for i in range(1, 20002, 100):
    os.system(f"./rtc {i}")

    random_1.append(int(os.popen("./qs 1").read().strip("\n").split(" ")[0]))
    random_2.append(int(os.popen("./qs 2").read().strip("\n").split(" ")[0]))
    random_3.append(int(os.popen("./qs 3").read().strip("\n").split(" ")[0]))

#print(random_1)
#print(random_2)
#print(random_3)

for i in range(1, 20002, 100):
    os.system(f"./itc {i}")
    inc_1.append(int(os.popen("./qs 1").read().strip("\n").split(" ")[0]))
    inc_2.append(int(os.popen("./qs 2").read().strip("\n").split(" ")[0]))
    inc_3.append(int(os.popen("./qs 3").read().strip("\n").split(" ")[0]))


#print(inc_1)
#print(inc_2)
#print(inc_3)


for i in range(1, 20002, 100):
    os.system(f"./dtc {i}")
    dec_1.append(int(os.popen("./qs 1").read().strip("\n").split(" ")[0]))
    dec_2.append(int(os.popen("./qs 2").read().strip("\n").split(" ")[0]))
    dec_3.append(int(os.popen("./qs 3").read().strip("\n").split(" ")[0]))


#print(dec_1)
#print(dec_2)
#print(dec_3)

x_axis = list(range(1, 20002, 100))

fig, axs =  plt.subplot_mosaic([['qs1'], ['qs2'], ['qs3']])

#axs['qs1'].set_xscale('log')
axs['qs1'].plot(x_axis, random_1, "b", label="Random numbers", linestyle =':')
axs['qs1'].plot(x_axis, inc_1, "g", label="Increasing numbers", linestyle ='-')
axs['qs1'].plot(x_axis, dec_1, "r", label="Decreasing numbers", linestyle='-.')
axs['qs1'].set_ylim(0, 250)
axs['qs1'].set_xlim(0, 20003)
axs['qs1'].set_title("First element as pivot")
axs['qs1'].grid(axis='y')
axs['qs1'].set_xlabel("Length of array")
axs['qs1'].set_ylabel("Time taken in miliseconds")
axs['qs1'].legend()


#axs['qs2'].set_xscale('log')
axs['qs2'].plot(x_axis, random_2, "b", label="Random numbers", linestyle=':')
axs['qs2'].plot(x_axis, inc_2, "g", label="Increasing numbers", linestyle="-")
axs['qs2'].plot(x_axis, dec_2, "r", label="Decreasing numbers", linestyle="-.")
axs['qs2'].set_ylim(0, 100)
axs['qs2'].set_xlim(0, 20003)
axs['qs2'].set_title("Randomized pivot")
axs['qs2'].grid(axis='y')
axs['qs2'].set_xlabel("Length of array")
axs['qs2'].set_ylabel("Time taken in miliseconds")
axs['qs2'].legend()


#axs['qs3'].set_xscale('log')
axs['qs3'].plot(x_axis, random_3, "b", label="Random numbers", linestyle=':')
axs['qs3'].plot(x_axis, inc_3, "g", label="Increasing numbers", linestyle='-')
axs['qs3'].plot(x_axis, dec_3, "r", label="Decreasing numbers", linestyle='-.')
axs['qs3'].set_ylim(0, 250)
axs['qs3'].set_xlim(0, 20003)
axs['qs3'].set_title("Median of three")
axs['qs3'].grid(axis='y')
axs['qs3'].set_xlabel("Length of array")
axs['qs3'].set_ylabel("Time taken in miliseconds")
axs['qs3'].legend()

os.system("rm rtc")
os.system("rm dtc")
os.system("rm itc")
os.system("rm qs")

plt.tight_layout()
plt.show()
