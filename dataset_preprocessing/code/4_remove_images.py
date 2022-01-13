

import os

# with open('./removed_test_left.txt', 'r') as f:
#         texts = f.readlines()

with open("./removed_test/*.txt", 'r') as f:
    texts = f.readlines()

# dir_path = "../images/"

dir_path = "../images/**/*.jpg"

for name in texts:
    if os.path.isfile(dir_path+name[:-1]):
        os.remove(dir_path+name[:-1])
        # pass
    else:
        print("no file : ", dir_path+name)

# for name in os.listdir(dir_path):
#     with open(os.path.join(dir_path, name), 'r') as f:
#         if os.path.isfile(dir_path+name[:-1]):
#            os.remove(dir_path+name[:-1])
#            # pass
#         else:
#            print("no file : ", dir_path+name)

        
