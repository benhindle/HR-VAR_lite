from tkinter import filedialog, Label, Button, messagebox
import xlrd
import numpy as np
import matplotlib
from scipy.signal import find_peaks
from calculations import get_frames, calc_trial_duration
from display import update_labels
import datetime
import globals
  

def click_browse():
#   xlsx. workbook config and file selection
    globals.file_path = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx")])
    workbook = xlrd.open_workbook(globals.file_path)
    sheet = workbook.sheet_by_name(globals.SHEET_NAME)
    globals.row_count = sheet.nrows - globals.headers
    globals.time = np.linspace(0, globals.row_count/globals.Fs, globals.row_count)
    
#   Convert total time in seconds to hr:min:sec
    duration = datetime.timedelta(seconds=globals.time[len(globals.time)-1])
    duration_hr = int(str(duration).split(':')[0])
    duration_min = int(str(duration).split(':')[1])
    duration_sec = float(str(duration).split(':')[2])
    
#   For future fuctionality - multiple input
    globals.ecg1 = np.zeros(globals.row_count)
    globals.ecg2 = np.zeros(globals.row_count)

#   Update end time input fields with maximum duration in hr:min:sec
    update_labels(duration_hr, duration_min, duration_sec)

#   For future fuctionality - multiple input
    for i in range(globals.headers, globals.row_count + globals.headers):
        globals.ecg1[i - globals.headers] = sheet.cell_value(i, 2)
        globals.ecg2[i - globals.headers] = sheet.cell_value(i, 3)
    
#   Make plot button active if file selected
    if globals.file_path != "":
        init_bottons(plot=True)

def click_plot(plot, canvas, labels):
#   Get start and end time user input
    start_hr = globals.times["start_hr"].get()
    start_min = globals.times["start_min"].get()
    start_sec = globals.times["start_sec"].get()
    end_hr = globals.times["end_hr"].get()
    end_min = globals.times["end_min"].get()
    end_sec = globals.times["end_sec"].get()
    
#   Clear plot and calculate start and end frame based on user input
    plot.clear()
    start_frame = get_frames(start_sec, start_min, start_hr)
    end_frame = get_frames(end_sec, end_min, end_hr)
    duration_total = calc_trial_duration(start_frame, end_frame)
    
#   Catch error case where use inputs 0 duration or start time greater than end -> else generate/update plot
    if start_frame == end_frame or start_frame > end_frame:
        print(messagebox.showwarning("Warning!", "Please ensure End time is greater than Start time..."))
    else:
        peaks3, _ = find_peaks(globals.ecg1[start_frame:end_frame], width=3, height=0.35)
        plot.plot(globals.time[peaks3 + start_frame], globals.ecg1[peaks3 + start_frame], 'og')
        plot.plot(globals.time[start_frame:end_frame], globals.ecg1[start_frame:end_frame])  
        plot.set_ylabel("Amplitude (mV)")
        plot.set_xlabel(xlabel="Time (s)")
        canvas.draw()
        temp_var = np.zeros(len(peaks3)-1)

#       Calculate mean HR variability throughout user selected time period
        for i in range(0, len(peaks3)-1):
            temp_var[i] = (peaks3[i+1] - peaks3[i]) / globals.Fs

        hrvar_mean = round(np.mean(temp_var), 3)
        hrvar_std = round(np.std(temp_var), 3)

#       Print trial duration and HR variability measures to "Trial details" box
        globals.labels["duration_trial"] = Label(globals.result_frame, text="Selected duration: " + duration_total)
        globals.labels["duration_trial"].grid(row=1, column=0, sticky='w')

        globals.labels["hr_var"] = Label(globals.result_frame, text="HR variability (s): " + str(hrvar_mean) + " " + u'\xb1' + " " + str(hrvar_std))
        globals.labels["hr_var"].grid(row=2, column=0, sticky='w')      

def init_bottons(plot):
    global button_plot
#   if case on initial load and no file selected -> else case once file selected
    if not(plot):
        button_file = Button(globals.control_frame, width=20, text='Select file', font=globals.font_heading, command=click_browse)
        button_file.grid(row=0, column=0, padx=20, pady=5, sticky='ew')
        button_plot = Button(globals.control_frame, state="disabled", width=20, text="Plot", font=globals.font_heading, command = lambda: click_plot(globals.plot, globals.canvas, globals.labels))
        button_plot.grid(row=1, column=0, padx=20, pady=5, sticky='ew')
    else:
        button_plot["state"] = "normal"
