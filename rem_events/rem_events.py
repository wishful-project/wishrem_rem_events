from uniflex.core import events

__author__ = "Daniel Denkovski, Valentin Rakovic"
__copyright__ = "Copyright (c) 2017, Faculty of Electrical Engineering and Information Technologies, UKIM, Skopje, Macedonia"
__version__ = "0.1.0"
__email__ = "{danield, valentin}@feit.ukim.edu.mk"

'''	
REM events between REM controller and other controllers
'''

class REMGetDeviceInformationEvent(events.EventBase):
	'''
	Request information for a specific device for a given mac address
	'''
	def __init__(self, macaddress):
		super().__init__()
		self.macaddress = macaddress

class REMRspDeviceInformationEvent(events.EventBase):
	'''
	Response information for a specific device --> dictionary (channel capabilities, location, mode of operation, status, channel)
	'''
	def __init__(self, macaddress, deviceinfo):
		super().__init__()
		self.macaddress = macaddress
		self.deviceinfo = deviceinfo

class REMGetPathlossModel(events.EventBase):
	'''
	Request information for a pathloss model for a given channel
	'''
	def __init__(self, channel):
		super().__init__()
		self.channel = channel

class REMRspPathlossModel(events.EventBase):
	'''
	Response information for a pathloss model --> pl_model: dictionary (L0, alpha, sigma, d0)
	'''
	def __init__(self, channel, pl_model):
		super().__init__()
		self.channel = channel
		self.pl_model = pl_model

class REMGetTransmittersLocations(events.EventBase):
	'''
	Request information for transmitters locations for channel, floor and timespan
	'''
	def __init__(self, channel, floor, timespan):
		super().__init__()
		self.channel = channel
		self.floor = floor
		self.timespan = timespan

class REMRspTransmittersLocations(events.EventBase):
	'''
	Response information for transmitters locations on a channel and floor --> tx_loc: list of tupples (mac, x and y coordinates, global location id, tx power)
	'''
	def __init__(self, channel, floor, tx_loc):
		super().__init__()
		self.channel = channel
		self.floor = floor
		self.tx_loc = tx_loc

class REMGetChannelStatus(events.EventBase):
	'''
	Request information for channel status for a given channel, duty cycle threshold and timespan
	'''
	def __init__(self, channel, threshold, timespan):
		super().__init__()
		self.channel = channel
		self.threshold = threshold
		self.timespan = timespan

class REMRspChannelStatus(events.EventBase):
	'''
	Response information for channel status on a given channel --> status: (0--> free, 1--> ocupied)
	'''
	def __init__(self, channel, status):
		super().__init__()
		self.channel = channel
		self.status = status

class REMGetChannelStatusByArea(events.EventBase):
	'''
	Request information for channel status for a given rectangle area ((ulx,uly),(drx,dry)), duty cycle threshold and timespan
	'''
	def __init__(self, channel, threshold, timespan, ulx, uly, drx, dry):
		super().__init__()
		self.channel = channel
		self.threshold = threshold
		self.timespan = timespan
		self.ulx = ulx
		self.uly = uly
		self.drx = drx
		self.dry = dry

class REMRspChannelStatusByArea(events.EventBase):
	'''
	Response information for channel status in a given rectangle area --> status: (0--> free, 1--> ocupied)
	'''
	def __init__(self, channel, ulx, uly, drx, dry, status):
		super().__init__()
		self.channel = channel
		self.ulx = ulx
		self.uly = uly
		self.drx = drx
		self.dry = dry
		self.status = status

class REMGetChannelStatusByDevice(events.EventBase):
	'''
	Request information for channel status for a given channel, device (mac address), duty cycle threshold and timespan
	'''
	def __init__(self, channel, rx_addr, threshold, timespan):
		super().__init__()
		self.channel = channel
		self.rx_addr = rx_addr
		self.threshold = threshold
		self.timespan = timespan

class REMRspChannelStatusByDevice(events.EventBase):
	'''
	Response information for channel status for a given device --> status: (0--> free, 1--> ocupied)
	'''
	def __init__(self, channel, rx_addr, status):
		super().__init__()
		self.channel = channel
		self.rx_addr = rx_addr
		self.status = status

