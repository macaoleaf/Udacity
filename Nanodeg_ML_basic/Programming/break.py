import webbrowser
import time

total_breaks = 3
count = 0

print("This program started on " + time.ctime())
while(count < total_breaks):
    time.sleep(2*60*60)
    webbrowser.open("https://www.youtube.com/watch?v=ro3EPPYbn44")
    count = count + 1
