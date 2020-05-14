class BaseConfig(object):
    '''
    Base config class
    '''
    DEBUG = True
    TESTING = False


class DevelopmentConfig(BaseConfig):
    """
    Development environment specific configuration
    """
    DEBUG = True
    TESTING = True