import numpy as np
import tensorflow as tf
import os
import pandas as pd
import cv2



def get_generator(tvt_type):

    shuffle_size = 1000
    batch_size = 32

    file_path = "../JAAD_split_videos/{}.txt".format(tvt_type)
    
    with open(file_path) as f:
        video_names = f.readlines()
    video_names = [video_name.rstrip('\n') for video_name in video_names]

    def get_action_data():
        
        for video_name in video_names:
            label_path = "../../dataset_preprocessing/removed_labels/{}.pickle".format(video_name)
            image_dir_path = "../../dataset_preprocessing/images/{}/".format(video_name)
            datas = pd.read_pickle(label_path)
            
            if os.path.isfile(label_path):
    
                datas = pd.read_pickle(label_path)
                
                for data in datas:
                    pic_number = str(data[0]).zfill(5)
                    image = cv2.imread(image_dir_path+'{}.jpg'.format(pic_number))
                    image = cv2.resize(image, dsize=(112, 192))
                    image = image/255.0
                    
                    yield (image, data[-4:])
            else:
                continue

    ds_series = tf.data.Dataset.from_generator(get_action_data,
                                            output_types=(tf.float32, tf.int16),
                                            output_shapes=(tf.TensorShape([192, 112, 3]), tf.TensorShape([4])),
                                            )


    ds_series_batch = ds_series.shuffle(shuffle_size).batch(batch_size) # dataset size parameter in shuffle function 
    
    return ds_series_batch
    