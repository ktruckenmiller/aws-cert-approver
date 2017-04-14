#!/bin/sh
docker run -it \
  -v $(PWD):/code \
  --workdir="/code/code" \
  -e IAM_ROLE="cloudformation" \
  jfloff/alpine-python:2.7 \
  /bin/sh -c "pip install -r requirements-test.pip && /bin/sh"
