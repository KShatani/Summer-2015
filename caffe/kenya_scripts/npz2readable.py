#!/bin/python

import caffe
import numpy as np
import sys 

if len(sys.argv) < 3: 
	print "Usage;", sys.argv[0], "<npz_path> <readable_file>"
	sys.exit(2)

npz_path = sys.argv[1] #input npz file
readable_file = sys.argv[2] #output file

raw = np.load(npz_path)

labels = raw["labels"]
data = raw["data"]

label_len = len(labels)
data_len = len(data)

data_path = 'kenya_scripts/savedFeatures/' + readable_file 

np.savetxt(data_path, data, delimiter=',')

print "number of feature vectors:" + str(label_len)

print "done extracting features and converting it to .txt file!"

#np.savetxt('kenya_scripts/saveFeatures/test_labels_new.txt.',labels,delimiter=',')
#save data as a .txt file.   	
#write the row number at the beginning of the file. 
#the row number corresponds to the ith file in the file_list.txt. which is the label. 

