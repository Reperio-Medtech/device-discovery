from pupil_labs.realtime_api.simple import discover_one_device, Device

from pupil_labs.realtime_api import Device, Network, receive_gaze_data

from pupil_labs.realtime_api.models import DiscoveredDeviceInfo

pi = None
while pi is None:
    pi = DiscoveredDeviceInfo(name="", server= "pi.local.", port="8080", addresses=['pi.local'])
    # pi = Device(address="pi.local", port="8080")

dev = Device.from_discovered_device(pi)



print(dev.get_status())
