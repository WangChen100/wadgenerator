#!/usr/bin/env bash
set -e

rm -rf outputs
mkdir -p outputs
mkdir -p outputs/maps
mkdir -p outputs/sources
mkdir -p outputs/images


ACC="./acc/acc"
if [ ! -f $ACC ]; then
    echo "File $ACC does not exist, compiling..."
    make -C ./acc
fi

for FILE in content/*.acs; do
    $ACC -i ./acc $FILE "outputs/$(basename ${FILE%.*}).o"
done

for INDEX in $(seq -s ' ' 0 3); do
    PLAN="outputs/maps/selfmaze${INDEX}"
    MAZE="outputs/maps/selfmaze${INDEX}.wad"
    python selfwad.py $PLAN $MAZE -b outputs/static_goal.o
    #python selfwad.py $PLAN $MAZE -b outputs/static_goal_train.o
done

echo "Success"
