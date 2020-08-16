import os, glob
import pandas as pd
import matplotlib.pyplot as plt
#Load file(s) in folder
try:
    file = glob.glob(os.getcwd()+"\\data\\*.fsl")
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
        plt.plot(fopen2.Fz,label=name[-1])
except Exception as e:
    print ("Couldn't open files.",e)
#
plt.ylabel("Force[N]")
plt.xlabel("Timestamp[1p=3.5ms]")
plt.title("Timeseries of Force in Z axis")
plt.legend(loc='upper center', bbox_to_anchor=(1, 0.75))
plt.show()