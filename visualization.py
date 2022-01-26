import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np


csv_data = pd.read_csv("result7_after_reomve_zero_from_dirctors.csv")
df_for_plot_only = csv_data.loc[: , [ 'filem_name', 'director_rank',  'rank_of_five_top_stars',
       'film_income', 'runtime_minuts', 'release_year' ] ]


mask1 = (df_for_plot_only.loc[: , 'director_rank' ] > 6000 ) & \
        (df_for_plot_only.loc[: , 'rank_of_five_top_stars'] < 50000 ) &\
        (df_for_plot_only.loc[: , 'film_income'] < 400000000 )

# df2 = df_for_plot_only[mask1]
sns.pairplot(df_for_plot_only[mask1])
print(df_for_plot_only[mask1].shape)

#
# plt.plot( df_for_plot_only['release_year'] , df_for_plot_only["film_income"] )

# x = df_for_plot_only['release_year']
# y = df_for_plot_only["film_income"]
# plt.scatter(x, y)

# df2 = df_for_plot_only[mask1]
# sns.set_theme(style="whitegrid")
# ax = sns.boxplot(x=df2["sum_of_first_five"])
# ax = sns.boxplot(x=df2["film_income"])


# sns.lmplot( x="director_rank", y="film_income", data=df_for_plot_only)
# sns.lmplot( x="sum_of_first_five", y="film_income", data=df_for_plot_only)

plt.show()
