import streamlit as st

page_bg_img = '''
<style> 
.stSidebar {
    background-image: url("https://sportsposterwarehouse.com/cdn/shop/files/nfl-logos-2024-poster-25605_1024x1024.jpg?v=1726256076");
    background-size: cover;
}
</style>
'''

import streamlit as st
import pandas as pd
from PIL import Image

team_logos = {
  "Arizona Cardinals": ("https://upload.wikimedia.org/wikipedia/en/thumb/7/72/Arizona_Cardinals_logo.svg/1024px-Arizona_Cardinals_logo.svg.png"),
"Atlanta Falcons": ("https://upload.wikimedia.org/wikipedia/en/thumb/c/c5/Atlanta_Falcons_logo.svg/1024px-Atlanta_Falcons_logo.svg.png"),
"Baltimore Ravens": ("https://upload.wikimedia.org/wikipedia/en/thumb/1/16/Baltimore_Ravens_logo.svg/1920px-Baltimore_Ravens_logo.svg.png"),
"Buffalo Bills": ("https://upload.wikimedia.org/wikipedia/en/thumb/7/77/Buffalo_Bills_logo.svg/1280px-Buffalo_Bills_logo.svg.png"),
"Carolina Panthers": ("https://upload.wikimedia.org/wikipedia/en/thumb/4/48/Las_Vegas_Raiders_logo.svg/800px-Las_Vegas_Raiders_logo.svg.png"),
"Chicago Bears": ("https://upload.wikimedia.org/wikipedia/en/thumb/1/15/Chicago_Bears_logo_primary.svg/800px-Chicago_Bears_logo_primary.svg.png"),
"Cincinnati Bengals": ("https://upload.wikimedia.org/wikipedia/commons/thumb/8/81/Cincinnati_Bengals_logo.svg/1280px-Cincinnati_Bengals_logo.svg.png"),
"Cleveland Browns": ("https://upload.wikimedia.org/wikipedia/en/thumb/d/d9/Cleveland_Browns_logo.svg/1024px-Cleveland_Browns_logo.svg.png"),
"Dallas Cowboys": ("https://upload.wikimedia.org/wikipedia/commons/thumb/1/15/Dallas_Cowboys.svg/800px-Dallas_Cowboys.svg.png"),
"Denver Broncos": ("https://upload.wikimedia.org/wikipedia/en/thumb/4/44/Denver_Broncos_logo.svg/1920px-Denver_Broncos_logo.svg.png"),
"Detroit Lions":("https://upload.wikimedia.org/wikipedia/en/thumb/7/71/Detroit_Lions_logo.svg/1024px-Detroit_Lions_logo.svg.png"),
"Green Bay Packers": ("https://upload.wikimedia.org/wikipedia/commons/thumb/5/50/Green_Bay_Packers_logo.svg/1280px-Green_Bay_Packers_logo.svg.png"),
"Houston Texans": ("https://upload.wikimedia.org/wikipedia/en/thumb/2/28/Houston_Texans_logo.svg/800px-Houston_Texans_logo.svg.png"),
"Indianapolis Colts": ("https://upload.wikimedia.org/wikipedia/commons/thumb/0/00/Indianapolis_Colts_logo.svg/800px-Indianapolis_Colts_logo.svg.png"),
"Jacksonville Jaguars": ("https://upload.wikimedia.org/wikipedia/en/thumb/7/74/Jacksonville_Jaguars_logo.svg/1024px-Jacksonville_Jaguars_logo.svg.png"),
"Kansas City Chiefs": ("https://upload.wikimedia.org/wikipedia/en/thumb/e/e1/Kansas_City_Chiefs_logo.svg/1280px-Kansas_City_Chiefs_logo.svg.png"),
"Las Vegas Raiders": ("https://upload.wikimedia.org/wikipedia/en/thumb/4/48/Las_Vegas_Raiders_logo.svg/800px-Las_Vegas_Raiders_logo.svg.png"),
"Los Angeles Chargers": ("https://upload.wikimedia.org/wikipedia/commons/thumb/a/a6/Los_Angeles_Chargers_logo.svg/1920px-Los_Angeles_Chargers_logo.svg.png"),
"Los Angeles Rams": ("https://upload.wikimedia.org/wikipedia/en/thumb/8/8a/Los_Angeles_Rams_logo.svg/1280px-Los_Angeles_Rams_logo.svg.png"),
"Miami Dolphins": ("https://upload.wikimedia.org/wikipedia/en/thumb/3/37/Miami_Dolphins_logo.svg/1024px-Miami_Dolphins_logo.svg.png"),
"Minnesota Vikings": ("https://upload.wikimedia.org/wikipedia/en/thumb/4/48/Minnesota_Vikings_logo.svg/800px-Minnesota_Vikings_logo.svg.png"),
"New England Patriots": ("https://upload.wikimedia.org/wikipedia/en/thumb/b/b9/New_England_Patriots_logo.svg/1920px-New_England_Patriots_logo.svg.png"),
"New Orleans Saints": ("https://upload.wikimedia.org/wikipedia/commons/thumb/5/50/New_Orleans_Saints_logo.svg/800px-New_Orleans_Saints_logo.svg.png"),
"New York Giants": ("https://upload.wikimedia.org/wikipedia/commons/thumb/6/60/New_York_Giants_logo.svg/1024px-New_York_Giants_logo.svg.png"),
"New York Jets": ("https://upload.wikimedia.org/wikipedia/commons/thumb/6/69/New_York_Jets_2024.svg/1280px-New_York_Jets_2024.svg.png"),
"Philadelphia Eagles": ("https://upload.wikimedia.org/wikipedia/en/thumb/8/8e/Philadelphia_Eagles_logo.svg/1280px-Philadelphia_Eagles_logo.svg.png"),
"Pittsburgh Steelers": ("https://upload.wikimedia.org/wikipedia/commons/thumb/d/de/Pittsburgh_Steelers_logo.svg/800px-Pittsburgh_Steelers_logo.svg.png"),
"San Francisco 49ers": ("https://upload.wikimedia.org/wikipedia/commons/thumb/3/3a/San_Francisco_49ers_logo.svg/1920px-San_Francisco_49ers_logo.svg.png"),
"Seattle Seahawks": ("https://upload.wikimedia.org/wikipedia/en/thumb/8/8e/Seattle_Seahawks_logo.svg/1920px-Seattle_Seahawks_logo.svg.png"),
"Tampa Bay Buccaneers": ("https://upload.wikimedia.org/wikipedia/en/thumb/a/a2/Tampa_Bay_Buccaneers_logo.svg/1024px-Tampa_Bay_Buccaneers_logo.svg.png"),
"Tennessee Titans": ("https://upload.wikimedia.org/wikipedia/en/thumb/c/c1/Tennessee_Titans_logo.svg/1280px-Tennessee_Titans_logo.svg.png"),
"Washington Commanders": ("https://upload.wikimedia.org/wikipedia/commons/thumb/0/0c/Washington_Commanders_logo.svg/1920px-Washington_Commanders_logo.svg.png")
}

