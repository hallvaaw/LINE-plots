#!/bin/python3

from Bio import SeqIO
import os
import matplotlib.pyplot as plt

workdir = os.getcwd() # Get working directory

def GC(seq):
    """
    Plot GC-content
    """
    gc = sum(seq.count(x) for x in ["G", "C", "g", "c", "S", "s"])
    try:
        return gc * 100.0 / len(seq)
    except ZeroDivisionError:
        return 0.0

def AT(seq):
    """
    Plot AT-content
    """
    at = sum(seq.count(x) for x in ["A", "T", "a", "t", "S", "s"])
    try:
        return at * 100.0 / len(seq)
    except ZeroDivisionError:
        return 0.0


lines = ['L1MD3', 'Lx7', 'L1VL2', 'Lx3B', 'L1Md_F3', 'L1Md_F', 'L1_Mus1', 'L1ME5', 'Lx2A1', 'Lx4A', 'L1Md_T', 'L1Md_F2', 'Lx3_Mus', 'Lx3A', 'Lx8', 'L1Md_A', 'Lx4B', 'L1VL4', 'L1_Mur1', 'Lx6', 'Lx2B', 'L1_Mus4', 'L1MA9', 'Lx2A', 'Lx', 'Lx5', 'L1_Mur3', 'L1VL1', 'Lx2', 'Lx9', 'Lx3C', 'L1MA4', 'MusHAL1', 'L1_Mus3', 'L1Md_Gf', 'L1_Mus2']


fig, ax = plt.subplots(len(lines), figsize = (8, 182)) # Width, height
fig.tight_layout(h_pad = 5) # Avoid overlap between plots

for i in range(len(lines)):
    gc_values = sorted(AT(rec.seq) for rec in SeqIO.parse(f"{workdir}/{lines[i]}.fasta", "fasta"))
    ax[i].plot(gc_values)
#    ax[i].set_ylim(33, 48)
    ax[i].set_ylim(53, 67)
    ax[i].set_title(f"{lines[i]} {len(gc_values)} elements")
    ax[i].set_xlabel("Genes")
    ax[i].set_ylabel("AT%")

plt.savefig(f"{workdir}/lines_AT_plot.png")
