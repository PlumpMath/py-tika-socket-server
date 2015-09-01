#!/usr/bin/env bash

set +x
java -cp .:lib/* clojure.main src/server.clj 2>&1 > tmp/tika-socket-server.log &

printf "server started\n"
