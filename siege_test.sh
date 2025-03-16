#!/bin/bash
echo "Testing /load_mongo"
siege -c 50 -t 5M http://localhost/load_mongo > mongo_test.log

echo "Testing /load_elastic"
siege -c 50 -t 5M http://localhost/load_elastic > elastic_test.log

echo "Testing /combined_load"
siege -c 100 -t 5M http://localhost/combined_load > combined_test.log