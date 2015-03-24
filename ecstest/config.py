"""Manage loading and return of test configuration settings."""

from os import environ as env

def __env_to_bool(envname, default_value=False):
    v = env.get(envname)
    if v == '1':
        return True
    elif v == '0':
        return False
    elif v == None or v == '':
        return default_value
    else:
        raise Exception("Unrecognized environment variable: %s=%s" % (envname,v))

def get_config():
    """Return a dictionary of configuration values."""

    return {
        'ADMIN_USERNAME': env.get('ECSTEST_ADMIN_USERNAME', 'username'),
        'ADMIN_PASSWORD': env.get('ECSTEST_ADMIN_PASSWORD', 'password'),
        'TOKEN': env.get('ECSTEST_TOKEN', None),
        'CONTROL_ENDPOINT':
            env.get('ECSTEST_CONTROL_ENDPOINT', 'https://127.0.0.1:4443'),
        'TOKEN_ENDPOINT':
            env.get('ECSTEST_TOKEN_ENDPOINT', 'https://127.0.0.1:4443/login'),
        'VERIFY_SSL': __env_to_bool('ECSTEST_VERIFY_SSL', False),
        'REQUEST_TIMEOUT': float(env.get('ECSTEST_REQUEST_TIMEOUT', 15.0)),
        'TOKEN_FILENAME': env.get('ECSTEST_TOKEN_FILENAME', '/tmp/ecstest.token'),
        'CACHE_TOKEN': __env_to_bool('ECSTEST_CACHE_TOKEN', True),
        'ACCESS_SSL': __env_to_bool('ECSTEST_ACCESS_SSL', False),
        'ACCESS_SERVER': env.get('ECSTEST_ACCESS_SERVER', 'localhost'),
        'ACCESS_PORT': int(env.get('ECSTEST_ACCESS_PORT', 3128)),
        'ACCESS_KEY': env.get('ECSTEST_ACCESS_KEY', 'mykey'),
        'ACCESS_SECRET': env.get('ECSTEST_ACCESS_SECRET', 'mysecret'),
        'VERBOSE_OUTPUT': __env_to_bool('ECSTEST_VERBOSE_OUTPUT', False)
    }