class REMGetAllChannelsStatusByDevice(events.EventBase):
	'''
	Request information for all channels status for a given device (mac address), duty cycle threshold and timespan
	'''
	def __init__(self, rx_addr, threshold, timespan):
		super().__init__()
		self.rx_addr = rx_addr
		self.threshold = threshold
		self.timespan = timespan

class REMRspAllChannelsStatusByDevice(events.EventBase):
	'''
	Response information for all channels status for a given device --> status: list of tuple (channel, channel status) (0--> free, 1--> ocupied)
	'''
	def __init__(self, rx_addr, status):
		super().__init__()
		self.rx_addr = rx_addr
		self.status = status

class REMGetAllChannelsStatus(events.EventBase):
	'''
	Request information for all channels status for a given duty cycle threshold and timespan
	'''
	def __init__(self, threshold, timespan):
		super().__init__()
		self.threshold = threshold
		self.timespan = timespan

class REMRspAllChannelsStatus(events.EventBase):
	'''
	Response information for all channels status --> status: list of tuple (channel, channel status) (0--> free, 1--> ocupied)
	'''
	def __init__(self, status):
		super().__init__()
		self.status = status

class REMGetDutyCycle(events.EventBase):
	'''
	Request information for average duty cycle on channel and in timespan
	'''
	def __init__(self, channel, timespan):
		super().__init__()
		self.channel = channel
		self.timespan = timespan

class REMRspDutyCycle(events.EventBase):
	'''
	Response information for average duty cycle on channel
	'''
	def __init__(self, channel, dc):
		super().__init__()
		self.channel = channel
		self.dc = dc

class REMGetDutyCycleByArea(events.EventBase):
	'''
	Request information for average duty cycle on channel, in timespan and in rectangle area ((ulx, uly), (drx, dry))
	'''
	def __init__(self, channel, timespan, ulx, uly, drx, dry):
		super().__init__()
		self.channel = channel
		self.timespan = timespan
		self.ulx = ulx
		self.uly = uly
		self.drx = drx
		self.dry = dry

class REMRspDutyCycleByArea(events.EventBase):
	'''
	Response information for average channel duty cycle in rectangle area
	'''
	def __init__(self, channel, ulx, uly, drx, dry, dc):
		super().__init__()
		self.channel = channel
		self.ulx = ulx
		self.uly = uly
		self.drx = drx
		self.dry = dry
		self.dc = dc

class REMGetDutyCycleByDevice(events.EventBase):
	'''
	Request information for average channel duty cycle for a given device in a given timespan 
	'''
	def __init__(self, channel, rx_add, timespan):
		super().__init__()
		self.channel = channel
		self.rx_add = rx_add
		self.timespan = timespan

class REMRspDutyCycleByDevice(events.EventBase):
	'''
	Response information for average channel duty cycle from device
	'''
	def __init__(self, channel, rx_add, dc):
		super().__init__()
		self.channel = channel
		self.rx_add = rx_add
		self.dc = dc

class REMGetDutyCycleAllChannelsByDevice(events.EventBase):
	'''
	Request information for average duty cycle for all channels, given device and in a given timespan 
	'''
	def __init__(self, channel, rx_add, timespan):
		super().__init__()
		self.channel = channel
		self.rx_add = rx_add
		self.timespan = timespan

class REMRspDutyCycleAllChannelsByDevice(events.EventBase):
	'''
	Response information for average duty cycle for all channels from device --> dc: list of tupple (channel, duty cycle)
	'''
	def __init__(self, rx_add, dc):
		super().__init__()
		self.rx_add = rx_add
		self.dc = dc

class REMGetDutyCycleAllChannels(events.EventBase):
	'''
	Request information for average duty cycle for all channels in a given timespan 
	'''
	def __init__(self, timespan):
		super().__init__()
		self.timespan = timespan

class REMRspDutyCycleAllChannels(events.EventBase):
	'''
	Response information for average duty cycle for all channels --> dc: list of tupple (channel,duty cycle)
	'''
	def __init__(self, dc):
		super().__init__()
		self.dc = dc

