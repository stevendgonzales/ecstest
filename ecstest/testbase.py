import testtools

from ecstest import config, client
from ecstest.extensions import matchers


class EcsTestBase(testtools.TestCase):
    """Generic TestBase class. Shall not use it but one of its subclass
    """
    def setUp(self):
        super(EcsTestBase, self).setUp()

        cfg = config.get_config()

    def assertJsonSchema(self, expected, observed, message=''):
        """Assert that 'expected' is equal to 'observed'.
        :param expected: The expected value.
        :param observed: The observed value.
        :param message: An optional message to include in the error.
        """
        matcher = matchers.JsonSchemaMatcher(expected)
        self.assertThat(observed, matcher, message)

class EcsControlPlaneTestBase(EcsTestBase):
    """Subclass for testing control plane
    """
    def setUp(self):
        super(EcsControlPlaneTestBase, self).setUp()

        self.controlplane_client = client.EcsControlPlaneClient(
            username=cfg['ADMIN_USERNAME'],
            password=cfg['ADMIN_PASSWORD'],
            token=cfg['TOKEN'],
            ecs_endpoint=cfg['ECS_CONTROL_ENDPOINT'],
            token_endpoint=cfg['ECS_TOKEN_ENDPOINT'],
            verify_ssl=cfg['VERIFY_SSL'],
            token_filename=cfg['TOKEN_FILENAME'],
            request_timeout=cfg['REQUEST_TIMEOUT'],
            cache_token=cfg['CACHE_TOKEN'])

