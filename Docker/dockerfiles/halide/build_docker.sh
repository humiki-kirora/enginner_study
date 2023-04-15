#!/bin/sh

container_name=$1
if [ -z $container_name ] ; then
    container_name=halide
    echo $container_name
fi

docker build --build-arg UID=$(id -u) --build-arg GID=$(id -g) -t $container_name .