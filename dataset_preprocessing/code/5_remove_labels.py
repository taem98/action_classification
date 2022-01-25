import pickle
import os
import cv2

            
dir_path = "../images/"
dir_list = os.listdir(dir_path)
dir_list.sort()

try:
    os.mkdir('../removed_labels')
except:
    pass

for dir in dir_list:
    path_dir = '../labels/{}.pickle'.format(dir)
    pick = open(path_dir, 'rb')
    data = pickle.load(pick)
    data.sort()
    count_data = len(data)
    
    # images without removed img0.
    for j in range(count_data):
        a = '{:05d}'.format(j)
        # img num in labels
        path = '../images/{0}/{1}.jpg'.format(dir,a)
        if os.path.isfile(path):
            pass
        else:
            if a == '00000':
                a = '0'
            else:
                a = a.lstrip('0')
            
            # print(data)
            p = int(a)
            
            # print(data[p])
            # del(data[p])
            for i, one_data in enumerate(data):
                if one_data[0] == p:
                    del(data[i])    

    with open('../removed_labels/{}.pickle'.format(dir), 'wb') as f:
        pickle.dump(data, f, pickle.HIGHEST_PROTOCOL)

            