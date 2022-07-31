# errors
class MHAPIError(Exception):
	"""Base class for all MHAPI errors"""
	pass

class MHAPIInvalidResponse(MHAPIError):
	"""Invalid response from MHAPI"""
	pass

class MHAPIInvalidInformationGiven(MHAPIError):
	"""Invalid information given to MHAPI"""
	pass

class MHAPIInvalidAuthentication(MHAPIError):
	"""Invalid authentication"""
	pass

class MHAPIUnknownException(MHAPIError):
	"""Unknown exception"""
	pass