import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
from scipy.optimize import curve_fit

def square_root_offset(x, a, b):
    return a * x**(1/2) + b

def square_root_origin(x, a):
    return a * x**(1/2)

data_path = "../data/filter-paper_water.csv"
df = pd.read_csv(data_path)

x, y = df["t[s]"], df["l[mm]"]

plt.rcParams['text.usetex'] = True
plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.size'] = 50

plt.rcParams['axes.linewidth'] = 3

plt.rcParams['xtick.major.size'] = 12
plt.rcParams['xtick.major.width'] = 3
    
plt.rcParams['ytick.major.size'] = 12
plt.rcParams['ytick.major.width'] = 3

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(20,8))

objective = square_root_offset
label_fit = r"$ l = a \cdot t^{1/2} + b$"
popt, var = curve_fit(objective, x, y)
a, b = popt

print(a, b)

objective = square_root_origin
label_fit = r"$ l = a \cdot t^{1/2}$"
#popt, var = curve_fit(objective, x, y)
#a = popt

print(a)
    
xline = np.arange(0,65,60/1000)
ax1.plot(xline, objective(xline, a), label = label_fit, linewidth = 4, color = "black")
#ax1.plot(xline, objective(xline, a, b), label = label_fit, linewidth = 4, color = "black")
#ax1.scatter(x, y, label="Experiment", s = 200, marker = "o", color = "black")
ax1.scatter(x, [y_new - b for y_new in y], label="Experiment", s = 200, marker = "o", color = "black")

ax1.text(0.02, 0.89, r'\bf{(a)}', transform=ax1.transAxes)

xline = np.arange(a**(-2), 100,60/1000)
ax2.plot(xline, objective(xline, a), label = label_fit, linewidth = 4, color = "black")
ax2.scatter(x, [y_new - b for y_new in y], label="Experiment", s = 200, marker = "o", color = "black")

xline = np.arange(1, 10, 1/10)
ax2.plot(xline, objective(xline, a / 2.5 ), label = label_fit, linewidth = 2, color = "black")
ax2.plot(xline, np.repeat(a/2.5, 90), label = label_fit, linewidth = 2, color = "black")
ax2.plot(np.repeat(10, 90), objective(xline, a / 2.5 ), label = label_fit, linewidth = 2, color = "black")

ax2.text(0.02, 0.88, r'\bf{(b)}', transform=ax2.transAxes)
ax2.text(3, a/2.5 - 0.6 , r'$2$')
ax2.text(12, a/2.5 + 0.9 , r'$1$')

print(objective(a**(-2), a))

ax1.set_xlim(0,65)
#ax1.set_ylim(0,65)
ax1.set_ylim(0,39)
ax1.set_yticks(np.arange(0, 39, 10))

ax1.set_xlabel(r"$t$ [s]")
ax1.set_ylabel(r"$l$ [mm]")

ax1.xaxis.set_label_coords(0.5,-0.14)
ax1.yaxis.set_label_coords(-0.16,0.5)

ax2.set_xscale('log')
ax2.set_yscale('log')

ax2.set_xlim(a**(-2), 100)
ax2.set_ylim(1,50)
ax2.set_yticks([1,10])
ax2.set_xticks([0.1, 1,10])

ax2.set_xlabel(r"$\log t$")
ax2.set_ylabel(r"$\log l$")

ax2.xaxis.set_label_coords(0.5,-0.14)
ax2.yaxis.set_label_coords(-0.18,0.5)

plt.subplots_adjust(wspace = 0.3)

ax1.legend(frameon = False, handlelength=0.5,loc="lower right")

plt.savefig("../pictures/experiments/filter-paper_water_1s-60s_eval_origin-offset.pdf", bbox_inches='tight')
# plt.savefig("../pictures/experiments/filter-paper_water_1s-60s_eval_origin.pdf", bbox_inches='tight')
# plt.savefig("../pictures/experiments/filter-paper_water_1s-60s_eval_offset.pdf", bbox_inches='tight')