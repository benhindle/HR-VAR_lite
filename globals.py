from tkinter import Label, Entry, Tk, Frame, LabelFrame
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk) 
from navigation import NavigationToolbar

def init():
    global canvas, control_frame, directory_name_frames, durationframe,\
        ecg1, ecg2, root, figure, file_path, font_heading, Fs, headers,\
        labels, plot, plotframe, result_frame, root, row_count SHEET_NAME, time,\
        times, toolbar, toolbarframe         

    ecg1 = list()
    ecg2 = list()
    file_path = ""
    font_heading = "sans-serif 12"
    Fs = 250
    headers = 3
    result_frame = ""
    root = Tk()
    root.title("HR variability")
    root.geometry("900x600")
    row_count = 0
    SHEET_NAME = 'ECG'
    time = list()
    
#   Define frames for plot and navigation toolbar to allow grid/pack to work together
    plotframe = Frame(root)
    toolbarframe = Frame(root)

#   Initialize figure/plot
    plt.gcf().subplots_adjust(bottom=0.15)  
    figure = plt.figure(figsize=(6, 3), dpi=100)
    plot = figure.add_subplot(1, 1, 1)
    
#   Set x-y plot labels
    plot.set_ylabel("Amplitude (mV)")
    plot.set_xlabel(xlabel="Time (s)")

#   Ensure spacing between axes and x-ylabels
    plt.tight_layout()
    
#   Initialize plot and toolbar widgits
    canvas = FigureCanvasTkAgg(figure, plotframe)
    toolbar = NavigationToolbar(canvas, toolbarframe)
    
#   Initialize control, duration and result frame/boxes
    directory_name_frames = Frame(root, pady=3)
    durationframe = LabelFrame(root, text="Trial duration", font=font_heading, pady=3)
    control_frame = LabelFrame(root, text="Plot controls", font=font_heading, pady=3)
    result_frame = LabelFrame(root, text="Trial detials", font=font_heading, pady=3)
    
#   Initialize times dictionary containing user input objects to pass to display
    times= {
        "start_hr" : Entry(durationframe, width=5),
        "start_min" : Entry(durationframe, width=5),
        "start_sec" : Entry(durationframe, width=5),
        "end_hr" : Entry(durationframe, width=5),
        "end_min" : Entry(durationframe, width=5),
        "end_sec" : Entry(durationframe, width=5),    
    }   

#   Initialize labels dictionary containing Label objects to pass to display
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

