

import os

with open('./removed_test_left.txt', 'r') as f:
        texts = f.readlines()

dir_path = "../images/video_0001/"

for name in texts:
    if os.path.isfile(dir_path+name[:-1]):
        os.remove(dir_path+name[:-1])
        # pass
    else:
        print("no file : ", dir_path+name)

