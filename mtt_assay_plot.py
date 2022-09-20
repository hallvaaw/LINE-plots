import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Concentrations and controls

control_mean = [0.5555, 0.653333, 0.730167]
control_sd = [0.275907, 0.501557, 0.384411]

arac_mean = [0.475, 0.539667, 0.693667]
arac_sd = [0.206673, 0.379462, 0.455551]

p100_mean =[0.531333, 0.542389, 0.6605]
p100_sd = [0.329805, 0.482048, 0.441396]

p200_mean = [0.546, 0.584167, 0.705389]
p200_sd = [0.313912, 0.473587, 0.466092]

p400_mean = [0.500778, 0.501278, 0.725056]
p400_sd = [0.31083, 0.451884, 0.490935]

p800_mean = [0.544111, 0.494389, 0.674056]
p800_sd = [0.319797, 0.4388, 0.466245]

p1600_mean = [0.511222, 0.466944, 0.572722]
p1600_sd = [0.28064, 0.440134, 0.450958]

ax_len = len(p1600_mean) # Length of axis
fig, ax = plt.subplots(figsize = (25, 25)) # Create subplot for each concentration
ax.tick_params(axis = "x", labelsize = 20)
ax.tick_params(axis = "y", labelsize = 25)
ax.plot(range(0, ax_len), control_mean, "o", label = "Control", color = "black", markersize = 15)
ax.plot(range(0, ax_len), p100_mean, "s", label = "P100", color = "#6CB0D6", markersize = 15)
ax.plot(range(0, ax_len), p200_mean, "v", label = "P200", color = "#3C93C2", markersize = 15)
ax.plot(range(0, ax_len), p400_mean, "D", label = "P400", color = "#226E9C", markersize = 15)
ax.plot(range(0, ax_len), p800_mean, "x", label = "P800", color = "#0D4A70", markersize = 15)
ax.plot(range(0, ax_len), p1600_mean, "^", label = "P1600", color = "#0D4A70", markersize = 15)
ax.plot(range(0, ax_len), arac_mean, "P", label = "AraC", color = "#FF1F5B", markersize = 15)
ax.errorbar(range(0, ax_len), control_mean, yerr = control_sd, color = "black", capsize = 12, linewidth = 3)
ax.errorbar(range(0, ax_len), p100_mean, yerr = p100_sd, color = "#6CB0D6", capsize = 12, linewidth = 3)
ax.errorbar(range(0, ax_len), p200_mean, yerr = p200_sd, color = "#3C93C2", capsize = 12, linewidth = 3)
ax.errorbar(range(0, ax_len), p400_mean, yerr = p400_sd, color = "#226E9C", capsize = 12, linewidth = 3)
ax.errorbar(range(0, ax_len), p800_mean, yerr = p800_sd, color = "#0D4A70", capsize = 12, linewidth = 3)
ax.errorbar(range(0, ax_len), p1600_mean, yerr = p1600_sd, color = "#0D4A70", capsize = 12, linewidth = 3)
ax.errorbar(range(0, ax_len), arac_mean, yerr = arac_sd, color = "#FF1F5B", capsize = 12, linewidth = 3)


plt.locator_params(axis = 'x', nbins = 3) # 22 1st
ax.set_xticklabels([0, 24, 48, 72], size = 25) # 3rd

plt.xlabel("Hours", size = 30)
plt.ylabel("Absorbance (570 nm)", size = 30)
ax.legend(loc = 'upper left', shadow = True, prop = {"size":20})
plt.savefig("MTT_assay.tif")
