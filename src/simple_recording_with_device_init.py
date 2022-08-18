import time
from pupil_labs.realtime_api.simple import Device

pi = None
while pi is None:
    pi = Device(address="pi.local", port="8080")

print(f"Connecting to {pi}...")

if pi is None:
    print("No device found.")
    raise SystemExit(-1)

recording_id = pi.recording_start()
print("started recording ", recording_id)
time.sleep(3)
pi.recording_cancel()
print("cancelled recording ")
pi.close()