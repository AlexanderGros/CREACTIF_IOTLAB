import pycom
import time

pycom.heartbeat(False)
for cycles in range(5): # stop after 10 cycles
    pycom.rgbled(0x007f00) # green
    time.sleep(1)
    pycom.rgbled(0x7f7f00) # yellow
    time.sleep(1)
    pycom.rgbled(0x7f0000) # red
    time.sleep(1)

# last value will be kept in memory if no heartbeat

# reactivate heartbeat if you want
pycom.heartbeat(True)
