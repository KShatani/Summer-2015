#!/bin/bash

echo "enter a new feature folder"
read foldername
echo $foldername

echo "enter number of files in file"
read nFiles

.././build/tools/extract_features ../models/bvlc_reference_caffenet/bvlc_reference_caffenet.caffemodel ../examples/_temp/imagenet_val.prototxt fc7 kenya_scripts/$foldername $nFiles lmdb
