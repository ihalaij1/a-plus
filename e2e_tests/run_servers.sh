#!/bin/bash

export COMPOSE_FILE=e2e_tests/docker-compose.yml

# Move to aplus-manual directory and build the course
cd `dirname "$0"`/../aplus-manual
git submodule update --init
./docker-compile.sh

# Move to a-plus directory and run the server
cd ..
./docker-up.sh
