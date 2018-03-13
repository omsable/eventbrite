#!/bin/sh
set -e

# install eventbrite from pypi
apk update
apk add --no-cache python py-pip

pip install eventbrite

rm -rf /var/cache/apk/*
