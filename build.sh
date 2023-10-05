#!/bin/bash

DEFAULT_BUILD="Release"

build_type=$1
case $build_type in
    'Debug' | 'Release' | 'RelWithDebInfo')
        echo "Using ${build_type}"
        ;;
    *)
        echo "Using default '${DEFAULT_BUILD}' build type"
        build_type=$DEFAULT_BUILD
        ;;
esac

cmake -S . -B "$build_type" || exit | tee build.log
cmake --build "$build_type" || exit | tee build.log
