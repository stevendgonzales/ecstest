from nose.plugins.attrib import attr
from ecstest import config, constants, tag, testbase
from ecstest.logger import logger
import random


@attr(tags=[tag.DATA_PLANE, tag.BUCKET_MGMT])
class TestBucketCreateDelete(testbase.EcsDataPlaneTestBase):
    def setUp(self):
        super(TestBucketCreateDelete, self).setUp()

    def test_create_delete(self):
        """Create a bucket, then delete it."""
        bucket_name='test_bucket_' + str(random.randint(1000, 2000))
        logger.info("Trying to create bucket: %s", bucket_name)
        # Any error will be raised as exception
        bucket = self.data_conn.create_bucket(bucket_name)
        # Verify the bucket is created
        # Any error will be raised as exception
        logger.info("Check whether bucket %s exists", bucket_name)
        buck = self.data_conn.get_bucket(bucket_name)
        self.assertTrue(buck)

        # Delete the bucket
        logger.info("Trying to delete the bucket %s", bucket_name)
        self.data_conn.delete_bucket(bucket_name)
        # Verify the bucket is deleted

        # self.assertRaise(self.data_conn.get_bucket(bucket_name))
