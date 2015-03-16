from nose.plugins.attrib import attr
from nose import with_setup

from ecstest import constants
from ecstest import tag
from ecstest import config

from boto.s3.connection import S3Connection, OrdinaryCallingFormat

import random

cfg = config.get_config()
conn = S3Connection(
                    aws_access_key_id=cfg['ACCESS_KEY'],
                    aws_secret_access_key=cfg['ACCESS_SECRET'],
                    is_secure=False,
                    port=cfg['ACCESS_PORT'],
                    host=cfg['ACCESS_SERVER'],
                    calling_format=OrdinaryCallingFormat())

bucket_name='test_bucket_' + str(random.randint(1000, 2000))

def setUp():
    pass

def tearDown():
    pass

def is_bucket_exist(bname):
    bucket_list = conn.get_all_buckets()
    for buck in bucket_list:
        if (buck.name == bname):
            return True
    else:
        return False

@with_setup(setUp, tearDown)
@attr(tags=[tag.DATA_PLANE, tag.BUCKET_MGMT])
def test_create_bucket():
    print "Trying to create bucket:", bucket_name
    # Any error will be raised as exception
    bucket = conn.create_bucket(bucket_name)
    # Verify the bucket is created
    print "Check whether bucket", bucket_name, "exists"
    if is_bucket_exist(bucket_name):
        print "Bucket", bucket_name, "does exist"
    else:
        print "Bucket", bucket_name, "does NOT exist!!!"
        assert False

@with_setup(setUp, tearDown)
@attr(tags=[tag.DATA_PLANE, tag.BUCKET_MGMT])
def test_remove_empty_bucket():
    print "Delete bucket:", bucket_name
    # Any error will be raised as exception
    conn.delete_bucket(bucket_name)
    # Verify the bucket is deleted
    #
    # Only after restarting fake-s3, the bucket disappears
    # Need to be investigated whether we should list buckets and verify here in real system
    #


