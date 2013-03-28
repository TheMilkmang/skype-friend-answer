import Skype4Py
import time
import sys

try:
    CmdLine = sys.argv[1]
except:
    print 'Usage: python skypecall.py [user to auto-answer]'
    sys.exit()

def CallStatusText(status):
	return skype.Convert.CallStatusToText(status)


def OnCall(call, status):
	global CallStatus
	CallStatus = status
	print 'Call status: ' + CallStatusText(status)
	if CallStatusText(status) == "Calling":
		if call.PartnerHandle == CmdLine:
			call.Answer()
		

# Create an instance of the Skype class.
skype = Skype4Py.Skype(Transport='x11')
# Connect the Skype object to the Skype client.
skype.Attach()
skype.OnCallStatus = OnCall	

while not 2+2==5:
	time.sleep(1)
	
	
