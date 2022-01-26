import pandas as pd

df = pd.read_csv("result5_after_ranking_runtime_income.csv")


def return_moves_to_array(data_in):
    all_type_of_move = []
    if "&" in data_in:
        data_in = data_in.replace('&' , '')
    if "," in data_in:
        data_in = data_in.replace(','  , '')
    for x in data_in.split(' '):
        if x != '':
            all_type_of_move.append(x)
    return all_type_of_move

def check_if_Action(data_in):
    if "Action" in data_in:
        return 1
    else:
        return 0

def check_if_Drama(data_in):
    if "Drama" in data_in:
        return 1
    else:
        return 0

def check_if_Comedy(data_in):
    if "Comedy" in data_in:
        return 1
    else:
        return 0

def check_if_Adventure(data_in):
    if "Adventure" in data_in:
        return 1
    else:
        return 0

def check_if_Thriller(data_in):
    if "Thriller" in data_in:
        return 1
    else:
        return 0

def check_if_Mystery(data_in):
    if "Action" in data_in:
        return 1
    else:
        return 0

def check_if_Fantasy(data_in):
    if "Fantasy" in data_in:
        return 1
    else:
        return 0

def check_if_Biography(data_in):
    if "Biography" in data_in:
        return 1
    else:
        return 0

def check_if_Family(data_in):
    if "Family" in data_in:
        return 1
    else:
        return 0

def check_if_Kids(data_in):
    if "Kids" in data_in:
        return 1
    else:
        return 0

def check_if_Sci_Fi(data_in):
    if "Sci-Fi" in data_in:
        return 1
    else:
        return 0

def check_if_Romance(data_in):
    if "Romance" in data_in:
        return 1
    else:
        return 0

def check_if_Horror(data_in):
    if "Horror" in data_in:
        return 1
    else:
        return 0



df["genre_arr"] = df.loc[: , "genre"].apply(return_moves_to_array)
df["Action"] = df.loc[: , 'genre_arr' ].apply(check_if_Action)
df["Drama"] = df.loc[: , 'genre_arr' ].apply(check_if_Drama)
df["Comedy"] = df.loc[: , 'genre_arr' ].apply(check_if_Comedy)
df["Adventure"] = df.loc[: , 'genre_arr' ].apply(check_if_Adventure)
df["Thriller"] = df.loc[: , 'genre_arr' ].apply(check_if_Thriller)
df["Mystery"] = df.loc[: , 'genre_arr' ].apply(check_if_Mystery)
df["Fantasy"] = df.loc[: , 'genre_arr' ].apply(check_if_Fantasy)
df["Biography"] = df.loc[: , 'genre_arr' ].apply(check_if_Biography)
df["Family"] = df.loc[: , 'genre_arr' ].apply(check_if_Family)
df["Sci-Fi"] = df.loc[: , 'genre_arr' ].apply(check_if_Sci_Fi)
df["Romance"] = df.loc[: , 'genre_arr' ].apply(check_if_Romance)
df["Horror"] = df.loc[: , 'genre_arr' ].apply(check_if_Horror)


df.to_csv("result6_after_split_film_type.csv", encoding='utf-8', index=False)
