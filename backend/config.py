class BaseConfig(object):
	DEBUG = True
	DEVELOPMENT = True
	SECRET_KEY = "MAKE_THIS_SECURE"
	MONGODB_SETTINGS = {
		# 'USERNAME': None,
		# 'PASSWORD': None,
		'HOST': '127.0.0.1',
		'PORT': 27017,
		'DB': 'cfp'
	}

class ProductionConfig(object):
	DEBUG = False
	DEVELOPMENT = False