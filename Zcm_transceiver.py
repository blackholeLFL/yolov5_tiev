import time
from zerocm import ZCM
import MsgTrafficLightSignal

class ZcmTransceiver(object):
    def __init__(self):
        self.transceiver = ZCM('ipc')
        if not self.transceiver.good():
            print("Unable to initialize ZeroCM")
            exit(-1)

    def __call__(self, left: bool = True, forward: bool = True, right: bool = True):
        msg_traffic_light_signal = MsgTrafficLightSignal()
        msg_traffic_light_signal.timestamp = int(time.time())
        msg_traffic_light_signal.turn_signal = bytes([int(left),int(forward),int(right)])
        self.transceiver.publish("msgTrafficLightSignal", msg_traffic_light_signal)
