import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
	"""docstring for Config"""
	DEBUG = False
	TESTING = False
	CSRF_ENABLED = True
	SECRET_KEY = 'my-best-budy-is-doodle-bug'

class ProductionConfig(Config):
	"""docstring for ProductionConfig"""
	DEBUG = False

class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True

class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True

class TestingConfig(Config):
    TESTING = True
		
		