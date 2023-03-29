#!/bin/bash

echo
echo "Running Integration tests"
echo "----------------------------------------------------------------------"
echo

find . -name *pyc* -delete
source "dev/env_develop"

mamba -f progress `find . -maxdepth 2 -type d -name "integration_specs" | grep -v systems`
MAMBA_RETCODE=$?
exit $MAMBA_RETCODE
