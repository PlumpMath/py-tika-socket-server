#!/usr/bin/env bash
set +x
printf "\x03\n" | nc localhost 9999
