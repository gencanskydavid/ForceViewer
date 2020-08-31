import os, glob
import pandas as pd
import matplotlib.pyplot as plt
#Load file(s) in folder
try:
    file = glob.glob(os.getcwd()+"\\data\\NG\\*.fsl")
except Exception as e:
    print (e)
#
try:
    for i in file:
        fopen = open(i)
        fopen2 = pd.read_csv(fopen, skiprows=8, header=1)
        #get name of current file to show in Graph legend
        name = (i.split('\\'))
        #add data to graph with correct name
        plt.plot(fopen2["FB-Z"],fopen2.Fz,label=name[-1])
except Exception as e:
    print ("Couldn't open files.",e)
#
plt.ylabel("Force[N]")
plt.xlabel("Feedback position[mm]")
plt.title("Force / Position in Z Axis")
plt.grid(which='major',axis='both',color='black', linestyle='-', linewidth=1)
plt.legend(loc='upper center', bbox_to_anchor=(1.05, 0.75))
plt.show()