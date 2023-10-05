#!/bin/bash

./build.sh Release
./Release/max_clique | tee out.csv
