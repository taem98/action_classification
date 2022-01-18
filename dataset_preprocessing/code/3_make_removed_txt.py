import glob
import cv2  
import os


# bring all files in all directories in "../images/"

img_dir_path = "../images/**/*.jpg"

images = glob.glob(img_dir_path, recursive=True)
images.sort()


# exract list of images to be removed

remove_list = []

count = len(images)
index = 0

for img_name in images:
    img = cv2.imread(images[index])
    h, w, _ = img.shape
    if (h/w) > 5 :
        remove_list.append(img_name)

    index += 1
    if index >= count:
        index = 0


# make text files and put the list elements to each directory

os.mkdir('../removed_test')

for imgs in remove_list:
    temp_list = imgs.split("/")
    for num in range(0,347):
        num_list = "{:04d}".format(num)
        video_name = 'video_{}'.format(num_list)
        if video_name == temp_list[-2]:
            with open("../removed_test/removed_test_{}.txt".format(video_name), 'w') as f:
                for img_name in remove_list:
                    if img_name.split("/")[-2]== video_name:
                        f.write(img_name[-9:]+'\n')
