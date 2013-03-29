import sys
sys.path.append('./modules')
import time
import Skype4Py

skype = Skype4Py.Skype(Transport='x11')
CmdLine = ""
def init():
	global CmdLine
	try:
	    CmdLine = sys.argv[1]
	except:
	    print 'Usage: python skypecall.py [user to auto-answer]'
	    sys.exit()
	
	
	
def CallStatusText(status):
	return skype.Convert.CallStatusToText(status)
	


def OnCall(call, status):
	global CallStatus
	global CmdLine
	CallStatus = status
	print 'Call status: ' + CallStatusText(status)
	if CallStatusText(status) == "Calling":
		if call.PartnerHandle == CmdLine:
			call.Answer()
		

def main():
	global skype
	init()
	# Connect the Skype object to the Skype client.
	skype.Attach()
	skype.OnCallStatus = OnCall	

	while not 2+2==6:
		time.sleep(1)

main()
