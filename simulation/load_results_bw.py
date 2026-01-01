from os import fork
import numpy as np
import matplotlib.pyplot as plt
import pickle

plt.figure()

# results folder path
folder = "results/"

#-----------------------------------------
# Results to load and plot
#-----------------------------------------
file_list = [
    "samp500000_bw125000_sf7_cr2_payLen32_clk_offset_ppm0_softTrue_ldroFalse",
    "samp500000_bw125000_sf9_cr2_payLen32_clk_offset_ppm0_softTrue_ldroFalse",
]


colors = plt.cm.rainbow(np.linspace(0,1,len(file_list)))
for idx,file in enumerate(file_list):
    
    snrs, FER, Glob_FER = pickle.load(open(folder+file+".pkl","rb"))
    # Plot FER of frame which preamble has been detected
    plt.semilogy(snrs,FER,'-d',label=file_list[idx], color=colors[idx])
    # Plot FER over all transmitted frames
    plt.semilogy(snrs,Glob_FER,'--d',label=file_list[idx], color=colors[idx])

plt.grid()
plt.xlabel('SNR [dB]')
plt.ylabel('Frame Error rate')
plt.ylim([1e-4,1.05])
plt.legend(loc='upper right')
plt.title("")
plt.show()

