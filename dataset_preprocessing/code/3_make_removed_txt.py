import os
import pickle
import shutil
import cv2

img_dir_path = '../images/video_0001/'
img_list = os.listdir(img_dir_path)
img_list.sort()

remove_list = []

for img_name in img_list:
    img = cv2.imread(img_dir_path + img_name)
    h, w, _ = img.shape
    if (h/w) > 5 :
        remove_list.append(img_name)

with open("./removed_test_left.txt", 'w') as f:
    for img_name in remove_list:
        f.write(img_name+'\n')

