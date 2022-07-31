from mh_api_wrapper.mh import Minehut

authtoken = "YOUR_AUTH_TOKEN"
sessid = "YOUR_SESSION_ID"
mh = Minehut(authtoken, sessid)
mh.consoleCommand('/say Hello World!', '5bba8f6ce5ede455ce39b398')