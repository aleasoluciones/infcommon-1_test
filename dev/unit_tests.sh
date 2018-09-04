#!/bin/bash

mamba -f progress specs
UNITTESTS_RETCODE=$?
exit $UNITTESTS_RETCODE
