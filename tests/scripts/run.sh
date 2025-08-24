#!/bin/bash

cd ../../
source .venv/bin/activate

cd tests/test_java/
oasislmf model run -C oasislmf.json
