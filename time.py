import time

start = time.time()

while 1:
	time_elapsed = time.time() - start
	print time_elapsed
	time.sleep(.5)