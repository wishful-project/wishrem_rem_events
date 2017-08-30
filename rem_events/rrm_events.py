from uniflex.core import events

__author__ = "Daniel Denkovski, Valentin Rakovic"
__copyright__ = "Copyright (c) 2017, Faculty of Electrical Engineering and Information Technologies, UKIM, Skopje, Macedonia"
__version__ = "0.1.0"
__email__ = "{danield, valentin}@feit.ukim.edu.mk"

'''	
RRM events between node controller and RRM controller
'''

class RRMRegister(events.EventBase):
	'''	
	Carries the event information for connecting a specific RRM with the node controller
	'''
	def __init__(self):
		super().__init__()

class RRMRequestAPConfiguration(events.EventBase):
	'''	
	Trigger event, which requires the (re)configuration (RRM optimization) of a given access point
	'''
	def __init__(self, apmac):
		super().__init__()
		self.macaddr = apmac

class RRMReconfigureAP(events.EventBase):
	'''	
	Carries information regarding the (re)configuration setup for a given access point
	'''
	def __init__(self, macaddr, ssid, power, channel, hw_mode, ht_capab):
		super().__init__()
		self.macaddr = macaddr
		self.ssid = ssid
		self.power = power
		self.channel = channel
		self.hw_mode = hw_mode
		self.ht_capab = ht_capab

class RRMEvaluationTimeEvent(events.TimeEvent):
	'''	
	Trigger a periodic RRM re-evaluation in the RRM controller
	'''
	def __init__(self):
		super().__init__()
		
