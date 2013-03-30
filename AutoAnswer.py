import sys
sys.path.append('./modules')
import time
import Skype4Py


skype = Skype4Py.Skype(Transport='x11')		#Will segfault if Transoprt='x11' isn't there
cmdLine = "" 								#global cmdLine variable. So far is only used for adding people to the auto-answer list

def init():
	global cmdLine
	cmdLine = sys.argv
	print 'args: ' + str(len(cmdLine))

	if len(cmdLine) < 2:					#if no contact is specified
		print 'Usage: python AutoAnswer.py [user] [user2] [user3] etc...'
		sys.exit()
		
	try: 									#Connect the Skype object to the Skype client.
		skype.Attach()
	except Skype4Py.errors.SkypeAPIError:
		print "could not attach, are you logged in?"
		
	skype.OnCallStatus = onCall				#run these functions when these things happen
		

def callStatusText(status):					#converts skype call status to readable text
	return skype.Convert.CallStatusToText(status)

def onCall(call, status):					#Runs when call status changes
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
	
	while True:								#run forever~
		time.sleep(1)

		while not skype.AttachmentStatus == 0:#if skype isn't attached, keep retrying until it works
				try:
					skype.Attach()
				except Skype4Py.errors.SkypeAPIError:
					print "could not attach, maybe you're not logged in yet."
				time.sleep(10)
			
		
init()
main()
