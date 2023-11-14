import pandas as pd
import re


def build_standings_df(teams, wins, losses):

    data = {'team' : teams
            ,'wins' : wins
            ,'losses' : losses}

    standings_df = pd.DataFrame(data)

    return standings_df

def combine_conference_df(west_standings_df, east_standings_df):

    return pd.concat([west_standings_df, east_standings_df])


def parse_current(results):

    teams_set = results.find_all('th', class_='left')
    stats_set = results.find_all('td', class_='right')

    teams_raw = [th.get_text(strip=True) for th in teams_set if th.get("data-stat") == "team_name"]
    teams_raw.pop(0)
    # change 'team(n)' to 'team'
    teams = [re.sub(r'\(\d+\)', '', team).strip() for team in teams_raw]
    wins = [td.get_text(strip=True) for td in stats_set if td.get("data-stat") == "wins"]
    losses = [td.get_text(strip=True) for td in stats_set if td.get("data-stat") == "losses"]

    return teams, wins, losses

def parse_projection(results):

    result_set = results.find_all('tr')

    teams = [row.find('td', {'data-stat': 'team_name'}).text.strip()
            for row in result_set
            if row.find('td', {'data-stat': 'team_name'})]

    wins = [row.find('td', {'data-stat': 'wins_avg'}).text.strip()
            for row in result_set
            if row.find('td', {'data-stat': 'wins_avg'})]

    losses = [row.find('td', {'data-stat': 'losses_avg'}).text.strip()
            for row in result_set
            if row.find('td', {'data-stat': 'losses_avg'})]

    return teams, wins, losses
