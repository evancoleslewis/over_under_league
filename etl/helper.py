import pandas as pd


def build_standings_df(teams, wins, losses):

    data = {'team' : teams
            ,'wins' : wins
            ,'losses' : losses}

    standings_df = pd.DataFrame(data)

    return standings_df

def combine_conference_df(west_standings_df, east_standings_df):

    return pd.concat([west_standings_df, east_standings_df])