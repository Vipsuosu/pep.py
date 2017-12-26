from common.log import logUtils as log
from common.ripple import userUtils
from constants import clientPackets
from objects import glob
import json

def handle(userToken, packetData):
	# Friend remove packet
	packetData = clientPackets.addRemoveFriend(packetData)
	userUtils.removeFriend(userToken.userID, packetData["friendID"])
	jsonData = json.dumps({"from":userToken.userID, "userID":str(packetData["friendID"]), "action":2})
	glob.redis.publish("apipy:notify", jsonData)
	# Console output
	log.info("{} have removed {} from their friends".format(userToken.username, str(packetData["friendID"])))
