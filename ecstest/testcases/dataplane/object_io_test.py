from nose.plugins.attrib import attr
from ecstest import config, constants, tag, testbase
from ecstest.logger import logger
from boto.exception import S3ResponseError
from boto.s3.key import Key
import sys
import random

@attr(tags=[tag.DATA_PLANE, tag.OBJECT_IO])
class TestObjectPostGetDelete(testbase.EcsDataPlaneTestBase):
    def setUp(self):
        super(TestObjectPostGetDelete, self).setUp()
        self.bucket_name = "object_io_bucket_" + str(random.randint(2000, 3000))
        self.bucket = self.data_conn.create_bucket(self.bucket_name)

    def tearDown(self):
        self.data_conn.delete_bucket(self.bucket_name)
        super(TestObjectPostGetDelete, self).tearDown()

    def test_basic_post_get_delete(self):
        """JIRA ID: ECSTEST-5"""
        k = Key(self.bucket)
        k.key = 'test_key_1'
        content = 'This the the content of test_key_1'
        k.set_contents_from_string(content)

        content_2 = k.get_contents_as_string()
        self.assertEqual(content, content_2)

        k.delete()
        self.assertRaises(S3ResponseError, k.get_contents_as_string, None)

