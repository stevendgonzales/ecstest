"""Test client classes for interacting with the EMC ECS control/data planes.

Test clients allow the creation of both valid and invalid requests and return
low level response objects for use in TestCase assertions.
"""

import requests

from ecstest import constants


class EcsControlPlaneClient(object):

    def __init__(self, username=None, password=None, token=None,
                 ecs_endpoint=None, token_endpoint=None, verify_ssl=False,
                 token_filename='/tmp/ecstest.token',
                 request_timeout=15.0, cache_token=True):
        """
        Creates an instance of client class used for interacting
        with the ECS control plane.

        :param username: The username to fetch a token
        :param password: The password to fetch a token
        :param token: Supply a valid token to use instead of username/password
        :param ecs_endpoint: The URL where ECS is located
        :param token_endpoint: The URL where the ECS login is located
        :param verify_ssl: Verify SSL certificates
        :param token_filename: The name of the cached token filename
        :param request_timeout: How long to wait for ECS to respond
        :param cache_token: Whether to cache the token, by default this is true
        you should only switch this to false when you want to directly fetch
        a token for a user
        """

        self.username = username
        self.password = password
        self.token = token
        self.ecs_endpoint = ecs_endpoint.rstrip('/')
        self.token_endpoint = token_endpoint.rstrip('/')
        self.verify_ssl = verify_ssl
        self.token_filename = token_filename
        self.request_timeout = request_timeout
        self.cache_token = cache_token
        self.session = requests.Session()

    def make_login_request(self, username=None, password=None,
                           accept_header=constants.APPLICATION_JSON):
        """
        Request a new authentication token from ECS
        """
        if username is None:
            username = self.username
        if password is None:
            password = self.password

        self.session.auth = (username, password)

        response = self.session.get(self.token_endpoint,
                                    verify=self.verify_ssl,
                                    headers={'Accept': accept_header},
                                    timeout=self.request_timeout)
        return response


class EcsDataPlaneClient():
    def __init__(self):
        pass
