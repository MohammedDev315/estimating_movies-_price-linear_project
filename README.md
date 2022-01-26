
## Abstract
New movies are released every year, some of them become very successful with very high income, while others can not have the same success. In this project, I will try to estimate the price of these movies based on different features such as actors, production, year of reals ..etc.




## Question
If a new film released, how much it will make?

## Data:
Data has been collected from different websites using web scraping. These websites are, 
* "https://www.rottentomatoes.com" data extracted are rating, type, language, Director, Producer, Writer, Release Date, Runtime and Distributor.
* "https://www.wikipedia.org", get last five year films' names. 
* "https://www.the-numbers.com" get films' ranks  


## Tools
* SQL
* Tableau
* Numpy
* Pandas
* BeautifulSoup
* Selenium
* Requests



## Project Description:
I started by extracting all films from wekibidea using [this code ](https://github.com/MohammedDev315/estimating_movies-_price-linear_project/blob/master/get_films_name_from_wikipedia.py) and then print all names. 
The second step is taking these names and saving them as a list, after that, the for loop is used to get the film name for filem_list and use the selenium library to extract more film details from rottentomatoes.com - [code]( https://github.com/MohammedDev315/estimating_movies-_price-linear_project/blob/master/selen3.py ). All data are saved on a CSV file for future use. in addition, adding more details about film stars is important so, numbers.com  websites are used to extract more details such as star's details [code](https://github.com/MohammedDev315/estimating_movies-_price-linear_project/blob/master/get_box_office_star.py) ,  [directors ](https://github.com/MohammedDev315/estimating_movies-_price-linear_project/blob/master/get_top_director.py), [prediction companies](https://github.com/MohammedDev315/estimating_movies-_price-linear_project/blob/master/get_production_companies.py).
After that, all data gather together to make one CSV using SQL.
To analyze the data frame, I started [clean data](https://github.com/MohammedDev315/estimating_movies-_price-linear_project/blob/master/clean_data.py), after that made five new columns "dummy" to represent the most popular [film's type](https://github.com/MohammedDev315/estimating_movies-_price-linear_project/blob/master/split_moves_type.py). After that, a first leaner regression model was used to predict films income - [code](https://github.com/MohammedDev315/estimating_movies-_price-linear_project/blob/master/regression_evaluation.py)- however polynomial regression gives the better result -  [code](https://github.com/MohammedDev315/estimating_movies-_price-linear_project/blob/master/poly_regression.py)












