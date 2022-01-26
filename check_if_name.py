import pandas as pd
import numpy as np
import csv


df1 = pd.read_csv('film_stars2.csv')
df2 = pd.read_csv('result3_after_dropping.csv')

csv_file = open("films_with_cast_rate.csv" , "a")
write_to_csv = csv.writer(csv_file)
write_to_csv.writerow(['filem_name' ,
                       'cast1' ,
                       'cast2' ,
                       'cast3' ,
                       'cast4' ,
                       'cast5' ,
                       'cast6' ,
                       'cast7' ,
                       'cast8' ,
                       'cast9' ,
                       'five_total_missing',
                       'all_total_missing',
                       'sum_of_first_five'
                       ])

def replace_missing_value_and_get_total(curr_list , total_missing):
    sum_rplace = 0
    sum_total = 0
    #sum not none values:
    for x in curr_list[1:-3]:
        if x != None:
            sum_rplace = sum_rplace + x
    #Replace none with avrage-1
    for x in range(len(curr_list)):
        if curr_list[x] == None:
            curr_list[x] = int((sum_rplace/(total_missing+1)) )
    #Add total to list row
    for x in curr_list[1:-7]:
        sum_total = sum_total + x
    curr_list[-1] = sum_total
    return curr_list



# because data has ',' we have to remove to convert rank to integer
for x in range(len(df1)):
    aa = df1.iloc[x , 0]
    if x >= 999:
        df1.iloc[x , 0] = int(f"{aa.split(',')[0]}{aa.split(',')[1]}")
    else:
        df1.iloc[x , 0] = int(aa)

df1['rank'] = df1['rank'].astype(int)

#Join each name with its rank.
names = []
for index_num in range(len(df1)):
    name_with_rank = f'{df1.iloc[index_num,1].lower()} = {df1.iloc[index_num,0]}'
    names.append(name_with_rank)



#convert all filem_stars with their filems to a list and append it to big list
all_filems_and_name = []
for x in range(len(df2)):
# for x in range(100):
    tem_filem_and_names = []
    tem_filem_and_names.append(df2.iloc[x , 0])
    for name in df2.iloc[x , 16].split(',')[:-1]:
        tem_filem_and_names.append(name)
    all_filems_and_name.append(tem_filem_and_names)

count_less_than_3 = 0
#convert previous list to rank using rankkin list
for filem_name_one_list in all_filems_and_name:
    filem_name_result = ['',0,0,0,0,0,0,0,0,0,0,0,0]
    # these to lines will detremin which rows have huge amount of missing vlaue
    first_five_none = 0
    total_none = 0
    filem_name_result[0] = filem_name_one_list[0] # get the name of file and put it first ele
    #Check each name with each rank and put it on fillem_name_result based on its order
    for num in range(1,10):
        searched_name = filem_name_one_list[num].lower().strip()
        matching = [s.lower() for s in names if searched_name in s.lower()]
        if len(matching) > 0:
            rank = 10000 - ( int(matching[0].split('=')[1].strip()) )
            filem_name_result[num] = rank
        else:
            filem_name_result[num] = None
            total_none = total_none + 1
            if num <= 5:
                first_five_none =first_five_none + 1

    filem_name_result[10] = first_five_none
    filem_name_result[11] = total_none
    if first_five_none <= 2:
        count_less_than_3 = count_less_than_3 + 1
        result_from_func = replace_missing_value_and_get_total(filem_name_result, first_five_none)
        print(result_from_func)
        print(result_from_func[0])
        write_to_csv.writerow([
                               result_from_func[0],
                               result_from_func[1],
                               result_from_func[2],
                               result_from_func[3],
                               result_from_func[4],
                               result_from_func[5],
                               result_from_func[6],
                               result_from_func[7],
                               result_from_func[8],
                               result_from_func[9],
                               result_from_func[10],
                               result_from_func[11],
                               result_from_func[12]
                               ])



csv_file.close()


