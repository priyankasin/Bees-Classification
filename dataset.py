from PIL import Image, ImageDraw
import numpy as np
from numpy import genfromtxt
import os
import shutil
import scipy.misc
import pandas as pd

print("Start.....")
label= pd.read_csv('train_labels.csv')
label.index=label.id
# print(label)
label=label['genus']
label=label.T.to_dict()
# print(label)
train1="train/bombus/"
train2="train/apis/"
if not os.path.exists(train1):
		os.makedirs(train1)

if not os.path.exists(train2):
		os.makedirs(train2)

src='/home/priyanka/Downloads/bee_classifier_using_cnn-master/dataset/images/train'

for img in os.listdir(os.path.join(src)):
	print(img)

	label_id=img[:-4]
	if label[int(label_id)]==1.0:
		path_file = os.path.join(src,img)
		print(path_file)

		shutil.copy2(path_file,train1)
	else:
		path_file = os.path.join(src,img)
		print(path_file)

		shutil.copy2(path_file,train2)



	# label_id=list(data.label[data.id==int(label_id)-1])
	# print(label_id)
	# label_id=label_id[0]
	# print(label_id)

	# file_name = os. path . join (dst,label_id,str(i)+'.jpg')
	# subject_path= os. path . join (dst,label_id)
	# print(subject_path)
	# if not os.path.exists(subject_path):
	# 	os.makedirs(subject_path)

	# path_file = os.path.join(src,img)
	# print(path_file)
	
	# shutil.copy2(path_file,subject_path)
	# print('data save')