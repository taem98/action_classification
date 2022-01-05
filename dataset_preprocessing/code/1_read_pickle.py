import pandas as pd


file_path = "../labels/video_0003.pickle"
datas = pd.read_pickle(file_path)
print(datas)