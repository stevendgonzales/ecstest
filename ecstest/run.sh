#!/bin/bash

#
# Temporary command to run single case
#

export TEST_ROOT=$PWD
export PYTHONPATH=$TEST_ROOT/libs:$PYTHONPATH

python -m testtools.run $@

