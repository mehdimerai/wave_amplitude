# wave_amplitude
Convert a batch of WAVE files into CSV Amplitude files using Numpy, Python. This work could be helpful for people working around signal processing and looking for a Mathlab open source alternative for this specific function.

# tutorial

##Files organization
Let's support that you're code is in a folder named "CurrentFolder". You need to organize your files and folders as follow:

CurrentFolder
-- convert.py (Python file)
-- myfolder (folder containing your .wav files)
-- csv (folder that will host the generated .csv files)

##Execution
1. Throw Terminal, navigate to "CurrentFolder" (or any location you where you have your convert.py file)
2. Simply enter this command: 
```
python convert.py
```

##Results
The execution result will be displayed your Terminal as follow

```
WAVE ---> CSV
BATCH SIZE = 4
 Converting File10.wav ---> File10.csv: DONE - 1 / 4 completed
 Converting File11.wav ---> File11.csv: DONE - 2 / 4 completed
 Converting File12.wav ---> File12.csv: DONE - 3 / 4 completed
 Converting File9.wav ---> File9.csv: DONE - 4 / 4 completed
THE 4 FILES BATCH PROCESSING LASTED 0.524949073792 SECONDS.
```

Then, you will find your amplitude files under the folder csv.
