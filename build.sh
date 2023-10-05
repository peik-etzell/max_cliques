#!/bin/bash

cmake -S . -B build || exit | tee build.log
cmake --build build || exit | tee build.log