class REMGetDutyCycleHeatMap(events.EventBase):
	'''
	Request heat map of duty cycle for a given timespan in a given area (rectangle ((ulx,uly),(drx,dry)), with resolution (nx X ny)
	'''
	def __init__(self, channel, timespan, nx, ny, ulx, uly, drx, dry):
		super().__init__()
		self.channel = channel
		self.timespan = timespan
		self.nx = nx
		self.ny = ny
		self.ulx = ulx
		self.uly = uly
		self.drx = drx
		self.dry = dry

class REMRspDutyCycleHeatMap(events.EventBase):
	'''
	Response information for duty cycle heat map for channel --> val: tuple consisted of x,y and interpolated dc
	'''
	def __init__(self, channel, val):
		super().__init__()
		self.channel = channel
		self.val = val

class REMGetEstimatedTXLocation(events.EventBase):
	'''
	Request location estimation for device (mac address) for a given timespan in a given area (rectangle ((ulx,uly),(drx,dry)), with resolution (nx X ny)
	'''
	def __init__(self, addr, timespan=60, ulx=0, uly=15, drx=32, dry=0, nx=10, ny=10, nz=10):
		super().__init__()
		self.addr = addr
		self.timespan = timespan
		self.ulx = ulx
		self.uly = uly
		self.drx = drx
		self.dry = dry
		self.nx = nx
		self.ny = ny
		self.nz = nz

class REMRspEstimatedTXLocation(events.EventBase):
	'''
	Response information for estimated location of device --> val: tuple consisted of estimated x,y,z coordinates and respective estimated tx power (x,y,z,txpow)
	'''
	def __init__(self, addr, val):
		super().__init__()
		self.addr = addr
		self.val = val

class REMGetOccupiedChannels(events.EventBase):
	'''
	Request active channels
	'''
	def __init__(self):
		super().__init__()

class REMRspOccupiedChannels(events.EventBase):
	'''
	Response with the list of active channels
	'''
	def __init__(self, ac):
		super().__init__()
		self.ac = ac

class REMGetOccupiedChannelsCount(events.EventBase):
	'''
	Request number of active APs per channel
	'''
	def __init__(self):
		super().__init__()

class REMRspOccupiedChannelsCount(events.EventBase):
	'''
	Response with number of active APs per channel --> acl: tupple (active APs count, channel)
	'''
	def __init__(self, acl):
		super().__init__()
		self.acl = acl

class REMGetAllAPStatistics(events.EventBase):
	'''
	Request average statistics from all active APs in a given timespan
	'''
	def __init__(self, timespan = 1):
		super().__init__()
		self.timespan = timespan

class REMRspAllAPStatistics(events.EventBase):
	'''
	Response average statistics from all active APs --> stats: tupple (ap_mac_address, avg_tx_retries, avg_tx_failed, avg_tx_throughput, avg_rx_throughput, avg_tx_activity, avg_rx_activity)
	'''
	def __init__(self, stats):
		super().__init__()
		self.stats = stats

class REMGetDegradedAPsBasedOnRetries(events.EventBase):
	'''
	Request degraded APs based on retries threshold in a given timespan
	'''
	def __init__(self, timespan=1, retries_threshold=10):
		super().__init__()
		self.timespan = timespan
		self.retries_threshold = retries_threshold

class REMRspDegradedAPs(events.EventBase):
	'''
	Response list of degraded APs (mac addresses)
	'''
	def __init__(self, degraded):
		super().__init__()
		self.degraded = degraded

class REMGetAllActiveDevicesOnChannel(events.EventBase):
	'''
	Request all active devices on channel
	'''
	def __init__(self, channel, timespan):
		super().__init__()
		self.channel = channel
		self.timespan = timespan

class REMRspAllActiveDevicesOnChannel(events.EventBase):
	'''
	Response all active devices on channel --> activedevs: list of devices (mac addresses)
	'''
	def __init__(self, channel, activedevs):
		super().__init__()
		self.channel = channel
		self.activedevs = activedevs

class REMCalculatePathLossModel(events.EventBase):
	'''
	Request calculation of path loss model on channel in a given timespan
	'''
	def __init__(self, channel, timespan):
		super().__init__()
		self.channel = channel
		self.timespan = timespan

