from constants import clientPackets
from objects import glob

def handle(userToken, packetData):
	# Get usertoken data
	userID = userToken.userID

	# Read packet data
	packetData = clientPackets.changeSlot(packetData)
	if userToken.matchID not in glob.matches.matches:
		return
	with glob.matches.matches[userToken.matchID] as match:
		# Change slot
		match.userChangeSlot(userID, packetData["slotID"])
