#!/bin/bash

./build.sh
./build/max_clique | tee out.tsv
