
from bs4 import BeautifulSoup
import requests
import csv
import time
import numpy as np


# csv_file = open("prduction_companies.csv" , "a")
# write_to_csv = csv.writer(csv_file)
# write_to_csv.writerow(['rank' , 'name' , 'num_filem'])
#


# for page_num in np.arange(1,1000):
#     print(f'PageNumber ==>  10{page_num}')
#     req1 = requests.get(f"https://www.the-numbers.com/box-office-star-records/worldwide/lifetime-specific-technical-role/director/{page_num}01").text
#     soup = BeautifulSoup(req1, "html5lib")
#
#     table_body = soup.find_all('tbody')
#     # table_body_of_cast = table_body[3]
#     table_body_of_cast = table_body[0]
#     table_row = table_body_of_cast.find_all('tr')
#
#     for x in range(0 , 100):
#         table_data = table_row[x].find_all('td')
#         rank = table_data[0].text
#         cast_name = table_data[1].text
#         movies = table_data[3].text
#         print(f"Rank : {rank} -- CastName : {cast_name} -- Movies : {movies}  ")
#         write_to_csv.writerow([rank , cast_name , movies])
#
#     time.sleep(np.random.randint(4,18))


rank = 100
for page_num in range(1,3):
    print(f"Current => {page_num} ")
    req1 = requests.get(f"https://www.the-numbers.com/movies/production-companies/#production_companies_overview=p{page_num}:od2").text
    time.sleep(5)
    soup = BeautifulSoup(req1, "html5lib")
    table_row = soup.find_all('tr')
    for x in range(1,101):
        company_name = table_row[x].find_all('td')[0].text
        print(f"{rank} - {company_name}")
        rank = rank + 1


#
# table_row = soup.find_all('tr')
# for x in range(1,101):
#     company_name = table_row[x].find_all('td')[0].text
#     print(f"{rank} - {company_name}")
#     rank = rank + 1





# for x in range(0 , 100):
#     table_data = table_row[x].find_all('td')
#     rank = table_data[0].text
#     cast_name = table_data[1].text
#     movies = table_data[3].text
#     print(f"Rank : {rank} -- CastName : {cast_name} -- Movies : {movies}  ")
    # write_to_csv.writerow([rank , cast_name , movies])


#
# csv_file.close()













