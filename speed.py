import time
Max_speed = 30
Min_time =2
input("Press any button to start")
Camera_A = time.time()
input("Press any button to stop")
Camera_B = time.time()
Time_taken = Camera_B - Camera_A
if Time_taken >= Min_time:
	print("Vehicle is within limit")
else:
	print("Vehicle is speeding")
