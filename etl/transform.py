from bs4 import BeautifulSoup
import config
import etl.helper as helper
import logging


def get_conference_standings(html, current_or_projection, conference_id):
    """
    Get standings for given conference from html.
    """

    conference_standings_df = None
    soup = BeautifulSoup(html, 'html.parser')
    results = soup.find(id=conference_id)

    if current_or_projection == 'current':
        teams, wins, losses = helper.parse_current(results)
    if current_or_projection == 'projection':
        teams, wins, losses = helper.parse_projection(results)

    conference_standings_df = helper.build_standings_df(teams, wins, losses)

    return conference_standings_df

def get_standings(html, current_or_projection):
    """
    Gets standings for both conferences from html.
    """

    west_id = config.RUN_DICT[current_or_projection]['western']
    east_id = config.RUN_DICT[current_or_projection]['eastern']

    west_standings_df = get_conference_standings(html, current_or_projection, west_id)
    east_standings_df = get_conference_standings(html, current_or_projection, east_id)

    all_standings_df = helper.combine_conference_df(east_standings_df, west_standings_df)

    return all_standings_df