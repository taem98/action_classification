

import os

with open('./removed_train_right.txt', 'r') as f:
        texts = f.readlines()

dir_path = "../../images/split_data/direction/train_removed/right/"

for name in texts:
    if os.path.isfile(dir_path+name[:-1]):
        os.remove(dir_path+name[:-1])
        # pass
    else:
        print("no file : ", dir_path+name)

