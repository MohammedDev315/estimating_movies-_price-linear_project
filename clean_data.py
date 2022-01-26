import matplotlib.pyplot as plt
import pandas as pd
from pandas.api.types import is_string_dtype


df = pd.read_csv('result2.csv')
# df = df.astype({
#     "CategoryCategoryName": str,
#     "OrderShipCity": str,
#     "OrderShipCountry" :str,
#     "OrderShipRegion" :str
# })


def show_basic_statics(col_name):
    print(f"==={col_name}===")
    #chek if cloumn has null
    print(f"No Null : {len(df[df.loc[:, col_name ].isnull() == False]) == len(df.loc[:, col_name ])} ")
    # check if text number has empty space
    if is_string_dtype(df[col_name]):
        for text in df.loc[:, col_name]:
            if len(text.strip()) != len(text):
                print(f"Please check this text :  {text} ")
    print(df.loc[:, col_name].describe())
    print("==========End========")

#drop column 'aspect_ration


columns_name = ['filem_name', 'tomatometerscore', 'audiencescore', 'reviews_numb',
       'ratings_numb', 'rating', 'genre', 'language', 'director', 'producer',
       'writer', 'release_date_theaters', 'release_date_streaming',
       'box_office', 'runtime', 'distributor', 'aspect_ratio', 'actors']

show_basic_statics(columns_name[7])
