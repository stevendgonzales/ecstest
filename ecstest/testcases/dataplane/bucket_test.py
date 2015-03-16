from nose.plugins.attrib import attr
from ecstest import config, constants, tag, testbase
import random


@attr(tags=[tag.DATA_PLANE, tag.BUCKET_MGMT])
class TestBucketCreateDelete(testbase.EcsTestBase):
    def setUp(self):
        super(TestBucketCreateDelete, self).setUp()

    def test_create_delete(self):
        """Create a bucket, then delete it."""
        bucket_name='test_bucket_' + str(random.randint(1000, 2000))
        print "Trying to create bucket:", bucket_name
        # Any error will be raised as exception
        bucket = self.data_conn.create_bucket(bucket_name)
        # Verify the bucket is created
        # Any error will be raised as exception
        print "Check whether bucket", bucket_name, "exists"
        buck = self.data_conn.get_bucket(bucket_name)
        self.assertTrue(buck)

        # Delete the bucket
        self.data_conn.delete_bucket(bucket_name)
        # Verify the bucket is deleted
        #
        # Only after restarting fake-s3, the bucket disappears
        # Need to be investigated whether we should list buckets and verify here in real system
        #
