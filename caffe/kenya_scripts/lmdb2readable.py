#!/usr/bin/env python

import sys
import lmdb
import numpy as np
import caffe

if len(sys.argv) < 3:
  print "Usage:", sys.argv[0], "<lmdb_path> <npz_file>"
  sys.exit(2)

lmdb_path = sys.argv[1] #input folder
npz_file = sys.argv[2] #output file

env = lmdb.open(lmdb_path)
env_stat = env.stat()
num_images = env_stat['entries']
print "Number of images: ", num_images

data = None
labels = np.empty(num_images)
with env.begin() as txn:
    with txn.cursor() as curs:
        for key, value in curs:
            # convert value to numpy array
            datum = caffe.proto.caffe_pb2.Datum()
            datum.ParseFromString(value)
            arr = caffe.io.datum_to_array(datum)

            # lazily initialize matrix, once we know number of features
            if data is None:
                num_features = arr.shape[0]
                print "Number of features: ", num_features
                data = np.empty((num_images, num_features))

            # copy data to matrix
            data[int(key), ] = arr[:, 0, 0]
            labels[int(key)] = datum.label

env.close()

np.savez_compressed(npz_file, data=data, labels=labels)
