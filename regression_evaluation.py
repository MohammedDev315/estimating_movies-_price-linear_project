import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, Ridge #ordinary linear regression + w/ ridge regularization
from sklearn.preprocessing import StandardScaler, PolynomialFeatures
from sklearn.model_selection import KFold

csv_data = pd.read_csv("result7_after_reomve_zero_from_dirctors.csv")

mask1 = (csv_data.loc[: , 'director_rank' ] > 6000 ) & \
        (csv_data.loc[: , 'rank_of_five_top_stars'] < 48000 ) &\
        (csv_data.loc[: , 'film_income'] < 400000000 )

filtered_df = csv_data[mask1]

X = filtered_df[[ 'director_rank', 'rank_of_five_top_stars',
       'runtime_minuts',  'Action', 'Drama', 'Comedy',
       'Adventure', 'Mystery', 'Fantasy']]
y = filtered_df[["film_income"]]



X, X_test, y, y_test = train_test_split(X, y, test_size=.2, random_state=10) #hold out 20% of the data for final testing
X, y = np.array(X), np.array(y)
kf = KFold(n_splits=5, shuffle=True, random_state=71)
cv_lm_r2s, cv_lm_reg_r2s = [], []  # collect the validation results for both models
for train_ind, val_ind in kf.split(X, y):
    X_train, y_train = X[train_ind], y[train_ind]
    X_val, y_val = X[val_ind], y[val_ind]

    # simple linear regression
    lm = LinearRegression()
    lm_reg = Ridge(alpha=1)

    lm.fit(X_train, y_train)
    cv_lm_r2s.append(lm.score(X_val, y_val))

    # ridge with feature scaling
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_val_scaled = scaler.transform(X_val)

    lm_reg.fit(X_train_scaled, y_train)
    cv_lm_reg_r2s.append(lm_reg.score(X_val_scaled, y_val))



print(f'Simple mean cv r^2: {np.mean(cv_lm_r2s):.3f} +- {np.std(cv_lm_r2s):.3f}')
print(f'Ridge mean cv r^2: {np.mean(cv_lm_reg_r2s):.3f} +- {np.std(cv_lm_reg_r2s):.3f}')

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
X_test_scaled = scaler.transform(X_test)
lm_reg = Ridge(alpha=1)
lm_reg.fit(X_scaled,y)
print(f'Ridge Regression test R^2: {lm_reg.score(X_test_scaled, y_test):.3f}')




