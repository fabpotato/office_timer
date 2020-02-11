from tkinter import *
import datetime
import os
from if_half_day import do_what

def on_closing():
    is_leaving_early = (datetime.datetime.now() - start_time) < SHIFT
    if is_leaving_early:
        should_leave_at = start_time + SHIFT
        do_what(should_leave_at.time())
    try:
        os.remove(filename)
        exit()
    except Exception as e:
        print(e)

start_time = datetime.datetime.now()
root = Tk()
clock = Label(root, font=('times', 20, 'bold'), bg='green')
clock.pack(fill=BOTH, expand=1)
root.protocol("WM_DELETE_WINDOW", on_closing)


def tick():
    global start_time
    # get the current local time from the PC
    now = datetime.datetime.now()
    # if time string has changed, update it
    td = now - start_time
    d = (datetime.datetime(1,1,1)+td)
    seconds = td.seconds
    hours_completed = int(seconds/(60*60))
    minutes_completed = int(seconds/(60))
    seconds_completed = int(seconds%(60))
    styl = "%s:%s:%s"%(d.hour,d.minute,d.second)
    clock.config(text=styl)
    # calls itself every 200 milliseconds
    # to update the time display as needed
    # could use >200 ms, but display gets jerky
    clock.after(1000, tick)
 

SHIFT = datetime.timedelta(hours = 7, minutes=40)
today = str(datetime.datetime.now().date())
filename = "is_running"+today+".txt"
file_exists = os.path.isfile("temp/"+filename)
if file_exists:
    exit()
else:
    file = open("temp/"+filename,'a')
    file.close() 
tick()
root.mainloop()