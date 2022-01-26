import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

csv_data = pd.read_csv("result7_after_reomve_zero_from_dirctors.csv")

mask1 = (csv_data.loc[: , 'director_rank' ] > 6000 ) & \
        (csv_data.loc[: , 'rank_of_five_top_stars'] < 48000 ) &\
        (csv_data.loc[: , 'film_income'] < 400000000 )

filtered_df = csv_data[mask1]
print(filtered_df.shape)

X = filtered_df[[ 'director_rank', 'rank_of_five_top_stars',
       'runtime_minuts', 'release_year' ,  'Action', 'Drama', 'Comedy',
       'Adventure', 'Mystery', 'Fantasy']]
y = filtered_df[["film_income"]]

# Splitting the dataset into the Training set and Test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

poly_reg = PolynomialFeatures(degree=9)
X_poly = poly_reg.fit_transform(X)
pol_reg = LinearRegression()
pol_reg.fit(X_poly, y)

print(f'Degree 9 polynomial regression val R^2: {pol_reg.score(X_poly, y):.3f}')




