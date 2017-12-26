from common.log import logUtils as log
from common.ripple import userUtils
from constants import clientPackets
from objects import glob
import json

def handle(userToken, packetData):
	# Friend add packet
	packetData = clientPackets.addRemoveFriend(packetData)
	userUtils.addFriend(userToken.userID, packetData["friendID"])
	jsonData = json.dumps({"from":userToken.userID, "userID":str(packetData["friendID"]), "action":1})
	glob.redis.publish("apipy:notify", jsonData)
	# Console output
	log.info("{} have added {} to their friends".format(userToken.username, str(packetData["friendID"])))
