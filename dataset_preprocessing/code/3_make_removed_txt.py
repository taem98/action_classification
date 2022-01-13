# import os
# import os.path
# import pickle
# import shutil
# import cv2
# import sys
# from glob import glob

# img_dir_path = "../images/"
# img_list = os.listdir(img_dir_path)
# # img_list = glob(img_dir_path)



# # def print_file(img_dir_path):
# #     files = os.listdir(img_dir_path)
# #     for item in files :
# #         if os.path.isdir(img_dir_path + item) == True :
# #             print_file(img_dir_path + item)
# #         else:
# #             return 0

            


# img_list.sort()

# remove_list = []

# for img_name in img_list:
#     img = cv2.imread(img_dir_path + img_name)
#     h, w, _ = img.shape
#     if (h/w) > 5 :
#         remove_list.append(img_name)
#     video_name = remove_list
# # with open("./removed_test_{}.txt".format(video_name), 'w') as f:
# # with open("./removed_test_[].txt", 'w') as f:
#     for img_name in remove_list:
#         f.write(img_name+'\n')


# =========================================================================
# =========================================================================


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

# categorize and extract list of categories

# category = []

# for imgs in remove_list:
#     temp_list = imgs.split("/")
#     category.append(temp_list[-2])

# temp_set = set(category)
# result = list(temp_set)
# result.sort()


# make text files and put the list elements to each directory

os.mkdir('./removed_test')

for imgs in remove_list:
    temp_list = imgs.split("/")
    for num in range(0,347):
        num_list = "{:04d}".format(num)
        video_name = 'video_{}'.format(num_list)
        if video_name == temp_list[-2]:
            with open("./removed_test/removed_test_{}.txt".format(video_name), 'w') as f:
                for img_name in remove_list:
                    if img_name.split("/")[-2]== video_name:
                        f.write(img_name+'\n')
