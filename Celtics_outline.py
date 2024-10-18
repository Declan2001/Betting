"""
Keklan Baker
Right now this is taking end of year average data. Want to expand to per game data eventually.
"""
import numpy as np
from nba_api.stats.endpoints import playercareerstats
from nba_api.stats.endpoints import playergamelog
import pandas as pd

# Jason Tatum #0
career = playercareerstats.PlayerCareerStats(player_id='1628369') 
Tatum_career_df = career.get_data_frames()[0]
gamelog = playergamelog.PlayerGameLog(player_id='1628369', season='2023-24', season_type_all_star='Regular Season')
Tatum_per_game_23_24 = gamelog.get_data_frames()[0]


# This prints out a big table showing the correlation between different pieces of data
#   This can be useful to pick which features to use in your model. Though I would say that
#   21 cols is basically nothing.
# You can see that I turned Win/Loss into True/False. Most times you cannot use text to optimize stuff
#   The team being played against is another col you can work on fitting into the model, prob useful
Tatum_per_game_23_24['WL'] = Tatum_per_game_23_24['WL'].replace({ 'W': True, 'L': False })
print(Tatum_per_game_23_24.iloc[0:67, 5:-1].corr())

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
