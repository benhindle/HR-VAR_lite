from tkinter import END, Label
import globals

def insert_to_app(dictionary):
    for key in dictionary.keys():
        dictionary[key].insert(END, 0)

def set_grid():
#   Frames for page setup/division
    globals.root.grid_columnconfigure((0,1,2), weight=1, uniform='third')
    globals.toolbarframe.grid(row=0, column=0, columnspan=3, sticky='e')
    globals.plotframe.grid(row=1, column=0, columnspan=3)
    globals.durationframe.grid(row=3, column=1, rowspan=3, sticky='nsew', padx=10, pady=10)
    globals.durationframe.grid_columnconfigure(0, weight=1)
    globals.directory_name_frames.grid(row=2, column=0, columnspan=3, padx=10, pady=10, sticky="w")
    globals.control_frame.grid(row=3, column=0, rowspan=3, sticky='nsew', padx=10, pady=10)
    globals.result_frame.grid(row=3, column=2, rowspan=3, sticky='nsew', padx=10, pady=10)
    globals.control_frame.grid_columnconfigure(0, weight=1)
    
#   User input boxes within "Trial duration" box
    globals.times["end_min"].grid(row=2, column=2, padx=(2.5,5), sticky='ew')
    globals.times["end_sec"].grid(row=2, column=3, padx=(2.5,5), sticky='ew')
    globals.times["start_hr"].grid(row=1, column=1, padx=(2.5,5), sticky='ew')
    globals.times["start_min"].grid(row=1, column=2, padx=(2.5,5), sticky='ew')
    globals.times["start_sec"].grid(row=1, column=3, padx=(2.5,5), sticky='ew')
    globals.times["end_hr"].grid(row=2, column=1, padx=(2.5,5), sticky='ew')

#   Labels for user input boxes within "Trial duration" box
    globals.labels["file"].grid(row=0, column=0, columnspan=3, sticky='w')
    globals.labels["hr"].grid(row=0, column=1, sticky='ew')
    globals.labels["min"].grid(row=0, column=2, sticky='ew')
    globals.labels["sec"].grid(row=0, column=3, sticky='ew')
    globals.labels["start"].grid(row=1, column=0, padx=5, sticky='w')
    globals.labels["end"].grid(row=2, column=0, padx=5, sticky='w')

#   Labels for results of duration and HR variability caluclations within "Trial details" box
    globals.labels["duration_trial_max"].grid(row=0, column=0, sticky='w')
    globals.labels["duration_trial_max"].grid(row=1, column=0, sticky='w')
    globals.labels["hr_var"].grid(row=2, column=0, sticky='w')

def insert_figure():
    globals.canvas.get_tk_widget().grid(row=0, column=0)

#   Place the canvas on the Tkinter root 
    globals.canvas.get_tk_widget().grid(row=5, column=0)

#   Create the Matplotlib toolbar 
    globals.toolbar.update() 

#   Place the toolbar on the Tkinter root 
    globals.canvas.get_tk_widget().grid(row=6, column=0)

    insert_to_app(globals.times)

def update_labels(duration_hr, duration_min, duration_sec):
#   On file selection (before commanding plot)

#   File directory label update
    globals.labels["file"].destroy()
    globals.labels["file"] = Label(globals.directory_name_frame, text="File path: " + globals.file_path, font=globals.font_heading)
    globals.labels["file"].grid(row=2, column=0, columnspan=5, sticky='w')
    
#   Maximum trial duration update within "Trial details" box
    globals.labels["duration_trial_max"].destroy()
    globals.labels["duration_trial_max"] = Label(globals.result_frame, font=globals.font_heading, text="Max. trial duration: " + str(duration_hr) + 'hr '+ str(duration_min) + 'min '+ str(round(duration_sec, 3)) + 'sec')
    globals.labels["duration_trial_max"].grid(row=0, column=0, sticky='w')
    
#   End time update for user input boxes within "Trial duration" box
    globals.times["end_hr"].delete(0, END)
    globals.times["end_hr"].insert(END, duration_hr)
    globals.times["end_min"].delete(0, END)
    globals.times["end_min"].insert(END, duration_min)
    globals.times["end_sec"].delete(0, END)
    globals.times["end_sec"].insert(END, duration_sec)

#   Reset all starting times to the beginning of the trial (user input =0) within "Trial duration" box
    globals.times["start_hr"].delete(0, END)
    globals.times["start_hr"].insert(END, int(0))
    globals.times["start_min"].delete(0, END)
    globals.times["start_min"].insert(END, int(0))
    globals.times["start_sec"].delete(0, END)
    globals.times["start_sec"].insert(END, float(0))