# Load the main DataFrame


st.markdown(page_bg_img, unsafe_allow_html=True)

# Add your Streamlit app content here
@st.cache_data
def load_data():
    return pd.read_csv('updated_ranks.csv')

df= load_data()

st.title("Regular Season Predictor")
st.write("Useful for both regular season matchups and playoffs as well!")
team1 = st.selectbox("Select the first team", df['Team'].unique())
if team1 in team_logos:
    st.image(team_logos[team1], caption=team1, width=200)
# Create a select box for the second team
team2 = st.selectbox("Select the second team", df['Team'].unique())
if team2 in team_logos:
    st.image(team_logos[team2], caption=team2, width=200)

# Find the ranks of the selected teams
team1_rank = df[df['Team'] == team1]['New_Rank'].values[0]
team2_rank = df[df['Team'] == team2]['New_Rank'].values[0]
team1_D_rank =  df[df['Team'] == team1]['D_Rank'].values[0]
team2_D_rank = df[df['Team'] == team2]['D_Rank'].values[0]
explain = "It's a tie"
loser = team2

# Determine the winner
if team1_rank > team2_rank:
    winner = team1
    loser = team2
    explain = "had the high average rank between offense and defense and their losses than the"
elif team1_rank < team2_rank:
    winner = team2
    loser = team1
    explain = "had the high average rank between offense and defense and their losses than the"

else:
    if team1_D_rank > team2_D_rank:
        winner = team1
        loser = team2
        explain = "won because although both teams had a overall tie on the average rank calculated, we use the tiebreaker of whichever team had the higher defensive metric (arguably the most important side of the football) and this team had a higher defensive metric than"
    elif team1_D_rank < team2_D_rank:
        winner = team2
        loser = team1
        explain = "won because although both teams had a overall tie on the average rank calculated, we use the tiebreaker of whichever team had the higher defensive metric (arguably the most important side of the football) and this team had a higher defensive metric than"
    else:
        winner = "It's a tie"
        
print(winner)

# Display the result
st.subheader(f"The winner between {team1} and {team2} is: {winner}!")
st.subheader(f"Explanation:")   
st.write(f"The {winner} {explain} {loser}!")
