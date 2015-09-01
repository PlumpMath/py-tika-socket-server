#!/usr/bin/env bash

set +x 

rm -f lib/*.jar

wget http://central.maven.org/maven2/org/clojure/clojure/1.7.0/clojure-1.7.0.jar  -P lib/
wget http://central.maven.org/maven2/org/apache/tika/tika-app/1.10/tika-app-1.10.jar -P lib/

