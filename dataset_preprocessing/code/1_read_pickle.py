import pandas as pd


file_path = "/home/msis/Desktop/deepsort_models/project/action_classification/dataset_preprocessing/labels/video_0001.pickle"
datas = pd.read_pickle(file_path)
print(datas)