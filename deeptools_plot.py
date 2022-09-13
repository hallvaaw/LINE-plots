#!/bin/python3

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os


SAMPLES = ["active_L1Md_A", "active_L1Md_T", "inactive_L1Md_A", "inactive_L1Md_T"]
PATH = os.getcwd()



class PlotMatrix:
    
    
    def __init__(self, name, dataset):
        self.name = name
        self.dataset = dataset
        self.lines = []
        self.linspaces = []
        self.ul = []
        self.ll = []


    def input_data(self):
        self.data = pd.read_csv(f"{PATH}{self.dataset}", "\t", skiprows = 1)
        self.subset = self.data.iloc[0:,6:]
        self.row_mean = list(self.subset.mean(axis = 0))
        self.uci = list(self.subset.apply(lambda x: np.mean(x) + 1.96 * (np.std(x) / np.sqrt(len(x))), axis = 0)) # Upper confidence interval
        self.lci = list(self.subset.apply(lambda x: np.mean(x) - 1.96 * (np.std(x) / np.sqrt(len(x))), axis = 0)) # Lower confidence interval
        self.x_ = np.linspace(-1000, 1000, self.subset.shape[1])
        self.lines.append(self.row_mean)
        self.linspaces.append(self.x_)
        self.ul.append(self.uci)
        self.ll.append(self.lci)
        return self.linspaces[0], self.lines[0], self.ul[0], self.ll[0]
    
    def plot_mean(self):
        return ax2.plot(self.input_data()[0], self.input_data()[1], label = self.name, linewidth = 3, color = self.line_color)
        
    def plot_uci(self):
        return ax2.plot(self.input_data()[0], self.input_data()[2], linewidth = 1, linestyle = "dashed", color = self.line_color)
    
    def plot_lci(self):
        return ax2.plot(self.input_data()[0], self.input_data()[3], linewidth = 1, linestyle = "dashed", color = self.line_color)



for sample in SAMPLES:
    fig, ax = plt.subplots(figsize = (8, 8))
    ax2 = ax.twinx()
    cage = PlotMatrix("CAGE", f"{sample}_matrix") # Plot CAGE signal
    ax.plot(cage.input_data()[0], cage.input_data()[1], label = cage.name, linewidth = 3, color = "blue")
    ax.set_xlabel("bp")
    ax.set_xlim(-1000, 1000) # 1000 bp upstream and downstream of TSS
    ax.set_ylim(0, 5)
    ax.set_ylabel("CAGE signal")
    plt.locator_params(axis = "x", nbins = 3)
    # Plot other metrics on the Y-axis
    wt_h2az = PlotMatrix("WT-H2AZ", f"{sample}_wt-h2az_s8_matrix")
    ax2.plot(wt_h2az.input_data()[0], wt_h2az.input_data()[1], label = "WT-H2AZ" , linewidth = 3, color = "deeppink")
    srr7059148 = PlotMatrix("SRR7059148", f"{sample}_SRR7059148_matrix")
    ax2.plot(srr7059148.input_data()[0], srr7059148.input_data()[1], label = "ATAC" , linewidth = 3, color = "purple")
    srr1991255 = PlotMatrix("SRR1991255", f"{sample}_SRR1991255_matrix")
    ax2.plot(srr1991255.input_data()[0], srr1991255.input_data()[1], label = "YY1", linewidth = 3, color = "gold")
    h1, l1 = ax.get_legend_handles_labels()
    h2, l2 = ax2.get_legend_handles_labels()
    plt.title(f"{sample}", size =  20)
    ax.legend(h1+h2, l1+l2, loc = "upper right")
    plt.savefig(f"{PATH}{sample}.png")











