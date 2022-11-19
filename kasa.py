from kasa import Discover


def get_devices():
    devices = Discover.discover()
    return devices
