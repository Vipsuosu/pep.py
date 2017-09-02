from constants import clientPackets
from objects import glob
from common.log import logUtils as log

def handle(userToken, packetData):
	packetData = clientPackets.UserToggleBlockNonFriendPM(packetData)
	userToken.BlockNonFriendPM = True if packetData["test"] == 1 else False