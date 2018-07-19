#!/usr/bin/env bash
cd ../
../scopuli-environment/bin/pip uninstall scopuli-core-config  -y
../scopuli-environment/bin/python3.7 setup.py install
