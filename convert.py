from scipy.io.wavfile import read
import numpy
from os import listdir
import os
import time

start_time = time.time()
print ("WAVE ---> CSV")
print("BATCH SIZE = %d" %len(listdir("myfolder/")))

nb_done = 0
# Browse all the .wav file in a specific folder
for file in os.listdir("myfolder/"):

	# Ensure that the processed file has .wav extension
    if file.endswith(".wav"):

    	# Read a file
        wave_file_id = read("myfolder/" + file)

        # Transform the file wave in a 1D numerical array (Thanks to Numpy)
        amplitude = numpy.array(wave_file_id[1],dtype=float)

        # Save the 1D numerical array in the 1st column of a CSV file 
        numpy.savetxt("csv/"+os.path.splitext(file)[0]+".csv", amplitude, delimiter=",")

        nb_done = nb_done + 1

        # Display the process current state
        print(" Converting " + file + " ---> " + os.path.splitext(file)[0]+".csv: DONE - %d / %d completed" %(nb_done, len(listdir("myfolder/"))))

    #Iterate


print("THE %d FILES BATCH PROCESSING LASTED %s SECONDS."%(len(listdir("myfolder/")),(time.time() - start_time)))
