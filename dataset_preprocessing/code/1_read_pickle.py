import pandas as pd


file_path = "../labels/video_0001.pickle"
datas = pd.read_pickle(file_path)
print(len(datas))

file_path = "../removed_labels/video_0001.pickle"
datas = pd.read_pickle(file_path)
print(len(datas))

for data in datas:
    print(data, end='\n')