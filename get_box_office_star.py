from bs4 import BeautifulSoup
import requests
import csv
import time
import numpy as np


csv_file = open("film_stars.csv" , "a")
write_to_csv = csv.writer(csv_file)
write_to_csv.writerow(['rank' , 'name' , 'num_filem'])

for page_num in np.arange(1,100):
    print(f'PageNumber ==>  10{page_num}')

    req1 = requests.get(f"https://www.the-numbers.com/box-office-star-records/domestic/lifetime-acting/top-grossing-leading-stars/{page_num}01").text
    soup = BeautifulSoup(req1, "html5lib")

    table_body = soup.find_all('tbody')
    # table_body_of_cast = table_body[3]
    table_body_of_cast = table_body[0]
    table_row = table_body_of_cast.find_all('tr')

    for x in range(0 , 100):
        table_data = table_row[x].find_all('td')
        rank = table_data[0].text
        cast_name = table_data[1].text
        movies = table_data[3].text
        print(f"Rank : {rank} -- CastName : {cast_name} -- Movies : {movies}  ")
        write_to_csv.writerow([rank , cast_name , movies])

    time.sleep(np.random.randint(4,18))

csv_file.close()









