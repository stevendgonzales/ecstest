"""Manage loading and return of test configuration settings."""

from os import environ as env


def _env_to_bool(envname, default_value=0):
    envval = env.get(envname, default_value)
    try:
        return bool(int(envval))
    except ValueError:
        raise Exception("Unsupported env value: %s=%s" % (envname, envval))


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
        'VERIFY_SSL': _env_to_bool('ECSTEST_VERIFY_SSL', 0),
        'REQUEST_TIMEOUT': float(env.get('ECSTEST_REQUEST_TIMEOUT', 15.0)),
        'TOKEN_FILENAME':
            env.get('ECSTEST_TOKEN_FILENAME', '/tmp/ecstest.token'),
        'CACHE_TOKEN': _env_to_bool('ECSTEST_CACHE_TOKEN', 1),
        'ACCESS_SSL': _env_to_bool('ECSTEST_ACCESS_SSL', 0),
        'ACCESS_SERVER': env.get('ECSTEST_ACCESS_SERVER', 'localhost'),
        'ACCESS_PORT': int(env.get('ECSTEST_ACCESS_PORT', 3128)),
        'ACCESS_KEY': env.get('ECSTEST_ACCESS_KEY', 'mykey'),
        'ACCESS_SECRET': env.get('ECSTEST_ACCESS_SECRET', 'mysecret'),
        'VERBOSE_OUTPUT': _env_to_bool('ECSTEST_VERBOSE_OUTPUT', 0)
    }
