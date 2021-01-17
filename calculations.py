import globals 
import datetime

def get_frames(timeSec, timeMin, timeHr):
    return int(round((float(timeSec) * globals.Fs) + (int(float(timeMin)) * 60 * globals.Fs) + (int(float(timeHr)) * 3600 * globals.Fs)))

def calc_trial_duration(start_frame, end_frame):
    total_frames = end_frame - start_frame
    total_time_sec = total_frames/globals.Fs
    time_delt_string = str(datetime.timedelta(seconds=total_time_sec))
    time_str_hr = time_delt_string.split(':')[0]
    time_str_min = time_delt_string.split(':')[1]
    time_str_sec = str(round(float(time_delt_string.split(':')[2]), 3))
    return time_str_hr + 'hr ' + time_str_min + 'min ' + time_str_sec + 'sec'