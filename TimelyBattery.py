import psutil
import threading
from datetime import datetime
import subprocess as subp

def notify():
	battery = psutil.sensors_battery()
	percent = battery.percent
	current_time = datetime.now().strftime("%H:%M:%S")
	threading.Timer(600.0, notify).start()
	if percent > 95:
		subp.call(['notify-send',"          Overloaded: Battery: "+str(percent)[:5]+ "   Time: " + current_time]  ,0)
	elif percent > 80: 
		subp.call(['notify-send',"  Disconnect Charger: Battery: "+str(percent)[:5]+ "   Time: " + current_time]  ,0)
	elif percent < 40: 
		subp.call(['notify-send',"     Connect Charger: Battery: "+str(percent)[:5]+ "   Time: " + current_time]  ,0)
	elif percent < 10:
		subp.call(['notify-send',"    Battery Critical: Battery: "+str(percent)[:5]+ "   Time: " + current_time]  ,0)
	else: 
		subp.call(['notify-send',"       Optimal Range: Battery: "+str(percent)[:5]+ "   Time: " + current_time]  ,0)
notify()