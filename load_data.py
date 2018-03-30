
import numpy as np
import pandas as pd 
import json
import csv
from pandas import DataFrame
import urllib


def load_data(json_data_path, dest_dir, sample_size):
    with open(json_data_path+".json") as temp_file:
        temp_data = json.load(temp_file)
    
    print(len(temp_data["annotations"]))
    
    image_ids=[]
    labels=[]
    urls=[]
    
    for i in range(0,len(temp_data["annotations"])):
        image_ids.append(temp_data["annotations"][i]['image_id'])
        labels.append(temp_data["annotations"][i]['label_id'])
        urls.append(temp_data["images"][i]['url'][0])
    
    d = {'image_id': val_img_ids, 'label':val_labels, 'url':val_urls}
    df = pd.DataFrame(data=d)
    df1 = df.sort_values(by=['label'])
    
    new_dataframe=df1.loc[df1['label']==1][0:sample_size]
    for i in range(2,129):
        new_dataframe=new_dataframe.append(df1.loc[df1['label']==i][0:sample_size])
    
    new_dataframe
    error_images=[]
    for i in range(0,len(new_dataframe)):
        try:
            urllib.request.urlretrieve(new_dataframe.iloc[i]['url'],dest_dir+"/"+ str(new_dataframe.iloc[i]['image_id']) +'.jpg')
        except:
            error_images.append(i)
            print("error"+str(i+1))
    
