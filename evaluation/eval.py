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
plt.rcParams['font.size'] = 42

plt.rcParams['axes.linewidth'] = 3

plt.rcParams['xtick.major.size'] = 12
plt.rcParams['xtick.major.width'] = 3
    
plt.rcParams['ytick.major.size'] = 12
plt.rcParams['ytick.major.width'] = 3

fig, ax = plt.subplots(1, 1, figsize=(16,6))

objective = square_root_offset
label_fit = r"$ l = a \cdot t^{1/2} + b$"
popt, var = curve_fit(objective, x, y)
a, b = popt

print(a, b)

# objective = square_root_origin
# label_fit = r"$ l = a \cdot t^{1/2}$"
# popt, var = curve_fit(objective, x, y)
# a = popt

# print(a)

#objective = square_root_origin
#label_fit = r"$ l = a \cdot t^{1/2}$"
    
xline = np.arange(0,65,60/1000)
# ax.plot(xline, objective(xline, a), label = label_fit, linewidth = 4, color = "black")
ax.plot(xline, objective(xline, a, b), label = label_fit, linewidth = 4, color = "black")
ax.scatter(x, y, label="Experiment", s = 200, marker = "o", color = "black")
#ax.scatter(x, [y_new - b for y_new in y], label="Experiment", s = 200, marker = "o", color = "black")

ax.set_xlim(0,65)
ax.set_ylim(0,65)
#ax.set_ylim(0,45)

ax.set_xticks

ax.set_xlabel(r"$t$ [s]")
ax.set_ylabel(r"$l$ [mm]")

ax.xaxis.set_label_coords(0.5,-0.18)
ax.yaxis.set_label_coords(-0.08,0.5)

ax.legend(frameon = False, handlelength=0.5,loc="lower right")

# plt.savefig("../pictures/experiments/filter-paper_water_1s-60s_eval_origin-offset.pdf", bbox_inches='tight')
# plt.savefig("../pictures/experiments/filter-paper_water_1s-60s_eval_origin.pdf", bbox_inches='tight')
plt.savefig("../pictures/experiments/filter-paper_water_1s-60s_eval_offset.pdf", bbox_inches='tight')