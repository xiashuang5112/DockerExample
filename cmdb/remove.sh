#!/usr/bin/env bash


docker stop cmdb_mysql
docker rm cmdb_mysql

docker-compose up -d

