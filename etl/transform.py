from bs4 import BeautifulSoup
import config
import etl.helper as helper
import re


import logging
logging.basicConfig(filename='log/transform.log', filemode='w', level=logging.INFO)



def get_conference_standings(html, conference_id):
    """
    Get standings for given conference from html.
    """
    soup = BeautifulSoup(html, 'html.parser')

    results = soup.find(id=conference_id)
    teams_set = results.find_all('th', class_='left')
    stats_set = results.find_all('td', class_='right')

    teams_raw = [th.get_text(strip=True) for th in teams_set if th.get("data-stat") == "team_name"]
    teams_raw.pop(0)
    # change 'team(n)' to 'team'
    teams = [re.sub(r'\(\d+\)', '', team).strip() for team in teams_raw]
    wins = [td.get_text(strip=True) for td in stats_set if td.get("data-stat") == "wins"]
    losses = [td.get_text(strip=True) for td in stats_set if td.get("data-stat") == "losses"]

    conference_standings_df = helper.build_standings_df(teams, wins, losses)

    return conference_standings_df

def get_standings(html):
    """
    Gets standings for both conferences from html.
    """

    west_standings_df = get_conference_standings(html, config.WESTERN_CONFERENCE_ID)
    east_standings_df = get_conference_standings(html, config.EASTERN_CONFERENCE_ID)

    all_standings_df = helper.combine_conference_df(east_standings_df, west_standings_df)

    return all_standings_df