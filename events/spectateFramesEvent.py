from objects import glob
from constants import serverPackets
from constants import clientPackets
from common.log import logUtils as log

def handle(userToken, packetData):
	# get token data
	userID = userToken.userID

	# Send spectator frames to every spectator
	streamName = "spect/{}".format(userID)
	if(userToken.allowed == 0):
		log.info(clientPackets.spectatorFrames(packetData))
	glob.streams.broadcast(streamName, serverPackets.spectatorFrames(packetData[7:]))