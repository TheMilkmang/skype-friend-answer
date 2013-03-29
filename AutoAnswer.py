import sys
sys.path.append('./modules')
import time
import Skype4Py

#Will segfault if Transoprt='x11' isn't there
skype = Skype4Py.Skype(Transport='x11')
#global cmdLine variable. So far is only used for adding people to the auto-answer list
cmdLine = ""

def init():
	global cmdLine
	cmdLine = sys.argv
	print 'args: ' + str(len(cmdLine))
	
	#if no contact is specified
	if len(cmdLine) < 2:
		print 'Usage: python AutoAnswer.py [user] [user2] [user3] etc...'
		sys.exit()
		
	# Connect the Skype object to the Skype client.
	try:
		skype.Attach()
	except Skype4Py.errors.SkypeAPIError:
		print "could not attach, exiting"
		sys.exit()
	#run these functions when these things happen
	skype.OnCallStatus = onCall	
		
#converts skype call status to readable text
def callStatusText(status):
	return skype.Convert.CallStatusToText(status)

#Runs when call status changes
def onCall(call, status):
	global callStatus
	global cmdLine
	callStatus = status
	print 'Call status: ' + callStatusText(status)
	
	if callStatusText(status) == "Calling":
		if call.PartnerHandle in cmdLine:
			call.Answer()
		else:
			print 'no auto answer for', call.PartnerHandle

def main():
	
	while True:
		time.sleep(1)
		print skype.AttachmentStatus
		print skype.Convert.AttachmentStatusToText(skype.AttachmentStatus)
		if not skype.AttachmentStatus == 0:
			if skype.AttachmentStatus == Skype4Py.apiAttachAvailable:
				try:
					skype.Attach()
				except Skype4Py.errors.SkypeAPIError:
					print "could not attach, maybe you're not logged in yet"
			
		
init()
main()
