from uniflex.core import events

__author__ = "Daniel Denkovski"
__copyright__ = "Copyright (c) 2017, Faculty of Electrical Engineering and Information Technologies, UKIM, Skopje, Macedonia"
__version__ = "0.1.0"
__email__ = "{danield}@feit.ukim.edu.mk"

'''	
Sensing and control events between node controller and WiFi devices
'''

class WiFiRssiSampleEvent(events.EventBase): #events.GenericRadioDeviceEvent?
	'''
	Carries information, from a WiFi monitoring device to the node controller, regarding the sensed RSSI on a specific channel, from a specific WiFi transmitter
	'''
	def __init__(self, ra, ta, rssi, chnel):
		super().__init__()
		self.ra = ra
		self.ta = ta
		self.receiverUuid = None
		self.rssi = rssi
		self.chnel = chnel

class WiFiDutyCycleSampleEvent(events.EventBase): #events.GenericRadioDeviceEvent?
	'''
	Carries information, from a WiFi monitoring device to the node controller, regarding the duty cycle value on a specific channel, as observed by the WiFi monitoring device
	'''
	def __init__(self, ra, dc, chnel):
		super().__init__()
		self.ra = ra
		self.receiverUuid = None
		self.dc = dc
		self.chnel = chnel

class WiFiConfigureAP(events.EventBase):
	'''
	Carries information, from the node controller to a WiFi device, with respect to the reconfiguration parameters that trigger the device to (re)configure in access point mode
	'''
	def __init__(self, macaddr, ssid, power, channel, hw_mode, ht_capab):
		super().__init__()
		self.receiverUuid = None
		self.macaddr = macaddr
		self.ssid = ssid
		self.power = power
		self.channel = channel
		self.hw_mode = hw_mode
		self.ht_capab = ht_capab

class WiFiConfigureAPRsp(events.EventBase):
	'''
	Response of an access point regarding the initiated (re)configuration process
	'''
	def __init__(self, macaddr, ap_config):
		super().__init__()
		self.macaddr = macaddr
		self.ap_config = ap_config

class WiFiConfigureStation(events.EventBase):
	'''
	Carries information, from the node controller to a WiFi device, with respect to the reconfiguration parameters that trigger the device to (re)configure in station mode
	'''
	def __init__(self, macaddr, ssid, ap, power, channel):
		super().__init__()
		self.receiverUuid = None
		self.macaddr = macaddr
		self.ssid = ssid
		self.ap = ap
		self.power = power
		self.channel = channel

class WiFiConfigureStationRsp(events.EventBase):
	'''
	Response of a station regarding the initiated (re)configuration process
	'''
	def __init__(self, macaddr, apmac, sta_config):
		super().__init__()
		self.macaddr = macaddr
		self.apmac = apmac
		self.sta_config = sta_config

class WiFiConfigureMonitor(events.EventBase):
	'''
	Carries information, from the node controller to a WiFi device that trigger the device to (re)configure in monitor mode
	'''
	def __init__(self, macaddr):
		super().__init__()
		self.receiverUuid = None
		self.macaddr = macaddr

class WiFiConfigureMonitorRsp(events.EventBase):
	'''
	Response of a WiFi monitoring device regarding the initiated (re)configuration process
	'''
	def __init__(self, macaddr):
		super().__init__()
		self.macaddr = macaddr

class WiFiGetCapabilities(events.EventBase):
	'''
	Triggers a WiFi device to report its capabilities to the node controller
	'''
	def __init__(self, uuid):
		super().__init__()
		self.receiverUuid = uuid

class WiFiCapabilities(events.EventBase):
	'''
	Carries information, from a WiFi device to the node controller, regarding the device’s capabilities
	'''
	def __init__(self, macaddr, capabilities):
		super().__init__()
		self.macaddr = macaddr
		self.capabilities = capabilities

class WiFiStopAll(events.EventBase):
	'''
	Event that stops all activities on a given WiFi device
	'''
	def __init__(self, macaddr):
		super().__init__()
		self.receiverUuid = None
		self.macaddr = macaddr

class WiFiLinkStatistics(events.EventBase):
	'''
	Carries information, from a WiFi device to the node controller, regarding link statistics
	'''
	def __init__(self, txmac, rxmac, rssi, tx_retries, tx_failed, tx_rate, rx_rate, tx_thr, rx_thr, tx_activity, rx_activity):
		super().__init__()
		self.txmac = txmac
		self.rxmac = rxmac
		self.rssi = rssi #in dBm
		self.tx_retries = tx_retries #in percents
		self.tx_failed = tx_failed #in percents
		self.tx_rate = tx_rate #in bps
		self.rx_rate = rx_rate #in bps
		self.tx_throughput = tx_thr #in bps
		self.rx_throughput = rx_thr #in bps
		self.tx_activity = tx_activity #in percents
		self.rx_activity = rx_activity #in percents

class WiFiAPStatistics(events.EventBase):
	'''
	Carries information, from a WiFi access point to the node controller, regarding access point communication statistics
	'''
	def __init__(self, apmac, stations, total_tx_retries, total_tx_failed, total_tx_thr, total_rx_thr, total_tx_activity, total_rx_activity):
		super().__init__()
		self.apmac = apmac
		self.stations = stations
		self.total_tx_retries = total_tx_retries #in percents
		self.total_tx_failed = total_tx_failed #in percents
		self.total_tx_throughput = total_tx_thr #in bps
		self.total_rx_throughput = total_rx_thr #in bps
		self.total_tx_activity = total_tx_activity #in percents
		self.total_rx_activity = total_rx_activity #in percents

class PeriodicEvaluationTimeEvent(events.TimeEvent):
	'''
	Local time event to trigger a WiFi device for a periodic (re)evaluation
	'''
	def __init__(self):
		super().__init__()

class ConnectionTimeoutEvent(events.TimeEvent):
	def __init__(self):
		super().__init__()
