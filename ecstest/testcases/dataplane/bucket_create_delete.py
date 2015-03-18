from nose.plugins.attrib import attr
from ecstest import config, constants, tag, testbase
from ecstest.logger import logger
from boto.exception import S3ResponseError
import random


@attr(tags=[tag.DATA_PLANE, tag.BUCKET_MGMT])
class TestBucketCreateDelete(testbase.EcsDataPlaneTestBase):
    def setUp(self):
        super(TestBucketCreateDelete, self).setUp()

    def create_delete_bucket(self, bucket_name):
        """Create a bucket, then delete it."""

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
        self.assertRaises(S3ResponseError, self.data_conn.get_bucket, bucket_name)

    def test_create_delete(self):
        """JIRA ID: ESCTEST-6 ESCTEST-7"""
        bucket_name = 'test_bucket_' + str(random.randint(1000, 2000))
        self.create_delete_bucket(bucket_name)

    def test_create_delete_shortest_name(self):
        """JIRA ID: ESCTEST-6 ESCTEST-7"""
        # TODO
        pass

    def test_create_delete_longest_name(self):
        """JIRA ID: ESCTEST-6 ESCTEST-7"""
        # TODO
        pass

    def test_create_delete_with_dot_underscore_hyphen(self):
        """JIRA ID: ESCTEST-6 ESCTEST-7"""
        # TODO
        pass

