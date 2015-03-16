from nose.plugins.attrib import attr

from ecstest import constants
from ecstest import tag
from ecstest import testbase


LOGIN_SCHEMA = {
    "$schema": "http://json-schema.org/draft-04/schema#",
    "id": "http://jsonschema.net",
    "type": "object",
    "properties": {
        "user": {
            "id": "http://jsonschema.net/user",
            "type": "string"
        }
    },
    "required": [
        "user"
    ]
}


@attr(tags=[tag.CONTROL_PLANE, tag.AUTH])
class TestUserLogin(testbase.EcsControlPlaneClient):

    def setUp(self):
        super(TestUserLogin, self).setUp()
        self.invalid_username = 'foo'
        self.invalid_password = 'bar'
        self.expected_token_length = 164

    def test_login_returns_successful(self):
        """Test that a valid login returns a 200,
        the proper json schema, and an access token in the header.
        """

        response = self.controlplane_client.make_login_request()

        # assert the expected return code
        self.assertEquals(response.status_code, 200)

        response_json = response.json()

        # make assertions on the schema of the response body
        self.assertJsonSchema(LOGIN_SCHEMA, response_json)
        self.assertEquals(self.controlplane_client.username,
                          response_json['user'])

        # assert a token was returned, and that it is the expected length
        self.assertIn(constants.AUTH_TOKEN_HEADER, response.headers)
        self.assertEqual(self.expected_token_length,
                         len(response.headers['x-sds-auth-token']))

    def test_login_returns_401_on_bad_creds(self):
        """Test that a failed login returns a 401,
        and does not provide a token.
        """

        response = self.controlplane_client.make_login_request(
            username='foo', password='bar')

        # assert the expected return code
        self.assertEquals(response.status_code, 401)

        # assert a token is not returned on a failed login request
        self.assertNotIn(constants.AUTH_TOKEN_HEADER, response.headers)
