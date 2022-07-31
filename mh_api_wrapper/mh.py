# mh.py
from .errors import MHAPIError, MHAPIInvalidResponse, MHAPIInvalidInformationGiven, MHAPIInvalidAuthentication, MHAPIUnknownException as err
import requests
class Minehut(object):
	def __init__(self, authtoken, sessid):
		self.authtoken = authtoken
		self.sessid = sessid
	def consoleCommand(self, command, serverid):
		baseurl = "https://api.minehut.com/"
		headers = {
			"Authorization": "{}".format(self.authtoken),
			"X-Session-ID": self.sessid
		}
		url = "https://api.minehut.com/" + "server/" + "{}".format(serverid) + "/send_command"
		payload = {
			"command": command
		}
		r = requests.post(url, headers=headers, json=payload)
		if r.status_code == 200:
			print(f'Command: {command} executed successfully. ({r.status_code}')
			return r.json()
		else:
			raise MHAPIInvalidResponse("Invalid response from MHAPI. Response code: {}".format(r.status_code))
			
	def getServerID(self, serverName):
		baseurl = "https://api.minehut.com/"
		headers = {
			"Authorization": "{}".format(self.authtoken),
			"X-Session-ID": self.sessid
		}
		url = baseurl + "server/" + "{}".format(serverName) + "?byName=true"
		r = requests.get(url, headers=headers)

		if r.status_code == 200:
			id = r.json()["server"]["_id"]
			return id
		else:
			raise MHAPIInvalidResponse("Invalid response from MHAPI. Response code: {}".format(r.status_code))
	def uploadFile(self, file, serverid, path):
		baseurl = "https://api.minehut.com/"
		headers = {
			"Authorization": "{}".format(self.authtoken),
			"X-Session-ID": self.sessid
		}
		url = baseurl + "file/" + "upload/" +"{}".format(serverid) + "/" + "{}".format(path)
		# convert file object to binary
		file_binary = file.read()
		
		# example payload: {"file": File (binary)}
		payload = {
			"file": file_binary
		}

		# request
		r = requests.post(url, headers=headers, files=payload)
		if r.status_code == 200:
			print(f'File uploaded successfully. Status Code: {r.status_code}')
			return r.json()
		else:
			raise MHAPIInvalidResponse(f"Invalid response from MHAPI. Response code: {r.status_code} {r.json} ")
	


		

	
