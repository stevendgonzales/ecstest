# ecstest

A functional test suite for testing [EMC ECS](https://www.emc.com/storage/ecs-appliance/index.htm) deployments.

The test suite is based off of the [testtools](http://testtools.readthedocs.org/) library
for creating tests that use [assertions](http://testtools.readthedocs.org/en/latest/for-test-authors.html#assertions).  
The library contains methods for test setup, teardown, and helper libraries for matchers and delayed assertions.

Every test included should make assertions about the feature it is testing, such as return codes,
response bodies, status codes, expected headers, etc.

