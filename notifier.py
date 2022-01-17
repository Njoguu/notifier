from plyer import notification		# --> to send notification
import psutil						# --> get data back from laptop sensors
import time


if __name__=="__main__":

	battery = psutil.sensors_battery()

	# CHECK BATTERY
	if battery.percent == 100:
	    # SEND NOTIFICATION
		notification.notify(title='Battery Full!', 
							message='Your laptop is fully charged. Please remove from charger!', 
							app_name='Charger', 
							app_icon=None, 
							timeout=5, 
							toast=True)

	# 