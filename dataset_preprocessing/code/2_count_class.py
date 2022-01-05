import pickle
import gzip
import os


path_dir = '../labels/'
file_list = os.listdir(path_dir)

# [image_num, frame_num, person_ID, move, direction, looking, phone ]

c_standing = 0
c_walking = 0

# c_left = 0
# c_right = 0
# c_front = 0
# c_back = 0

c_look = 0
c_nlook = 0

c_phone = 0
c_nphone = 0

c_bicycle_motorcycle = 0
c_nbicycle_motorcycle = 0

for file_name in file_list:
    with open(path_dir+file_name, 'rb') as f:
        data = pickle.load(f)

    for obj in data:
        
        if obj[3] == 0:   c_standing += 1
        elif obj[3] == 1: c_walking += 1

        # if obj[4] == 0:   c_left += 1 
        # elif obj[4] == 1: c_right += 1
        # elif obj[4] == 2: c_front += 1
        # elif obj[4] == 3: c_back += 1

        if obj[4] == 0:   c_nlook += 1
        elif obj[4] == 1: c_look += 1

        if obj[5] == 0:   c_nphone += 1
        elif obj[5] == 1: c_phone += 1

        if obj[6] == 0:   c_nbicycle_motorcycle += 1
        elif obj[6] == 1: c_bicycle_motorcycle += 1

with open('./count_result.txt', 'w') as f:
    f.write('standing : {}\n'.format(c_standing))
    f.write('walking : {}\n\n'.format(c_walking))
    f.write('all : {}\n\n'.format(c_standing+c_walking))

    # f.write('left : {}\n'.format(c_left))
    # f.write('right : {}\n'.format(c_right))
    # f.write('front : {}\n'.format(c_front))
    # f.write('back : {}\n\n'.format(c_back))
    # f.write('all : {}\n\n'.format(c_left+c_right+c_front+c_back))
    

    f.write('look : {}\n'.format(c_look))
    f.write('non_look : {}\n\n'.format(c_nlook))
    f.write('all : {}\n\n'.format(c_look+c_nlook))
    

    f.write('phone : {}\n'.format(c_phone))
    f.write('non_phone : {}\n\n'.format(c_nphone))
    f.write('all : {}\n\n'.format(c_phone+c_nphone))

    f.write('bicycle_motorcycle : {}\n'.format(c_bicycle_motorcycle))
    f.write('non_bicycle_motorcycle : {}\n\n'.format(c_nbicycle_motorcycle))
    f.write('all : {}\n\n'.format(c_bicycle_motorcycle+c_nbicycle_motorcycle))

    


