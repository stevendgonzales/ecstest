"""Manage loading and return of test configuration settings."""

from os import environ as env


def get_config():
    """Return a dictionary of configuration values."""

    return {
        'ADMIN_USERNAME': env.get('ADMIN_USERNAME', 'username'),
        'ADMIN_PASSWORD': env.get('ADMIN_PASSWORD', 'password'),
        'TOKEN': env.get('TOKEN', None),
        'ECS_CONTROL_ENDPOINT':
            env.get('ECS_CONTROL_ENDPOINT', 'https://127.0.0.1:4443'),
        'ECS_TOKEN_ENDPOINT':
            env.get('ECS_TOKEN_ENDPOINT', 'https://127.0.0.1:4443/login'),
        'VERIFY_SSL': bool(int(env.get('VERIFY_SSL', 0))),
        'REQUEST_TIMEOUT': float(env.get('REQUEST_TIMEOUT', 15.0)),
        'TOKEN_FILENAME': env.get('TOKEN_FILENAME', '/tmp/ecstest.token'),
        'CACHE_TOKEN': bool(int(env.get('CACHE_TOKEN', 1))),
        'ACCESS_SSL': bool(int(env.get('ACCESS_SSL', 0))),
        'ACCESS_SERVER': env.get('ACCESS_SERVER', 'localhost'),
        'ACCESS_PORT': int(env.get('ACCESS_PORT', 3128)),
        'ACCESS_KEY': env.get('ACCESS_KEY', 'mykey'),
        'ACCESS_SECRET': env.get('ACCESS_SECRET', 'mysecret'),
        'ECSTEST_VERBOSE_OUTPUT': env.get('ECSTEST_VERBOSE_OUTPUT', None)
    }
