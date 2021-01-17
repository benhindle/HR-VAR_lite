from tkinter import Label, Entry, Tk, Frame, LabelFrame
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk) 
from navigation import NavigationToolbar

def init():
    global root, figure, font_heading, SHEET_NAME, plot, canvas,\
        toolbar, control_frame, result_frame, plotframe, toolbarframe,\
        directory_name_frames, durationframe, headers, Fs, times, labels, \
        file_path, time, row_count, ecg1, ecg2, directory_name_frame, result_frame

    root = Tk()
    root.title("HR variability")
    root.geometry("900x600")
    directory_name_frame = ""
    result_frame = ""
    headers = 3
    Fs = 250
    SHEET_NAME = 'ECG'
    file_path = ""
    time = list()
    row_count = 0
    ecg1 = list()
    ecg2 = list()
    font_heading = "sans-serif 12"
    
    plotframe = Frame(root)
    toolbarframe = Frame(root)

    plt.gcf().subplots_adjust(bottom=0.15)
    
    figure = plt.figure(figsize=(6, 3), dpi=100)
    plot = figure.add_subplot(1, 1, 1)
    
    plot.set_ylabel("Amplitude (mV)")
    plot.set_xlabel(xlabel="Time (s)")
    
    plt.tight_layout()
    
    canvas = FigureCanvasTkAgg(figure, plotframe)
    
    toolbar = NavigationToolbar(canvas, toolbarframe)
    
    durationframe = LabelFrame(root, text="Trial duration", font=font_heading, pady=3)
    directory_name_frames = Frame(root, pady=3)

    control_frame = LabelFrame(root, text="Plot controls", font=font_heading, pady=3)
    result_frame = LabelFrame(root, text="Trial detials", font=font_heading, pady=3)
    
    times= {
        "start_hr" : Entry(durationframe, width=5),
        "start_min" : Entry(durationframe, width=5),
        "start_sec" : Entry(durationframe, width=5),
        "end_hr" : Entry(durationframe, width=5),
        "end_min" : Entry(durationframe, width=5),
        "end_sec" : Entry(durationframe, width=5),    
    }   

    labels = {
        "file" : Label(directory_name_frames, text="File pending selection...", font=font_heading),
        "hr" : Label(durationframe, text="hr", font=font_heading),
        "min" : Label(durationframe, text="min", font=font_heading),
        "sec" : Label(durationframe, text="sec", font=font_heading),
        "start" : Label(durationframe, text="Start time", font=font_heading),
        "end" : Label(durationframe, text="End time", font=font_heading),
        "duration_trial" : Label(result_frame, text="Selected duration: ", font=font_heading),
        "hr_var" : Label(result_frame, text="HR variability (s): ", font=font_heading),
        "duration_trial_max" : Label(result_frame, text="Max. trial duration: ", font=font_heading),
    }

