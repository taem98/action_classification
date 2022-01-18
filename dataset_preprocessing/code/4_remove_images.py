import os
import glob
from posixpath import split
import re




# get the directory list of videos

dir_path = "../images/"
list_dir = os.listdir(dir_path)
list_dir.sort()



# removed_video_name_list

img_path = "../removed_test/"

img_dir = []
txt_list = os.listdir(img_path)
txt_list.sort()
for i in txt_list:
    split_list = re.split('[_.]',i)
    split_name = split_list[2]+"_"+split_list[3]
    img_dir.append(split_name)



# remove the images in removed_test list


for imgs in img_dir:
    txt_path = "../removed_test/removed_test_{}.txt".format(imgs)
    file = open(txt_path, 'r')
    read_file = file.readlines()
    for img_name in read_file:
        impath = dir_path+txt_path[29:39]+"/"+img_name
        imlist = impath.split('\n')
        for name in imlist:
            if os.path.isfile(name):
                os.remove(name)
    

