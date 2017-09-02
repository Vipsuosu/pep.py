from constants import clientPackets
from constants import serverPackets
from helpers import chatHelper as chat
from common.ripple import userUtils
from objects import glob
from common.log import logUtils as log

def handle(userToken, packetData):
	# Send private message packet
	packetData = clientPackets.sendPrivateMessage(packetData)
	targetToken = glob.tokens.getTokenFromUsername(packetData["to"], safe=False)
	if targetToken is not None:
		if(userToken.admin == False and targetToken.BlockNonFriendPM == True):
			toId = targetToken.userID
			if glob.db.fetch("SELECT id FROM users_relationships WHERE user1 = %s AND user2 = %s LIMIT 1", [userToken.userID, toId]) is None:
				userToken.enqueue(serverPackets.UserPMBlocked(userToken.username, userToken.userID, packetData["to"], packetData["message"]))
			else:
				chat.sendMessage(token=userToken, to=packetData["to"], message=packetData["message"])
		else:
			chat.sendMessage(token=userToken, to=packetData["to"], message=packetData["message"])