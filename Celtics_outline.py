"""
Keklan Baker
Right now this is taking end of year average data. Want to expand to per game data eventually.
"""
import numpy as np
from nba_api.stats.endpoints import playercareerstats
from nba_api.stats.endpoints import playergamelog
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Jason Tatum #0
career = playercareerstats.PlayerCareerStats(player_id='1628369') 
Tatum_career_df = career.get_data_frames()[0]
gamelog = playergamelog.PlayerGameLog(player_id='1628369', season='2023-24', season_type_all_star='Regular Season')
Tatum_per_game_23_24 = gamelog.get_data_frames()[0]

# This prints out a big table showing the correlation between different pieces of data
# You can see that I turned Win/Loss into True/False. Most times you cannot use text to optimize stuff 
Tatum_per_game_23_24['WL'] = Tatum_per_game_23_24['WL'].replace({ 'W': True, 'L': False }) 
corr_matrix = Tatum_per_game_23_24.iloc[0:67, 5:-1].corr()
corr_3pts = corr_matrix['FG3M']

def corr_col(string):
    """ Display with heat map what the kek is going on here
            Input: the name of the column that we want to see how other columns correlate with
            Output: heatmap (column) of correlation """
    single_column_corr = corr_matrix[string]  # This is a Series of shape (20,)
    single_column_corr_2d = single_column_corr.values.reshape(-1, 1) # Reshape the series to be 2D (so that it's compatible with sns.heatmap)
    plt.figure(figsize=(5, 8)) #resize map
    sns.heatmap(single_column_corr_2d, annot=True, cmap='coolwarm', cbar=True, yticklabels=corr_matrix.index)
    plt.show()

print(Tatum_per_game_23_24['MATCHUP'])

"""
Ideas:
1) get data for each individual game in 23-24 yr
2) using shooting percentage from each game to tell us how opponents defense is
    high shooting % means bad defense  &  low shooting % means good def
    will want to average the two or three games they play against each team (reduces error by averaging)
3) use FG3A and FG3M and FG3P; find weights for each
4) make model which takes in [opponent, avg FG3P, avg FG3A] outputs [avg FG3M] for that game

Future Ideas:
see if this changes year to year (obvious trends?)
"""


# Data points
"""
opponent = Tatum_per_game_23_24["Matchup"]
    # figure out if it is away or home
    # figure out how many 3's the opponent conceeded 
Tatum_avg_3s = np.sum(Tatum_per_game_23_24["FG3M"].tolist())/len(Tatum_per_game_23_24["FG3M"].tolist())
Tatum_avg_3s_attempted = np.sum(Tatum_per_game_23_24["FG3A"].tolist())/len(Tatum_per_game_23_24["FG3A"].tolist())
opponent_3s_against = 1

# Model # Weight #
m1w1 = 1
m1w2 = 1
m1w3 = 1

m2w1 = 1
m2w2 = 1
m2w3 = 1
m2w4 = 1

#Tatum_model1 = m1w1*Tatum_avg_3s + m1w2*opponent_3s_against
#Tatum_model2 = m2w1*Tatum_avg_3s + m2w2*Tatum_avg_3s_attempted + m2w3*opponent_3s_against + m2w4*homeVSaway
"""
