from bs4 import BeautifulSoup
import requests


req1 = requests.get("https://en.wikipedia.org/wiki/List_of_American_films_of_2015").text
soup = BeautifulSoup(req1, "html5lib")
result = soup.find_all("tr")
filem_names_list = []
#Since we have multible table rows in the page
#code will start from row number 42 which has filem name
for table_row_number in range(42 , 237):
    try:
        filem_name = result[table_row_number].find("a")
        filem_names_list.append(filem_name.text)
        # print(filem_name.text)
    except:
        print("Nooooooooo")


print(len(filem_names_list))
print(filem_names_list)

