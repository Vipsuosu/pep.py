from objects import glob
from constants import clientPackets
from common.log import logUtils as log


def handle(userToken, packetData):
	# Get packet data
	packetData = clientPackets.transferHost(packetData)

	# Get match ID and match object
	matchID = userToken.matchID

	# Make sure we are in a match
	if matchID == -1:
		return

	# Make sure the match exists
	if matchID not in glob.matches.matches:
		return

	# Match exists, get object
	match = glob.matches.matches[matchID]

	# Host check
	if userToken.userID != match.hostUserID:
		return

	# Transfer host
	log.error("match {} | host {} transferHost to {}".format(matchID,userToken.userID,packetData["slotID"]))
	match.transferHost(packetData["slotID"])
