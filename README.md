# HR-VAR lite
HR-VAR lite is a lightweight, cross-platform program for measuring heart rate variability from a raw ECG (electrocardiogram) signal. The program, written in Python 3.8.2, is designed to accept .xlsx files output from a commercial ECG system and is intended to be a lightweight alternative to native proprietary software.

<br />

## Basic functionality
* Take in .xlsx files produced by the a commercial ECG system
* Accept start and end time instances to measure mean heart rate variability for the specified duration
* Plot the specified duration for visual inspection/validation of peak detection
* Allows user interaction with ploted data
* Save output plot to file 

<br />

## Input data structure
While HR-VAR lite was designed to be used for raw data output from a specific ECG system, structuring data in the following way will allow heart rate variability estimation using any system. The sheet containing the raw ECG data must be named _"ECG"_, alternatively, the argument _SHEET_NAME_ may be changed within globals.py. Users should also note and change accordingly the sample rate of the system used. This can be changed within the globals.py file, under Fs, where Fs is the system sample rate in Hz.

| Sensor ID: abc123 | | | |
| ------------- |-------------| ----- | ----- |
| Designation: | | |
| Date | Time | ECG Lead 1 | ECG Lead 2 |
| \<data\> | \<data\> | \<data\> | \<data\> |

<br />

## Future functionality
* User defined tuning of peak detection algorithm for increased accuracy
* Option for the user defined ECG line/input where multiple inputs exist
* Improved file loading speed
* User defined time scale
* Aesthetic improvements
* User defined sample rate