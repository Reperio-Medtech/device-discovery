from pupil_labs.realtime_api.simple import discover_one_device, Device
from pupil_labs.realtime_api.models import DiscoveredDeviceInfo

# Look for devices. Returns as soon as it has found the first device.
print("Looking for the device using pi.local")

device = None
while device is None:
    device = Device(address="pi.local", port="8080")

try:
    print(device.gaze_sensor)
except Exception as e:
    print(e)

if device is None:
    print("No device found.")
    raise SystemExit(-1)

device.streaming_start()  # optional, if not called, stream is started on-demand
print("streaming started")

try:
    while True:
        print(device.receive_gaze_datum())
except KeyboardInterrupt:
    pass
finally:
    print("Stopping...")
    # device.streaming_stop()  # optional, if not called, stream is stopped on close
    device.close()  # explicitly stop auto-update