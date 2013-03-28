import sys
sys.path.append('./modules')
import time
import Skype4Py


def init():

	try:
	    CmdLine = sys.argv[1]
	except:
	    print 'Usage: python skypecall.py [user to auto-answer]'
	    sys.exit()
	
	def CallStatusText(status):
		return skype.Convert.CallStatusToText(status)
	skype = Skype4Py.Skype(Transport='x11')


def OnCall(call, status):
	global CallStatus
	CallStatus = status
	print 'Call status: ' + CallStatusText(status)
	if CallStatusText(status) == "Calling":
		if call.PartnerHandle == CmdLine:
			call.Answer()
		

def main():
	
	# Connect the Skype object to the Skype client.
	skype.Attach()
	skype.OnCallStatus = OnCall	

	while not 2+2==5:
		time.sleep(1)
	
main()
